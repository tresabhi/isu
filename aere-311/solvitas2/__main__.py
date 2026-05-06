from hoppers import *
from couplers import *
from registry import *
from symbols import *
from units import *
from hopper import *
from utils import *

Hopper.units = anderson_units
# Hopper.verbose = True

air = {
    gamma: 7 / 5,
    R: 287.05 * ur("J / (kg * K)"),
}

s = Isentropic(
    {
        **air,
        T0: 440.0,
        p0: 10 * ur("atm"),
        p1: 1 * ur("atm"),
    }
).solve()
