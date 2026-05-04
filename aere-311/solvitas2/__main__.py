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

diamond_wedge(
    {
        **air,
        epsilon: 10 * ur("deg"),
        alpha: 15 * ur("deg"),
        M1: 3.150,
    }
)
