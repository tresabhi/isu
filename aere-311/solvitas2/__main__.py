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

s = NormalShock(
    {
        **air,
        T1: 288 * ur("K"),
        p1: 1 * ur("atm"),
        # T2: 698 * ur("K"),
        p2: 8.656 * ur("atm"),
    }
).solve()
