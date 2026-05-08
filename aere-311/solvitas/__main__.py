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

# NormalShockNozzle(
#     [
#         {
#             **air,
#             p0: 1 * ur("atm"),
#             A_At: x,
#         },
#         {
#             **air,
#         },
#         {
#             **air,
#         },
#         {
#             **air,
#             Ae_At1: 4,
#             As_At1: x,
#             p: y,
#         },
#     ],
#     (1, 8),
#     0.525 * ur("atm"),
# ).solve()


SubsonicRayleigh(
    {
        **air,
        #
        p01: 1 * ur("atm"),
        T01: 294 * ur("K"),
        delta_T0: 500 * ur("K"),
        M2: 1,
    }
).solve()
