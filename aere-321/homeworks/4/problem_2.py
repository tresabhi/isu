import pint
from math import sin, cos, atan2
import numpy as np

ur = pint.UnitRegistry()

N = ur.N
m = ur.m
kN = ur.kN
deg = ur.deg
mm = ur.mm
MPa = ur.MPa
Pa = ur.Pa

l = 200 * mm
w = 50 * mm

M = 2 * kN * m
theta = 60 * deg

M_y = M * sin(theta)
M_z = M * cos(theta)

v_bar = (l / 2 + l + w / 2) / 2
I_y = (1 / 12) * w * l**3 + (1 / 12) * l * w**3
I_z = (
    (1 / 12) * w * l**3
    + w * l * (l / 2 - v_bar) ** 2
    + (1 / 12) * l * w**3
    + l * w * (l - v_bar + w / 2) ** 2
)


sigma_x_B = -6 * MPa
sigma_x_G = 4 * MPa

M_B = sigma_x_B / ((sin(theta) / I_y) * (-l / 2) - (cos(theta) / I_z) * (w + l - v_bar))
M_C = sigma_x_G / ((sin(theta) / I_y) * (l / 2) - (cos(theta) / I_z) * (l - v_bar))

M_B = M_B.to(kN * m)
M_C = M_C.to(kN * m)

print(f"M_B = {M_B}")
print(f"M_C = {M_C}")
