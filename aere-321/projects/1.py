import numpy as np
from enum import Enum


class SupportType(Enum):
    NONE = 1
    FIXED = 2
    ROLLER = 3


class Support:
    def __init__(self, x: float, type: SupportType):
        self.type = type
        self.x = x


class ExternalType(Enum):
    FORCE = 1
    MOMENT = 2


class External:
    def __init__(self, x: float, type: ExternalType, value: float):
        self.x = x
        self.type = type
        self.value = value


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

    def render(self):
        icon = " |"

        if self.support.type == SupportType.FIXED:
            icon = "░░"
        elif self.support.type == SupportType.ROLLER:
            icon = "◯|"

        print(
            f"{icon} Joint {self.support.type} ↑ {self.external_force} ⭯ {self.external_moment}",
            end="\n",
        )


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

    def render(self):
        self.left.render()

        print(" |")
        print(f" | Member #{self.id} @ x={self.x} L={self.L}")
        print(" |")


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

    def solve(self) -> np.matrix:
        members = self.segment_members()
        indices = self.free_indices(members)

        S = self.S(members)[np.ix_(indices, indices)]
        P = self.P(members)[np.ix_(indices)]

        return np.linalg.solve(S, P)

    def print_and_solve(self):
        members = self.segment_members()
        indices = self.free_indices(members)
        solved = self.solve()
        max_id = (members[-1].id) * 2
        sorted = dict()

        i = 0
        for d in solved:
            sorted[indices[i]] = d.item()
            i += 1

        for id in range(max_id + 2):
            id_shifted = id + 1
            print(
                f"d_{id_shifted} = {sorted[id_shifted] if id_shifted in sorted else 0}"
            )

        print()

    def render(self):
        members = self.segment_members()

        for member in members:
            member.render()

        members[-1].right.render()
        print()


lecture_beam = Beam(
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
lecture_beam.render()
lecture_beam.print_and_solve()

project_beam = Beam(
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
project_beam.render()
project_beam.print_and_solve()
