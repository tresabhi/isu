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

SubsonicNozzle(
    {
        **air,
        #
        p0: 5 * ur("atm"),
        T0: 520 * ur("rankine"),
        At: 4.100 * ur("in^2"),
        A_At: 2.193,
    }
).solve()
