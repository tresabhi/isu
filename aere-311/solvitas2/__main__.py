from hoppers import *
from couplers import *
from registry import *
from symbols import *
from units import *
from hopper import *
from utils import *

Hopper.units = imperial_units
# Hopper.verbose = True

air = {
    gamma: 7 / 5,
    R: 287.05 * ur("J / (kg * K)"),
}

s = Isentropic(
    {
        **air,
        T01: 982 * ur.rankine,
        p01: 7.8 * ur.atm,
    }
).solve()
