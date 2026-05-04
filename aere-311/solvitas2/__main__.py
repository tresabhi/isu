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
        alpha: 5 * ur("deg"),
        M_inf: 2.600,
    }
).solve()

true_cl = 0.148
true_cd = 0.0129

e_cl = abs(s1[cl] - true_cl) / true_cl
e_cd = abs(s1[cd] - true_cd) / true_cd

e_cl *= 100
e_cd *= 100

print(f"cl error = {e_cl}%")
print(f"cd error = {e_cd}%")
