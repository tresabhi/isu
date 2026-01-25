import pint
from tabulate import tabulate
import math

ur = pint.UnitRegistry()


T_0 = 440.0 * ur.K
p_0 = 10 * ur.atm
p = 1 * ur.atm

R = 1716.46 * ur.ft * ur.lbf / (ur.slug * ur.rankine)
gamma = 1.4

T_1 = T_0
p_1 = p_0
p_2 = p

rho_1 = p_1 / (R * T_1)
T_2 = T_1 * (p_2 / p_1) ** ((gamma - 1) / gamma)
rho_2 = rho_1 * (p_2 / p_1) ** (1 / gamma)

print(
    tabulate(
        [
            ["T_2", T_2.to(ur.K)],
            ["rho_2", rho_2.to(ur.kg / ur.m**3)],
        ]
    )
)
