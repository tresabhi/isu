import pint
from math import sin, cos, atan2
import numpy as np

ur = pint.UnitRegistry()

N = ur.N
m = ur.m
kN = 1000 * N
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

print(I_z)


def sigma_x(z, y):
    return (M_y / I_y) * z - (M_z / I_z) * y


sigma_x_A = sigma_x(l / 2, w + l - v_bar).to(MPa)
sigma_x_B = sigma_x(-l / 2, w + l - v_bar).to(MPa)
sigma_x_C = sigma_x(l / 2, l - v_bar).to(MPa)
sigma_x_D = sigma_x(-l / 2, l - v_bar).to(MPa)
sigma_x_E = sigma_x(w / 2, l - v_bar).to(MPa)
sigma_x_F = sigma_x(-w / 2, l - v_bar).to(MPa)
sigma_x_G = sigma_x(w / 2, -v_bar).to(MPa)
sigma_x_H = sigma_x(-w / 2, -v_bar).to(MPa)

print(f"sigma_x_A = {sigma_x_A}")
print(f"sigma_x_B = {sigma_x_B}")
print(f"sigma_x_C = {sigma_x_C}")
print(f"sigma_x_D = {sigma_x_D}")
print(f"sigma_x_E = {sigma_x_E}")
print(f"sigma_x_F = {sigma_x_F}")
print(f"sigma_x_G = {sigma_x_G}")
print(f"sigma_x_H = {sigma_x_H}")
