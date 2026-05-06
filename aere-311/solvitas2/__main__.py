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

Isentropic(
    {
        **air,
        #
        M1: 36,
        T1: 350 * ur("K"),
    }
).solve()
