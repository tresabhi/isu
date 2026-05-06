from hoppers import *
from couplers import *
from registry import *
from symbols import *
from units import *
from hopper import *
from utils import *

Hopper.units = anderson_units
# Hopper.units = imperial_units
# Hopper.verbose = True

air = {
    gamma: 7 / 5,
    R: 287.05 * ur("J / (kg * K)"),
}

s = Isentropic(
    {
        **air,
        #
        T1: 300 * ur("K"),
        p1: 1.2 * ur("atm"),
        u1: 305.0 * ur("m/s"),
    }
).solve()
