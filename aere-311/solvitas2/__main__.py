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

s = Adiabatic(
    {
        **air,
        T0: 950 * ur("K"),
        T2: 600 * ur("K"),
    }
).solve()
