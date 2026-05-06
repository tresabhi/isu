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

WeakObliqueShock(
    {
        **air,
        #
        theta: 22.5 * ur("deg"),
        M1: 2.5,
        p1: 2 * ur("atm"),
        T1: 280 * ur("K"),
    }
).solve()
