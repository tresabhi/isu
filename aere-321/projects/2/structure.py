import math
import numpy as np
from enum import Enum
import matplotlib.pyplot as plt

np.set_printoptions(linewidth=1600)


class Material:
    def __init__(self, E: float, I: float, A: float, h: float):
        self.E = E
        self.I = I
        self.A = A
        self.h = h


class JointType(Enum):
    FREE = 1
    FIXED = 2


class Joint:
    id = -1

    def __init__(
        self,
        type: JointType,
        x: float,
        y: float,
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

    def relative_to(self, other: "Joint"):
        dx = self.x - other.x
        dy = self.y - other.y

        theta = math.atan2(dy, dx)
        L = math.sqrt(dx**2 + dy**2)

        return theta, L


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

        self.dx = joint_1.x - joint_0.x
        self.dy = joint_1.y - joint_0.y

        theta, L = self.theta, self.L = joint_1.relative_to(joint_0)
        c, s = self.c, self.s = math.cos(theta), math.sin(theta)

        self.material = material
        E, I, A = material.E, material.I, material.A

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

        K_padded = self.K_padded = np.zeros(
            shape=(3 * (max_joint_id + 1), 3 * (max_joint_id + 1))
        )

        self.joint_indices = [
            *[self.joint_0.id * 3 + i for i in range(3)],
            *[self.joint_1.id * 3 + i for i in range(3)],
        ]

        for u, i in enumerate(self.joint_indices):
            for v, j in enumerate(self.joint_indices):
                K_padded[i, j] += K[u, v]

    def v(self, d_padded: np.matrix):
        return d_padded[np.ix_(self.joint_indices)]

    def u(self, d_padded: np.matrix):
        return self.T * self.v(d_padded)

    def Q(self, d_padded: np.matrix):
        return self.k * self.u(d_padded)

    def F(self, d_padded: np.matrix):
        return self.T.T * self.Q(d_padded)

    def sigma_a(self, d_padded: np.matrix):
        return self.Q(d_padded)[3].item() / self.material.A

    def epsilon_a(self, d_padded: np.matrix):
        return self.sigma_a(d_padded) / self.material.E

    def sigma_b(self, d_padded: np.matrix, c: float, x: float):
        Q = self.Q(d_padded)
        return c * (Q[1].item() * x - Q[2].item()) / self.material.I

    def plot_strain(self, d_padded: np.matrix, points=2**4):
        E = self.material.E
        L = self.L
        c = self.material.h / 2

        xs = np.linspace(0, L, points)

        sigma_a = self.sigma_a(d_padded)
        sigma_b_top = self.sigma_b(d_padded, c, xs)
        sigma_b_bottom = self.sigma_b(d_padded, -c, xs)
        sigma_top = sigma_a + sigma_b_top
        sigma_bottom = sigma_a + sigma_b_bottom

        epsilon_top = sigma_top / E
        epsilon_bottom = sigma_bottom / E

        plt.plot(xs, epsilon_top, label=f"Member {self.id} Top")
        plt.plot(xs, epsilon_bottom, label=f"Member {self.id} Bottom")
        plt.title(f"Member {self.id} Strain")
        plt.legend()
        plt.xlabel("x (in)")
        plt.ylabel("epsilon (in/in)")
        plt.tight_layout()
        plt.show()


class Structure:
    def __init__(
        self, material: Material, joints: list[Joint], _members: list[tuple[int, int]]
    ):
        self.material = material
        self.joints = joints

        max_joint_id = len(joints) - 1

        members: list[Member] = []
        member_id = 0
        for joint_id_0, joint_id_1 in _members:
            joint_0 = joints[joint_id_0]
            joint_1 = joints[joint_id_1]

            joint_0.id = joint_id_0
            joint_1.id = joint_id_1

            member = Member(member_id, material, joint_0, joint_1, max_joint_id)

            members.append(member)
            member_id += 1

        self.members = members

        s_padded = sum(member.K_padded for member in members)

        free_indices: list[int] = []
        fixed_indices: list[int] = []
        P_padded: list[list[float]] = []

        for joint_id in range(max_joint_id + 1):
            joint = joints[joint_id]
            external_indices = [joint_id * 3, joint_id * 3 + 1, joint_id * 3 + 2]

            P_padded += [[joint.force_x], [joint.force_y], [joint.moment]]

            if joint.type == JointType.FREE:
                free_indices += external_indices
            elif joint.type == JointType.FIXED:
                fixed_indices += external_indices

        s = self.s = s_padded[np.ix_(free_indices, free_indices)]
        P_padded = np.matrix(P_padded)
        P = self.P = P_padded[np.ix_(free_indices)]
        d = self.d = np.linalg.solve(s, P)

        d_padded = self.d_padded = np.zeros((3 * (max_joint_id + 1), 1))
        d_padded[np.ix_(free_indices)] = d

    def render(self, exaggeration=100.0, points=2**4):
        _, ax = plt.subplots()

        for member in self.members:
            ax.plot(
                [member.joint_0.x, member.joint_1.x],
                [member.joint_0.y, member.joint_1.y],
                "--",
                color=(0.75, 0.75, 0.75),
                label="Original" if member.id == 0 else "",
            )

            [u_0, v_0, theta_0] = [
                self.d_padded[member.joint_0.id * 3 + i, 0] * exaggeration
                for i in range(3)
            ]
            [u_1, v_1, theta_1] = [
                self.d_padded[member.joint_1.id * 3 + i, 0] * exaggeration
                for i in range(3)
            ]

            ul_0 = member.c * u_0 + member.s * v_0
            vl_0 = -member.s * u_0 + member.c * v_0
            ul_1 = member.c * u_1 + member.s * v_1
            vl_1 = -member.s * u_1 + member.c * v_1

            xs = np.linspace(0, 1, points)
            N1 = 1 - 3 * xs**2 + 2 * xs**3
            N2 = member.L * (xs - 2 * xs**2 + xs**3)
            N3 = 3 * xs**2 - 2 * xs**3
            N4 = member.L * (-(xs**2) + xs**3)

            v_local = N1 * vl_0 + N2 * theta_0 + N3 * vl_1 + N4 * theta_1
            u_local = N1 * ul_0 + N3 * ul_1

            xs = (
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

            ax.plot(
                xs,
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

        for member in self.members:
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


structure = Structure(
    Material(10200, (1 * 0.25**3) / 12, 1 * 0.25, 0.25),
    [
        Joint(JointType.FIXED, 0, 0),
        Joint(JointType.FREE, 0, 8, 0, 0, 100 * 1e-3),
        Joint(JointType.FREE, 0, 8 + 8),
        Joint(JointType.FIXED, 16.25, 0),
        Joint(JointType.FREE, 16.25, 8),
        Joint(JointType.FREE, 16.25, 8 + 8, 10 * 1e-3, 0, 0),
    ],
    [
        (0, 1),
        (1, 2),
        (3, 4),
        (4, 5),
        (1, 4),
        (2, 5),
    ],
)

structure.solve()
structure.render()

for member in structure.members:
    member.plot_strain(structure.d_padded)
