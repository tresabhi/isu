import time
from hoppers import *
from couplers import *
from registry import *
from symbols import *
from units import *
from hopper import *

Hopper.units = anderson_units

air = {
    gamma: 7 / 5,
    R: 287.05 * ur("J / (kg * K)"),
}

PrandtlGlauertCriticalRule(
    {
        **air,
        M_cr: 1,
        M_inf: 0.84,
    }
).solve()
