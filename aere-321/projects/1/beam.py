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


class Beam:
    def __init__(self, E, I, L, supports: list[Support], externals: list[External]):
        self.E = E
        self.I = I
        self.L = L

        self.supports = supports
        self.externals = externals

    def break_points(self):
        points = {0, self.L}

        for support in self.supports:
            points.add(support.x)

        for external in self.externals:
            points.add(external.x)

        return sorted(list(points))

    def segment_members(self):
        break_points = self.break_points()
        member_id = 0
        members: list[Member] = []

        for x in break_points:
            is_first = member_id == 0
            is_last = member_id == len(break_points) - 1

            supports = [support for support in self.supports if support.x == x]
            externals = [external for external in self.externals if external.x == x]

            supports_length = len(supports)

            if supports_length > 1:
                raise ValueError("More than 1 support found")

            left = Joint(
                supports[0] if supports_length == 1 else Support(x, SupportType.NONE),
                externals,
            )
            right = Joint(Support(x, SupportType.NONE), [])

            if not is_last:
                x_next = break_points[member_id + 1]
                segment = Member(member_id, x, self.E, self.I, x_next - x, left, right)

            if not is_first:
                last_member = members[-1]
                last_member.right = left

            if not is_last:
                members.append(segment)

            member_id += 1

        return members

    def S(self, members: list[Member]):
        max_id = members[-1].id
        return sum([member.k_padded(max_id) for member in members])

    def P(self, members: list[Member]):
        rows: list[list[float]] = []

        for member in members:
            rows.append([member.left.external_force])
            rows.append([member.left.external_moment])

        rows.append([members[-1].right.external_force])
        rows.append([members[-1].right.external_moment])

        return np.matrix(rows)

    def free_indices(self, members: list[Member]):
        ids: list[int] = []
        length = len(members)

        for member in members:
            if member.left.free_displacement:
                ids.append(member.id * 2)

            if member.left.free_rotation:
                ids.append(member.id * 2 + 1)

        if members[-1].right.free_displacement:
            ids.append(length * 2)

        if members[-1].right.free_rotation:
            ids.append(length * 2 + 1)

        return ids

    def print_all(self) -> np.matrix:
        members = self.segment_members()

        for member in members:
            member.print_k()

        for member in members:
            member.left.print_loads(member.id * 2)

        members[-1].right.print_loads(members[-1].id * 2 + 1)
        print()

        free_indices = self.free_indices(members)

        S = self.S(members)

        print(f"S_untrimmed =")
        print(S, end="\n\n")

        S = S[np.ix_(free_indices, free_indices)]

        print(f"S =")
        print(S, end="\n\n")

        P = self.P(members)

        print("P_untrimmed =")
        print(P, end="\n\n")

        P = P[np.ix_(free_indices)]

        print("P =")
        print(P, end="\n\n")

        d = np.linalg.solve(S, P)

        print("d =")
        print(d, end="\n\n")

        d_sorted = dict()

        index = 0
        for free_index in free_indices:
            d_sorted[free_index] = d[index].item()
            index += 1

        d_untrimmed = []

        for index in range(members[-1].id * 2 + 4):
            d_untrimmed.append([d_sorted[index] if index in d_sorted else 0])

        d_untrimmed = np.matrix(d_untrimmed)

        print("d_untrimmed =")
        print(d_untrimmed, end="\n\n")

        for member in members:
            member.print_u(d_untrimmed)

        for member in members:
            member.print_Q(d_untrimmed)

        R_untrimmed = sum(
            [member.Q_padded(d_untrimmed, members[-1].id) for member in members]
        )

        for index in range(members[-1].id * 2 + 4):
            if index in free_indices:
                continue

            print(f"R_{index} = {R_untrimmed[index].item()}")

    def render(self):
        members = self.segment_members()

        for member in members:
            member.render()

        members[-1].right.render()
        print()


# lecture_beam = Beam(
#     200 * 10**6,
#     700 * 10**-6,
#     8 + 4,
#     [
#         Support(0, SupportType.FIXED),
#         Support(8, SupportType.ROLLER),
#     ],
#     [
#         External(8 + 4, ExternalType.FORCE, -85),
#     ],
# )
# lecture_beam.render()
# lecture_beam.print_all()

beam = Beam(
    150 * 10**6,
    500 * 10**-6,
    20,
    [
        Support(20 * (0 / 5), SupportType.FIXED),
        Support(20 * (1 / 5), SupportType.ROLLER),
        Support(20 * (3 / 5), SupportType.ROLLER),
        Support(20 * (4 / 5), SupportType.ROLLER),
    ],
    [
        External(20 * (1 / 5), ExternalType.MOMENT, 100),
        External(20 * (2 / 5), ExternalType.FORCE, -350),
        External(20 * (3 / 5), ExternalType.MOMENT, -100),
        External(20 * (5 / 5), ExternalType.FORCE, -200),
    ],
)

beam.render()
beam.print_all
()
