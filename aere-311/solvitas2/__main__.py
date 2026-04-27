import time
from hoppers import *
from couplers import *
from registry import *
from symbols import *
from units import *
from hopper import *

Hopper.units = anderson_units

air = {
    gamma: 7 / 5,
    R: 287.05 * ur("J / (kg * K)"),
}

# SubsonicRayleigh(
#     {
#         **air,
#         u1: 72 * ur("m / s"),
#         T1: 323 * ur("K"),
#         Q: 10**6 * ur("J / kg"),
#     }
# )

t0 = time.monotonic()

NormalShockNozzle(
    [
        {
            "invariants": {
                **air,
                p0: 1 * ur("atm"),
            },
            "variant": A_At,
        },
        {
            "invariants": air,
        },
        {
            "invariants": air,
        },
        {
            "invariants": {
                **air,
                Ae_At1: 1.53,
            },
            "variant": As_At1,
            "target": p,
        },
    ],
    (1, 1.53),
    0.75 * ur("atm"),
).solve()

t1 = time.monotonic()

print(f"{t1 - t0}s")
