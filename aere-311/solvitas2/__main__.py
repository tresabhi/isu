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
        M1: 3,
        T1: 280 * ur("K"),
        p1: 3 * ur("atm"),
        theta: 30.6 * ur("deg"),
    }
).solve()

ExpansionWave(
    {
        **air,
        **to_state_space(s, 2, 1),
        theta: s[theta],
    }
).solve()
