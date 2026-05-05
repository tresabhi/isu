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

s = LinearizedFlatPlate(
    {
        **air,
        alpha: 5 * ur("deg"),
        M_inf: 2.600,
    }
).solve()

rounded_cl = 0.145
rounded_cd = 0.0127
true_cl = 0.148
true_cd = 0.0129

percent_error_cl = ((true_cl - rounded_cl) / (true_cl)) * 100
percent_error_cd = ((true_cd - rounded_cd) / (true_cd)) * 100

print("percent error in cl:", percent_error_cl)
print("percent error in cd:", percent_error_cd)
