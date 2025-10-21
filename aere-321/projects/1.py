import pint
import numpy as np
from enum import Enum


class SupportType(Enum):
    FREE = 1
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
    def __init__(self, x: float, support: Support, externals: list[External]):
        self.x = x
        self.support = support
        self.externals = externals

        self.fixed_displacement = supports.type != SupportType.FREE
        self.fixed_rotation = support.type == SupportType.FIXED

    def __str__(self):
        return (
            f"Joint(x={self.x}, supports={self.supports}, externals={self.externals})"
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

        self.k = ((E * I) / L**3) * np.matrix(
            [
                [12, 6 * L, -12, 6 * L],
                [6 * L, 4 * L * L, -6 * L, 2 * L * L],
                [-12, -6 * L, 12, -6 * L],
                [6 * L, 2 * L * L, -6 * L, 4 * L * L],
            ]
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
        members = []
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
                x,
                supports[0] if supports_length == 1 else Support(x, SupportType.FREE),
                externals,
            )
            right = Joint(x, [], [])

            if not is_last:
                x_next = break_points[member_id]
                L = x_next - x
                segment = Member(member_id, x, E, I, L, left, right)

            if not is_first:
                last_member = members[-1]
                last_member.right = left

            if not is_last:
                members.append(segment)

            member_id += 1

        return members

    def solve(self):
        segments = self.segment_members()


ur = pint.UnitRegistry()

# stripping units for now to improve performance
E = (200 * 10**6 * ur.kN / ur.m**2).to_base_units().magnitude
I = (700 * 10**-6 * ur.m**4).to_base_units().magnitude
L = 8 + 4

supports = [
    Support(0, SupportType.FIXED),
    Support(8, SupportType.ROLLER),
]
externals = [External(8 + 4, ExternalType.FORCE, -85 * 1000)]
beam = Beam(E, I, L, supports, externals)

print(beam.segment_members())
