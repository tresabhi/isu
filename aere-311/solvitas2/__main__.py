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

s = WeakObliqueShock(
    {
        **air,
        #
        theta: 30.2 * ur("deg"),
        M1: 3.5,
        p1: 0.5 * ur("atm"),
    }
).solve()

NormalShock(
    {
        **air,
        **to_state_space(s, 2, 1),
    }
).solve()
