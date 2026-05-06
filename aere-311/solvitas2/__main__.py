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

s2 = ExpansionWave(
    {
        **air,
        #
        theta: 4 * ur("deg"),
        M1: 2.6,
    }
).solve()

s3 = WeakObliqueShock(
    {
        **air,
        #
        theta: 4 * ur("deg"),
        M1: 2.6,
    }
).solve()
