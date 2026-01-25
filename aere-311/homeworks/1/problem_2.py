import pint
from tabulate import tabulate

ur = pint.UnitRegistry()

R = 1716.46 * ur.ft * ur.lbf / (ur.slug * ur.rankine)
T = 936 * ur.rankine
p = 7.8 * ur.atm

gamma = 1.4

c_v = R / (gamma - 1)
c_p = R + c_v
e = c_v * T
h = c_p * T

print(
    tabulate(
        [
            ["c_p", c_p.to(ur.ft * ur.lbf / (ur.slug * ur.rankine))],
            ["c_v", c_v.to(ur.ft * ur.lbf / (ur.slug * ur.rankine))],
            ["e", e.to(ur.ft * ur.lbf / ur.slug)],  # WRONG
            ["h", h.to(ur.ft * ur.lbf / ur.slug)],  # WRONG
        ]
    )
)
