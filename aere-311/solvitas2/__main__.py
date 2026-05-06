from hoppers import *
from couplers import *
from registry import *
from symbols import *
from units import *
from hopper import *
from utils import *

# Hopper.units = ephemeral_units
Hopper.units = anderson_units
# Hopper.verbose = True

air = {
    gamma: 7 / 5,
    R: 287.05 * ur("J / (kg * K)"),
}

NormalShock(
    {
        **air,
        #
        p02: 1.245 * ur("atm"),
        p1: 0.1 * ur("atm"),
    }
).solve()

# ObliqueShock(
#     {
#         **air,
#         #
#         beta_weak: 30 * ur.deg,
#         M1: 4,
#         p1: 2.65e4 * ur.N / ur.m**2,
#         T1: 223.3 * ur.K,
#     }
# ).solve()
