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

s = diamond_wedge(
    {
        **air,
        epsilon: 10 * ur("deg"),
        alpha: 15 * ur("deg"),
        M1: 3.150,
    }
)

true_cl = 0.418
true_cd = 0.169

error_cl = (s[Cl] - true_cl) / true_cl
error_cd = (s[Cd] - true_cd) / true_cd

error_cl *= 100
error_cd *= 100

error_cl = abs(error_cl)
error_cd = abs(error_cd)

print(f"Cl error = {error_cl}%")
print(f"Cd error = {error_cd}%")
