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

s = Bernoulli(
    {
        **air,
        #
        p1: 0.61 * ur("atm"),
        rho1: 0.819 * ur("kg / m^3"),
        u1: 300 * ur("m / s"),
        p2: 0.550 * ur("atm"),
    }
).solve()
