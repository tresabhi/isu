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

PerfectlyExpandedSubsonicNozzle(
    {
        **air,
        A_At: 1.53,
        p0: 1 * ur("atm"),
    }
)

PerfectlyExpandedSupersonicNozzle(
    {
        **air,
        A_At: 1.53,
        p0: 1 * ur("atm"),
    }
)

NormalShock(
    {
        **air,
        T1: 288 * ur("K"),
        p1: 1 * ur("atm"),
        M1: 2,
        # Ae_At: 4,
        # p01: 1 * ur("atm"),
        # pe: 0.525 * ur("atm"),
    }
)
