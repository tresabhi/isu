from hoppers import *
from couplers import *
from registry import *
from symbols import *
from units import *
from hopper import *

Hopper.units = anderson_units
# Hopper.verbose = True

air = {
    gamma: 7 / 5,
    R: 287.05 * ur("J / (kg * K)"),
}

Rayleigh(
    {
        **air,
        M1: 1.75,
        T01: 650 * ur("K"),
        p01: 1 * ur("atm"),
        delta_T0: 110 * ur("K"),
    }
)

# PerfectlyExpandedSubsonicNozzle(
#     {
#         **air,
#         A_At: 1.53,
#         p0: 1 * ur("atm"),
#     }
# )

# PerfectlyExpandedSupersonicNozzle(
#     {
#         **air,
#         A_At: 1.53,
#         p0: 1 * ur("atm"),
#     }
# )

# NormalShockNozzle(
#     [
#         {
#             "invariants": {
#                 **air,
#                 p0: 1 * ur("atm"),
#             },
#             "variant": A_At,
#         },
#         {
#             "invariants": air,
#         },
#         {
#             "invariants": air,
#         },
#         {
#             "invariants": {
#                 **air,
#                 Ae_At1: 4,
#             },
#             "variant": As_At1,
#             "target": p,
#         },
#     ],
#     (1, 4),
#     0.525 * ur("atm"),
# ).solve()
