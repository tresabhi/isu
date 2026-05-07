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

s1 = SubsonicNozzle(
    {
        **air,
        #
        A: 2.8,
        M: 0.32,
    }
).solve()

s2 = SubsonicNozzle(
    {
        **air,
        #
        A: 1.311,
        M: 0.32,
    }
).solve()

_At = s2[At]
_A = s1[A]
_A_At = _A / _At

print(_A, _At)

SubsonicNozzle(
    {
        **air,
        A_At: 2.8 / 1.311,
    }
).solve()
