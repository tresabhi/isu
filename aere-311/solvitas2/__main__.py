from hoppers import *
from couplers import *
from registry import *
from symbols import *
from units import *
from hopper import *
from utils import *
from shakers import *

Hopper.units = anderson_units
# Hopper.verbose = True

air = {
    gamma: 7 / 5,
    R: 287.05 * ur("J / (kg * K)"),
}

NormalShockNozzleShaker(
    [
        {
            **air,
            p0: 1 * ur("atm"),
        },
        {
            **air,
        },
        {
            **air,
        },
        {
            **air,
            Ae_At1: 1.53,
            p: 0.75 * ur("atm"),
        },
    ],
)
