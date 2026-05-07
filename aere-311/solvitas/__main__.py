from hoppers import *
from couplers import *
from registry import *
from symbols import *
from units import *
from hopper import *
from utils import *
from shakers import *

Hopper.units = imperial_units
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
#             Ae_At1: 1.53,
#             As_At1: x,
#             p: y,
#         },
#     ],
#     (1, 2),
#     0.75 * ur("atm"),
# ).solve()

s = SupersonicNozzle(
    {
        **air,
        #
        M: 3.100,
        m_dot: 1 * ur("slug / s"),
        p: 2116 * ur("lbf / ft^2"),
        T: 519 * ur("rankine"),
    }
).solve()

NormalShock(
    {
        **air,
        #
        **to_state_space(s, "generic", 1),
    }
).solve()
