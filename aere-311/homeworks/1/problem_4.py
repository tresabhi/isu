import pint
from tabulate import tabulate
import math

ur = pint.UnitRegistry()

T_1 = 288 * ur.K
p_1 = 1 * ur.atm
T_2 = 698 * ur.K
p_2 = 8.656 * ur.atm

R = 1716.46 * ur.ft * ur.lbf / (ur.slug * ur.rankine)
gamma = 1.4

c_v = R / (gamma - 1)
c_p = R + c_v

h_1 = c_p * T_1
h_2 = c_p * T_2
e_1 = c_v * T_1
e_2 = c_v * T_2

delta_h = h_2 - h_1
delta_e = e_2 - e_1
delta_s = c_p * math.log(T_2 / T_1) - R * math.log(p_2 / p_1)

print(
    tabulate(
        [
            ["delta_h / 1e5", delta_h.to(ur.J / ur.kg) / 1e5],
            ["delta_e / 1e5", delta_e.to(ur.J / ur.kg) / 1e5],
            ["delta_s", delta_s.to(ur.J / (ur.kg * ur.K))],
        ]
    )
)
