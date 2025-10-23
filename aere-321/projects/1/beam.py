# I am using numpy to handle matrices; there's no need for me to make my own
# implementation.
import numpy as np

# Enums are great for discrimination in TypeScript and Rust. Python doesn't
# have them out of the box, but there's a class.
from enum import Enum

# Numpy's print width was too narrow to fit big matrices so I changed it.
np.set_printoptions(linewidth=200)


# The support type discriminator. Logic later uses this to figure out what's
# fixed and free.
class SupportType(Enum):
    NONE = 1
    FIXED = 2
    ROLLER = 3


# This is a purely nominal class that I use for interfacing with the Beam class
# later.
class Support:
    def __init__(self, x: float, type: SupportType):
        self.type = type
        self.x = x


# Another enum, this time for the external force or moment type.
class ExternalType(Enum):
    FORCE = 1
    MOMENT = 2


# Another nominal class without methods. The held values here will be used in
# logic below.
class External:
    def __init__(self, x: float, type: ExternalType, value: float):
        self.x = x
        self.type = type
        self.value = value


# Finally, a class with methods! This class represents the joint between two
# members.
class Joint:
    # A joint can only have 1 support, but any number of external moments and
    # forces.
    def __init__(self, support: Support, externals: list[External]):

        # Store the support.
        self.support = support

        # Filter forces and moments into separate lists.
        external_forces = [
            external for external in externals if external.type == ExternalType.FORCE
        ]
        external_moments = [
            external for external in externals if external.type == ExternalType.MOMENT
        ]

        # Find resultants and store them.
        self.external_force = sum([external.value for external in external_forces])
        self.external_moment = sum([external.value for external in external_moments])

        # Also cache the freedoms of the joint to avoid recomputing them.
        self.free_displacement = support.type == SupportType.NONE
        self.free_rotation = support.type != SupportType.FIXED

    # This is a part of the debug renderer which draws the beam in the console.
    # The joint renders a pipe ( |) and the support type which can either be a
    # fixed block (░░) or a roller (◯|). In the case of a free joint, the pipe
    # us left alone.
    def render(self):

        # Default to a pipe.
        icon = " |"

        # Turn pipe into a fixed support.
        if self.support.type == SupportType.FIXED:
            icon = "░░"
        elif self.support.type == SupportType.ROLLER:
            icon = "◯|"

        # Print the joint type and external forces and moments.
        print(f"{icon} → {self.external_force} ⭯ {self.external_moment}")

    # Print P_i and P_i+1.
    def print_loads(self, id: int):
        print(f"P_{id} = {self.external_force}")
        print(f"P_{id + 1} = {self.external_moment}")


# This class represents members that sit between two joints.
class Member:
    # Members accept an id, starting from 0 because it's Python, the x position
    # of the left end of the member, E and I of the material, L of the member
    # (not the whole beam, that was a nasty bug!), and the left and right
    # joints. The left joint is the same as the right joint for the last member
    # and vice versa.
    def __init__(
        self, id: int, x: float, E: float, I: float, L: float, left: Joint, right: Joint
    ):
        # Store the values.
        self.id = id
        self.x = x

        self.E = E
        self.I = I
        self.L = L

        self.left = left
        self.right = right

    # Computing the k value is a method here and not a part of __init__ because
    # this class is always initialized with a dummy joint for the right side of
    # the beam which is later replaced with a real joint when the left joint of
    # the next member is initialized.
    def k(self):

        # Declare local variables for ease of reading.
        E = self.E
        I = self.I
        L = self.L

        # The goofy matrix from lecture.
        return ((E * I) / L**3) * np.matrix(
            [
                [12, 6 * L, -12, 6 * L],
                [6 * L, 4 * L * L, -6 * L, 2 * L * L],
                [-12, -6 * L, 12, -6 * L],
                [6 * L, 2 * L * L, -6 * L, 4 * L * L],
            ]
        )

    # The k matrix is normally trimmed. For instance, the k matrix of member
    # a joint of displacement id 3 will have the 3rd id in the first two (index
    # of 0). So, we need to pad.
    def k_padded(self, max_id: int):

        # Rows and columns to pad above and below was an interesting algebraic
        # problem. Fortunately, when I switched to 0-based indexing, it became
        # much easier.
        top_left_padding = 2 * self.id
        bottom_right_padding = 2 * (max_id - self.id)

        # Numpy has a built-in function for padding matrices.
        return np.pad(
            self.k(),
            pad_width=(
                (top_left_padding, bottom_right_padding),
                (top_left_padding, bottom_right_padding),
            ),
        )

    # The u matrix is a subset of the full d column vector.
    def u(self, d: np.matrix):

        # This is the most clever thing I have come up with Python by far. The
        # range(4) produces values from 0 to 3 (inclusive). Then, I just add it
        # to the double of the member id, which turns out is the first id of the
        # left joint since we are using 0-based indexing.
        slice = [self.id * 2 + index for index in range(4)]

        # Numpy has a built-in function for slicing matrices.
        return d[np.ix_(slice)]

    # Printed for the u matrix just denotes the subscript and prints the raw
    # matrix.
    def print_u(self, d: np.matrix):
        print(f"u_{self.id} =")
        print(self.u(d), end="\n\n")

    # Q is as simple as k * u. Not much to say here.
    def Q(self, d: np.matrix):
        u = self.u(d)
        return self.k() * u

    # Before Q can be globally manipulated, it needs to be padded. It uses the
    # same padding as k_padded but with some simplification since its a column
    # vector.
    def Q_padded(self, d: np.matrix, max_id: int):
        top_padding = 2 * self.id
        bottom_padding = 2 * (max_id - self.id)

        return np.pad(
            self.Q(d),
            pad_width=(
                (top_padding, bottom_padding),
                (0, 0),
            ),
        )

    # Same deal. Prints Q with a label of the correct subscript.
    def print_Q(self, d: np.matrix):
        print(f"Q_{self.id} =")
        print(self.Q(d), end="\n\n")

    # Renders the intermediate pipe (|) symbols between the joint along with
    # the id, x position, and length of the member.
    def render(self):
        self.left.render()

        print(" |")
        print(f" | #{self.id} x={self.x} L={self.L}")
        print(" |")

    # The k matrix is printed for each member with the correct label.
    def print_k(self):
        print(f"k_{self.id} =")
        print(self.k(), end="\n\n")


# The beam is a collection of members.
class Beam:
    # The beam accepts material properties and a list of supports and external
    # forces and moments.
    def __init__(self, E, I, L, supports: list[Support], externals: list[External]):

        # Simply store the values.
        self.E = E
        self.I = I
        self.L = L

        self.supports = supports
        self.externals = externals

        # Break points is clever because I found out Python has sets much
        # like Set<number>() in TypeScript. This lets me collect all candidates
        # for where I can split the beam into members. The points of interest
        # include the start and end of the beam as a default in the off case
        # the beam has literally no supports or externals.
        break_points_pool = {0, self.L}

        # Loop though all supports, regardless of type, and add it to the set.
        # And since sets in Python work much like Set() from TypeScript, any
        # duplicates will be ignored. So we end up with a unique set of points.
        for support in self.supports:
            break_points_pool.add(support.x)

        # Same deal with externals.
        for external in self.externals:
            break_points_pool.add(external.x)

        # The points will likely be out of order so I sort them into a proper
        # list.
        self.break_points = sorted(list(break_points_pool))

        # This is the juicy function that's tricky to get right. Thankfully,
        # 0-based indexing makes it trivial.
        # The first member id is 0.
        member_id = 0

        # An empty list to hold the members.
        self.members: list[Member] = []

        # Loop through the break points which represent the position of the
        # left side of the members (thus, by extension, the left joints).
        for x in self.break_points:

            # Store this info since I will use it multiple times.
            is_first = member_id == 0
            is_last = member_id == len(self.break_points) - 1

            # Filter supports and externals that act on the left side of this
            # beam.
            supports = [support for support in self.supports if support.x == x]
            externals = [external for external in self.externals if external.x == x]

            # It makes no physical sense to have more than 1 support on the
            # same point. So I record the length for future consideration.
            supports_length = len(supports)

            # Throw an error (or as it's called in Python, raise and error) if
            # there are more than 1 support.
            if supports_length > 1:
                raise ValueError(f"More than 1 support found at x={x}")

            # Create the left joint with the appropriate support if available
            # or create a nominal NONE type joint.
            left = Joint(
                supports[0] if supports_length == 1 else Support(x, SupportType.NONE),
                externals,
            )

            # The right hand side is a dummy awaiting to be replaced by the
            # left hand side of the next member.
            right = Joint(Support(x, SupportType.NONE), [])

            # If this is the last index, we are actually dealing with a member
            # beyond the length of the beam. In other words, the left side of
            # this member would at the very right end of the whole beam. So we
            # never create a member if this is the last index.
            if not is_last:

                # Get the next break point to get the length of this member.
                x_next = self.break_points[member_id + 1]

                # Create the segment with the correct values.
                segment = Member(member_id, x, self.E, self.I, x_next - x, left, right)

            # If this is anything but the first member, there exists another
            # member to the left of this one which is awaiting a right side
            # joint. So, I donate the left side of this member to the right
            # side of the previous member.
            if not is_first:
                last_member = self.members[-1]
                last_member.right = left

            if not is_last:
                # Throw it into the list.
                self.members.append(segment)

            # Increment the member id.
            member_id += 1

        self.free_indices: list[int] = []
        length = len(self.members)

        for member in self.members:
            if member.left.free_displacement:
                self.free_indices.append(member.id * 2)

            if member.left.free_rotation:
                self.free_indices.append(member.id * 2 + 1)

        if self.members[-1].right.free_displacement:
            self.free_indices.append(length * 2)

        if self.members[-1].right.free_rotation:
            self.free_indices.append(length * 2 + 1)

        self.free_indices = self.free_indices

    # The S, by default, is the sum of all the padded stiffness matrices.
    def S_padded(self):
        max_id = len(self.members) - 1
        return sum([member.k_padded(max_id) for member in self.members])

    def S(self):
        S_padded = self.S_padded()
        return S_padded[np.ix_(self.free_indices, self.free_indices)]

    def P_padded(self):
        rows: list[list[float]] = []

        for member in self.members:
            rows.append([member.left.external_force])
            rows.append([member.left.external_moment])

        rows.append([self.members[-1].right.external_force])
        rows.append([self.members[-1].right.external_moment])

        return np.matrix(rows)

    def P(self):
        P_padded = self.P_padded()
        return P_padded[np.ix_(self.free_indices)]

    def d(self):
        return np.linalg.solve(self.S(), self.P())

    def d_padded(self):
        d = self.d()
        d_sorted = dict()

        index = 0
        for free_index in self.free_indices:
            d_sorted[free_index] = d[index].item()
            index += 1

        d_padded = []

        for index in range(len(self.members) * 2 + 2):
            d_padded.append([d_sorted[index] if index in d_sorted else 0])

        return np.matrix(d_padded)

    def R_padded(self):
        d_padded = self.d_padded()

        return sum(
            [
                member.Q_padded(d_padded, len(self.members) - 1)
                for member in self.members
            ]
        )

    def solve(self) -> np.matrix:
        for member in self.members:
            member.print_k()

        for member in self.members:
            member.left.print_loads(member.id * 2)

        self.members[-1].right.print_loads(2 * len(self.members) - 1)
        print()

        print(f"S =\n{self.S()}\n\n")
        print(f"P =\n{self.P()}\n\n")
        print(f"d =\n{self.d()}\n\n")

        d_padded = self.d_padded()

        for member in self.members:
            member.print_u(d_padded)

        for member in self.members:
            member.print_Q(d_padded)

        R_padded = self.R_padded()

        for index in range(len(self.members) * 2 + 2):
            print(f"R_{index} = {R_padded[index].item()}")

        print()

    def render(self):
        for member in self.members:
            member.render()

        self.members[-1].right.render()
        print()


lecture_example_1 = Beam(
    200 * 10**6,
    700 * 10**-6,
    8 + 4,
    [
        Support(0, SupportType.FIXED),
        Support(8, SupportType.ROLLER),
    ],
    [
        External(8 + 4, ExternalType.FORCE, -85),
    ],
)
lecture_example_1.render()
lecture_example_1.solve()

# beam = Beam(
#     150 * 10**6,
#     500 * 10**-6,
#     20,
#     [
#         Support(20 * (0 / 5), SupportType.FIXED),
#         Support(20 * (1 / 5), SupportType.ROLLER),
#         Support(20 * (3 / 5), SupportType.ROLLER),
#         Support(20 * (4 / 5), SupportType.ROLLER),
#     ],
#     [
#         External(20 * (1 / 5), ExternalType.MOMENT, 100),
#         External(20 * (2 / 5), ExternalType.FORCE, -350),
#         External(20 * (3 / 5), ExternalType.MOMENT, -100),
#         External(20 * (5 / 5), ExternalType.FORCE, -200),
#     ],
# )

# beam.render()
# beam.solve()
