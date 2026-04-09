import pint
import math
import sympy
import numpy as np
from scipy.optimize import brentq

ur = pint.UnitRegistry()

pe = 101 * ur.kPa
Tt = 300 * ur.K
Rt = 10 * ur.mm

gamma = 1.4

nozzle = []

with open("nozzle.dat") as file:
    for line in file.readlines():
        [z_Rt, r_Rt] = [float(cell) for cell in line.strip().split(" ")]

        r = r_Rt * Rt
        z = z_Rt * Rt

        nozzle.append((z, r))


re = nozzle[-1][1]
rt = Rt

print(f"re = {re}")
print(f"rt = {rt}")
print()

Ae = math.pi * re**2
At = math.pi * rt**2


def solve(pt):
    pe_pt = pe / pt
    Ae_At = Ae / At

    # def f(M):
    #     return Ae_At - area_mach(M)

    Me_1 = math.sqrt(
        (-1 / (gamma - 1))
        + (
            1 / ((gamma - 1) ** 2)
            + (2 / (gamma - 1))
            * (
                ((2 / (gamma + 1)) ** ((gamma + 1) / (gamma - 1)))
                / ((Ae_At * pe_pt) ** 2)
            )
        )
        ** (1 / 2)
    )
    pt_pe_1 = (1 + ((gamma - 1) / 2) * Me_1**2) ** (gamma / (gamma - 1))

    # M = sympy.Symbol("M")

    # eq = Ae_At - (1 / M) * ((2 / (gamma + 1)) * (1 + (gamma - 1) / 2 * M**2)) ** (
    #     (gamma + 1) / (2 * (gamma - 1))
    # )

    # M_sub = brentq(f, 1e-6, 0.999)
    # M_sup = brentq(f, 1.001, 10)

    print(f"pt = {pt}")
    print(f"Ae/At = {Ae_At}")
    print(f"Me (1st critical) = {Me_1}")
    # print(f"M_sub = {M_sub}")
    # print(f"M_sup = {M_sup}")
    print(f"pt/pe (1st critical) = {pt_pe_1}")
    print()


solve(1000 * ur.kPa)
solve(400 * ur.kPa)
