import math
import numpy as np
from enum import Enum
import matplotlib.pyplot as plt

# Once again, like last time, the print width by default is too short so I
# expand it.
np.set_printoptions(linewidth=1600)


# This class holds the material properties of the structure so that I can
# easily access and share them.
class Material:
    def __init__(self, E: float, I: float, A: float, h: float):
        self.E = E
        self.I = I
        self.A = A
        self.h = h


# This helps discriminate between the two types of joints. This time, there
# are no rollers so the logic for free indices will be easy.
class JointType(Enum):
    FREE = 1
    FIXED = 2


# This holds the properties of a joint.
class Joint:

    # The id is an invalid one by default to cause any errors if I accidentally
    # end up using it before it's overwritten with the correct id by the
    # Structure class.
    id = -1

    def __init__(
        self,
        type: JointType,
        x: float,
        y: float,
        # The externals are 0 by default so that I don't have to type too much
        # every time I create a regular forceless joint.
        force_x=0.0,
        force_y=0.0,
        moment=0.0,
    ):
        self.type = type
        self.x = x
        self.y = y
        self.force_x = force_x
        self.force_y = force_y
        self.moment = moment

    # This returns the relative length and angle between two joints.
    def relative_to(self, other: "Joint"):
        dx = self.x - other.x
        dy = self.y - other.y

        # Using the arctangent2 function to avoid division by 0 causing bad
        # angles.
        theta = math.atan2(dy, dx)
        L = math.sqrt(dx**2 + dy**2)

        return theta, L, dx, dy


class Member:
    def __init__(
        self,
        id: int,
        material: Material,
        joint_0: Joint,
        joint_1: Joint,
        max_joint_id: int,
    ):
        self.id = id
        self.joint_0 = joint_0
        self.joint_1 = joint_1

        # Using that relative function here but I don't need dx and dy here
        # right now (but I will later so I will save it in self).
        theta, L, _, _ = self.theta, self.L, self.dx, self.dy = joint_1.relative_to(
            joint_0
        )
        # c and s short forms save me typing and some compute power.
        c, s = self.c, self.s = math.cos(theta), math.sin(theta)

        self.material = material
        # Pull out E, I, and A for ease of typing.
        E, I, A = material.E, material.I, material.A

        # Straight from the lectures. Also store T in self.T for later use.
        T = self.T = np.matrix(
            [
                [c, s, 0, 0, 0, 0],
                [-s, c, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, c, s, 0],
                [0, 0, 0, -s, c, 0],
                [0, 0, 0, 0, 0, 1],
            ]
        )
        # Also from the lecture.
        k = self.k = ((E * I) / L**3) * np.matrix(
            [
                [(A * L**2) / I, 0, 0, -(A * L**2) / I, 0, 0],
                [0, 12, 6 * L, 0, -12, 6 * L],
                [0, 6 * L, 4 * L**2, 0, -6 * L, 2 * L**2],
                [-(A * L**2) / I, 0, 0, (A * L**2) / I, 0, 0],
                [0, -12, -6 * L, 0, 12, -6 * L],
                [0, 6 * L, 2 * L**2, 0, -6 * L, 4 * L**2],
            ]
        )
        K = self.K = T.T * k * T

        # Adding a bunch of 0's top-left and bottom-right based on the current
        # id and the maximum id which dictates the size of the K matrix.
        K_padded = self.K_padded = np.zeros(
            shape=(3 * (max_joint_id + 1), 3 * (max_joint_id + 1))
        )

        # Unlike the 1D beam, the joints 0 and 1 may not have continuous ids so
        # I have to compensate for that here by recording the freedom of
        # movement indices.
        self.joint_indices = [
            *[self.joint_0.id * 3 + i for i in range(3)],
            *[self.joint_1.id * 3 + i for i in range(3)],
        ]

        # And then I pad in the correct places which might sometimes might be
        # between the joints 0 and 1.
        for u, i in enumerate(self.joint_indices):
            for v, j in enumerate(self.joint_indices):
                K_padded[i, j] += K[u, v]

    # v is just a small subset of d_padded.
    def v(self, d_padded: np.matrix):
        return d_padded[np.ix_(self.joint_indices)]

    # u is the local version of v.
    def u(self, d_padded: np.matrix):
        return self.T * self.v(d_padded)

    # Q is als local so it uses u instead of v and multiplies it to k which
    # is also local to get the forces and moments.
    def Q(self, d_padded: np.matrix):
        return self.k * self.u(d_padded)

    # Back to global forces and moments.
    def F(self, d_padded: np.matrix):
        return self.T.T * self.Q(d_padded)

    # Stress due to axial force.
    def sigma_a(self, d_padded: np.matrix):
        return self.Q(d_padded)[3].item() / self.material.A

    # Strain due to axial force.
    def epsilon_a(self, d_padded: np.matrix):
        return self.sigma_a(d_padded) / self.material.E

    # Stress due to bending.
    def sigma_b(self, d_padded: np.matrix, c: float, x: float):
        Q = self.Q(d_padded)
        return c * (Q[1].item() * x - Q[2].item()) / self.material.I

    # Let's plot the strain for this member!
    def plot_strain(self, d_padded: np.matrix, points=2**4):
        E = self.material.E
        L = self.L
        c = self.material.h / 2

        # xs here is like "x's" much like saying "dogs" to mean the plural of
        # "dog".
        xs = np.linspace(0, L, points)

        # Thought these functions I wrote accept floats for x, it's okay to
        # pass a numpy array here since numpy will broadcast it.
        sigma_a = self.sigma_a(d_padded)
        sigma_b_top = self.sigma_b(d_padded, c, xs)
        sigma_b_bottom = self.sigma_b(d_padded, -c, xs)
        sigma_top = sigma_a + sigma_b_top
        sigma_bottom = sigma_a + sigma_b_bottom

        # Strains are just one division away.
        epsilon_top = sigma_top / E
        epsilon_bottom = sigma_bottom / E

        # Matplotlib to the rescue!
        plt.plot(xs, epsilon_top, label=f"Member {self.id} Top")
        plt.plot(xs, epsilon_bottom, label=f"Member {self.id} Bottom")
        plt.title(f"Member {self.id} Strain")
        plt.legend()
        plt.xlabel("x (in)")
        plt.ylabel("epsilon (in/in)")
        plt.tight_layout()
        plt.show()


# The structure class really brings it all together.
class Structure:
    # I made this class accept a very limited amount of data for ease of use
    # even though I only use it like once haha. So there's the Material
    # instance of course, followed by a list of joints, and a list of tuples
    # with the joint ids which form the ends of each member. I was inspired by
    # the binary formal of GLB files: https://docs.fileformat.com/3d/glb/
    def __init__(
        self, material: Material, joints: list[Joint], _members: list[tuple[int, int]]
    ):
        self.material = material
        self.joints = joints

        # Compute this and store it because I use it a lot.
        max_joint_id = len(joints) - 1

        # This is where I go through the indices and assemble the members.
        members: list[Member] = []
        member_id = 0
        for joint_id_0, joint_id_1 in _members:

            # The associated joints.
            joint_0 = joints[joint_id_0]
            joint_1 = joints[joint_id_1]

            # Rectify the ids of the joints which are -1 by default since they
            # don't know where they're placed in the list.
            joint_0.id = joint_id_0
            joint_1.id = joint_id_1

            # Form the member.
            member = Member(member_id, material, joint_0, joint_1, max_joint_id)

            # And then append it.
            members.append(member)
            member_id += 1

        # Store it for later too.
        self.members = members

        # Since the K's are padded by default, their sum, s, will also be
        # padded.
        s_padded = sum(member.K_padded for member in members)

        # Now time to figure out what can move and what cannot. While I am at
        # it, I will also assemble the P vector.
        free_indices: list[int] = []
        P_padded: list[list[float]] = []

        for joint_id in range(max_joint_id + 1):
            joint = joints[joint_id]

            # The ids related to this joint are 3 times its own id and added to
            # it 0, 1, and 2.
            external_indices = [joint_id * 3, joint_id * 3 + 1, joint_id * 3 + 2]

            # Once again, while I am at it, I also append the correct values to
            # P. They're wrapped in lists (so like a list in a list) since
            # these are are new columns. Adding them in a list just 1 layer
            # deep would make it a row vector instead of a column vector.
            P_padded += [[joint.force_x], [joint.force_y], [joint.moment]]

            # If it's free, add its indices to the list of free indices.
            if joint.type == JointType.FREE:
                free_indices += external_indices

        # Trim out all the indices that are not free.
        s = self.s = s_padded[np.ix_(free_indices, free_indices)]

        # Convert that P column vector I assembled into a real np matrix.
        P_padded = np.matrix(P_padded)

        # Trim P much like s.
        P = self.P = P_padded[np.ix_(free_indices)]

        # Solve for d finally and record it in self so that other methods
        # can use it at any time.
        d = self.d = np.linalg.solve(s, P)

        # Also add d back with a bunch if 0s for the fixed indices and store
        # that too.
        d_padded = self.d_padded = np.zeros((3 * (max_joint_id + 1), 1))
        d_padded[np.ix_(free_indices)] = d

    # This part I understand the least but I tried my best to follow ACS
    # College of Engineering's guide. This accepts just exaggeration and
    # the default amount of points that I chose is good enough for most
    # cases.
    def render(self, exaggeration=100.0, points=2**4):
        # There's going to be a bunch of plots overlaid on top of each other
        # giving the illusion that it's one image.
        _, ax = plt.subplots()

        # Loop through all the members.
        for member in self.members:

            # The original members are list linear interpolations.
            ax.plot(
                [member.joint_0.x, member.joint_1.x],
                [member.joint_0.y, member.joint_1.y],
                "--",
                color=(0.75, 0.75, 0.75),
                label="Original" if member.id == 0 else "",
            )

            # Okay, I am proud of myself on this one with my usage of Python
            # syntax. But essentially, I loop through a range of 3 (so that's
            # 0, 1, and 2) and to that I add the joint's id multiplied by 3
            # which gives the correct index to pull values from the d_padded
            # column vector.
            r = range(3)
            [u_0, v_0, theta_0] = [
                self.d_padded[member.joint_0.id * 3 + i, 0] * exaggeration for i in r
            ]
            [u_1, v_1, theta_1] = [
                self.d_padded[member.joint_1.id * 3 + i, 0] * exaggeration for i in r
            ]

            # Then localize the displacements using trig functions.
            ul_0 = member.c * u_0 + member.s * v_0
            vl_0 = -member.s * u_0 + member.c * v_0
            ul_1 = member.c * u_1 + member.s * v_1
            vl_1 = -member.s * u_1 + member.c * v_1

            # These are values of t from 0 to 1 (so this isn't in inches, it's
            # just an interpolator). It may as well be called t because it acts
            # like a parametric variable.
            xs = np.linspace(0, 1, points)

            # Use Hermite shape functions to get the coefficients for the
            # solution of the differential equation.
            N1 = 1 - 3 * xs**2 + 2 * xs**3
            N2 = member.L * (xs - 2 * xs**2 + xs**3)
            N3 = 3 * xs**2 - 2 * xs**3
            N4 = member.L * (-(xs**2) + xs**3)

            # The real, combined, offsets in local coordinates.
            v_local = N1 * vl_0 + N2 * theta_0 + N3 * vl_1 + N4 * theta_1
            u_local = N1 * ul_0 + N3 * ul_1

            # The same thing as above, but offset by the joints' original
            # positions and the real displacements, but this time in global
            # coordinates.
            sx = (
                member.joint_0.x
                + xs * member.dx
                - member.s * v_local
                + member.c * u_local
            )
            ys = (
                member.joint_0.y
                + xs * member.dy
                + member.c * v_local
                + member.s * u_local
            )

            # Plot 'em!
            ax.plot(
                sx,
                ys,
                "k-",
                linewidth=2,
                label=(
                    f"Deformed (x{exaggeration} exaggeration)" if member.id == 0 else ""
                ),
            )

        ax.set_aspect("equal")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.legend()

        plt.title("Deformed Structure")
        plt.show()

    # This function just prints everything I need to show to prove that the
    # code works with all correct intermediate values. Most of them are just
    # loops so I won't comment on them.
    def solve(self):
        for member in self.members:
            print(f"k_{member.id} =\n{member.k}\n")

        for member in self.members:
            print(f"K_{member.id} =\n{member.K}\n")

        print(f"P =\n{self.P}\n")

        print(f"s =\n{self.s}\n")

        print(f"d =\n{self.d}\n")

        for member in self.members:
            print(f"u_{member.id} =\n{member.u(self.d_padded)}\n")

        for member in self.members:
            print(f"Q_{member.id} =\n{member.Q(self.d_padded)}\n")

        for member in self.members:
            print(f"F_{member.id} =\n{member.F(self.d_padded)}\n")

        for member in self.members:
            print(f"sigma_a_{member.id} = {member.sigma_a(self.d_padded)}")
            print(f"epsilon_a_{member.id} = {member.epsilon_a(self.d_padded)}\n")

        # This loop is a bit more involved than the rest as there's no method
        # I implemented in the Member class to get the reaction forces since
        # they're already a part of F(). Nevertheless, here's that implemented.
        for member in self.members:
            # For both joints, I check if it's fixed. And if it is, I extract
            # the right indices which are 0, 1, and 2 for the first joint and
            # 3, 4, and 5 for the second joint.

            if member.joint_0.type == JointType.FIXED:
                print(f"Reaction forces at joint {member.joint_0.id} =")
                print(member.F(self.d_padded)[np.ix_([0, 1, 2])], end="\n\n")

            if member.joint_1.type == JointType.FIXED:
                print(f"Reaction forces at joint {member.joint_1.id} =")
                print(member.F(self.d_padded)[np.ix_([3, 4, 5])], end="\n\n")


# lecture_example_1 = Structure(
#     Material(29000, 310, 11.8, -1),
#     [
#         Joint(JointType.FIXED, 0, 0),
#         Joint(JointType.FREE, 10 * 12, 20 * 12, 50, 0, -125 * 12),
#         Joint(JointType.FIXED, (10 + 20) * 12, 20 * 12),
#     ],
#     [
#         (0, 1),
#         (1, 2),
#     ],
# )


# You first start off by creating a structure class.
structure = Structure(
    # Give it a material.
    Material(10200, (1 * 0.25**3) / 12, 1 * 0.25, 0.25),
    # The joints.
    [
        Joint(JointType.FIXED, 0, 0),
        Joint(JointType.FREE, 0, 8, 0, 0, 100 * 1e-3),
        Joint(JointType.FREE, 0, 8 + 8),
        Joint(JointType.FIXED, 16.25, 0),
        Joint(JointType.FREE, 16.25, 8),
        Joint(JointType.FREE, 16.25, 8 + 8, 10 * 1e-3, 0, 0),
    ],
    # And then combine the joints.
    [
        (0, 1),
        (1, 2),
        (3, 4),
        (4, 5),
        (1, 4),
        (2, 5),
    ],
)

# The solve method logs all the required intermediate values.
structure.solve()

# And the render method shows the deformed structure.
structure.render()

# And as for the strain plots, I loop through all the members and use the
# method I made just for this.
for member in structure.members:
    member.plot_strain(structure.d_padded)
