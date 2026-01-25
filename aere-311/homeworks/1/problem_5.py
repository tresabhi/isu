import pint
from tabulate import tabulate
import math

ur = pint.UnitRegistry()

T_inf = 245 * ur.K
p_inf = 4.35e4 * ur.N / ur.m**2
p = 3.600e4 * ur.N / ur.m**2

R = 1716.46 * ur.ft * ur.lbf / (ur.slug * ur.rankine)
gamma = 1.4

p_1 = p_inf
T_1 = T_inf
p_2 = p

rho_1 = p_1 / (R * T_1)
rho_2 = rho_1 * (p_2 / p_1) ** (1 / gamma)

print(
    tabulate(
        [
            ["rho_2", rho_2.to(ur.kg / ur.m**3)],
        ]
    )
)
