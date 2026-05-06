from hoppers import *
from couplers import *
from registry import *
from symbols import *
from units import *
from hopper import *
from utils import *

Hopper.units = ephemeral_units
# Hopper.verbose = True

air = {
    gamma: 7 / 5,
    R: 287.05 * ur("J / (kg * K)"),
}

s = Isentropic(
    {
        **air,
        #
        M1: 0.82,
        M2: 0.78,
        p1: 1455.6 * ur("lbf/ft^2"),
        T1: 483.04 * ur("rankine"),
    }
).solve()
