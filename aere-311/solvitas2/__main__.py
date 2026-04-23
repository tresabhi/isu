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

NormalShockNozzle(
    [
        {
            **air,
            p0: 1 * ur("atm"),
        },
        {**air},
        {**air},
        {
            **air,
            Ae_At: 1.53,
        },
    ],
    [
        {},
        {},
        {},
        {
            pe: 0.525 * ur("atm"),
        },
    ],
    [
        {A_At: 1.204},
        {},
        {},
        {},
    ],
)
