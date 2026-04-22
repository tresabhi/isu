from hoppers import *
from registry import *
from symbols import *
from units import *

Hopper.units = anderson_units

air = {
    gamma: 7 / 5,
    R: 287.05 * ur("J / (kg * K)"),
}

nh = PerfectlyExpandedSubsonicNozzleHopper(
    {
        **air,
        A_At: 1.53,
        p0: 1 * ur("atm"),
    }
)
