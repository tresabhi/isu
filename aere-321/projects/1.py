import numpy as np
from enum import Enum


class SupportType(Enum):
    NONE = 1
    FIXED = 2
    PINNED = 3
    ROLLER = 4

    def __str__(self):
        return self.name


class Support:
    def __init__(self, x: float, type: SupportType):
        self.type = type
        self.x = x

    def __str__(self):
        return f"Support(x={self.x}, type={self.type})"

    def __repr__(self):
        return self.__str__()


class ExternalType(Enum):
    FORCE = 1
    MOMENT = 2

    def __str__(self):
        return self.name


class External:
    def __init__(self, x: float, type: ExternalType, value: float):
        self.x = x
        self.type = type
        self.value = value

    def __str__(self):
        return f"External(x={self.x}, type={self.type}, value={self.value})"

    def __repr__(self):
        return self.__str__()


class Joint:
    def __init__(self, support: Support, externals: list[External]):
        self.support = support

        external_forces = [
            external for external in externals if external.type == ExternalType.FORCE
        ]
        external_moments = [
            external for external in externals if external.type == ExternalType.MOMENT
        ]

        self.external_force = sum([external.value for external in external_forces])
        self.external_moment = sum([external.value for external in external_moments])

        self.free_displacement = support.type == SupportType.NONE
        self.free_rotation = support.type != SupportType.FIXED

    def __str__(self):
        return f"Joint(force={self.external_force}, moment={self.external_moment})"


class Member:

    def __init__(
        self, id: int, x: float, E: float, I: float, L: float, left: Joint, right: Joint
    ):
        self.id = id
        self.x = x

        self.E = E
        self.I = I
        self.L = L

        self.left = left
        self.right = right

    def k(self):
        E = self.E
        I = self.I
        L = self.L

        return ((E * I) / L**3) * np.matrix(
            [
                [12, 6 * L, -12, 6 * L],
                [6 * L, 4 * L * L, -6 * L, 2 * L * L],
                [-12, -6 * L, 12, -6 * L],
                [6 * L, 2 * L * L, -6 * L, 4 * L * L],
            ]
        )

    def k_padded(self, max_id: int):
        top_left_padding = 2 * (self.id - 1)
        bottom_right_padding = 2 * (max_id - self.id)

        return np.pad(
            self.k(),
            pad_width=(
                (top_left_padding, bottom_right_padding),
                (top_left_padding, bottom_right_padding),
            ),
        )

    def __str__(self):
        return f"Member#{self.id}(x={self.x}, L={self.L}, left={self.left}, right={self.right})"

    def __repr__(self):
        return self.__str__()


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
        member_id = 1
        members: list[Member] = []
        length = len(break_points)

        for x in break_points:
            is_first = member_id == 1
            is_last = member_id == length

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
                x_next = break_points[member_id]
                L = x_next - x
                segment = Member(member_id, x, self.E, self.I, L, left, right)

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
                ids.append((member.id - 1) * 2)

            if member.left.free_rotation:
                ids.append((member.id - 1) * 2 + 1)

        if members[-1].right.free_displacement:
            ids.append(length * 2)

        if members[-1].right.free_rotation:
            ids.append(length * 2 + 1)

        return ids

    def solve(self):
        members = self.segment_members()
        indices = self.free_indices(members)

        S = self.S(members)[np.ix_(indices, indices)]
        P = self.P(members)[np.ix_(indices)]

        return np.linalg.solve(S, P)


supports = [
    Support(0, SupportType.FIXED),
    Support(8, SupportType.ROLLER),
]
externals = [External(8 + 4, ExternalType.FORCE, -85)]
beam = Beam(
    200 * 10**6,  # kN/m^2
    700 * 10**-6,  # m^4
    8 + 4,  # m
    supports,
    externals,
)

members = beam.segment_members()

print(beam.solve())
