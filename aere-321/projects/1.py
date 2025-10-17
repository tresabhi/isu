import pint
import numpy as np
from enum import Enum


class SupportType(Enum):
    FIXED = 1
    PINNED = 2
    ROLLER = 3


class Support:
    def __init__(self, type, x):
        self.type = type
        self.x = x


class ExternalType(Enum):
    FORCE = 1
    MOMENT = 2


class External:
    def __init__(self, type, x, value):
        self.type = type
        self.x = x
        self.value = value


class Segment:

    def __init__(self, E: float, I: float, L: float):
        self.E = E
        self.I = I
        self.L = L

        self.k = ((E * I) / L**3) * np.matrix(
            [
                [12, 6 * L, -12, 6 * L],
                [6 * L, 4 * L * L, -6 * L, 2 * L * L],
                [-12, -6 * L, 12, -6 * L],
                [6 * L, 2 * L * L, -6 * L, 4 * L * L],
            ]
        )


class Beam:
    def __init__(self, E, I, L, supports: list[Support], externals: list[External]):
        self.E = E
        self.I = I
        self.L = L
        self.supports = supports
        self.externals = externals


ur = pint.UnitRegistry()

# stripping units for now to improve performance
E = (200 * 10**6 * ur.kN / ur.m**2).to_base_units().magnitude
I = (700 * 10**-6 * ur.m**4).to_base_units().magnitude
L = 8 + 4

supports = [
    Support(SupportType.FIXED, 0),
    Support(SupportType.ROLLER, 8),
]
externals = [
    External(ExternalType.FORCE, 8 + 4, (-85 * ur.kN).to_base_units().magnitude)
]
beam = Beam(E, I, L, supports, externals)
