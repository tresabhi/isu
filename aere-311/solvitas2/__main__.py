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

s1 = LinearizedFlatPlate(
    {
        **air,
        alpha: 30 * ur("deg"),
        M_inf: 2.600,
    }
).solve()

true_p2_p_inf = 0.0725
true_p3_p_inf = 5.687

error_p2_p_inf = abs(s1[p2_p_inf] - true_p2_p_inf) / true_p2_p_inf
error_p3_p_inf = abs(s1[p3_p_inf] - true_p3_p_inf) / true_p3_p_inf

error_p2_p_inf *= 100
error_p3_p_inf *= 100

print(f"p2_p_inf error: {error_p2_p_inf}%")
print(f"p3_p_inf error: {error_p3_p_inf}%")
