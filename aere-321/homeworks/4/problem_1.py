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
I_y = w * l**3 + l * w**3
I_z = (
    w * l**3
    + w * l * (l / 2 - v_bar) ** 2
    + l * w**3
    + l * w * (l - v_bar + w / 2) ** 2
)


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

l = l.to_base_units().magnitude
w = w.to_base_units().magnitude
v_bar = v_bar.to_base_units().magnitude
I_y = I_y.to_base_units().magnitude
I_z = I_z.to_base_units().magnitude

A = np.matrix(
    [
        [(-l / 2) / I_y, (w + l - v_bar) / I_z],
        [(w / 2) / I_y, -v_bar / I_z],
    ]
)
b = np.matrix(
    [
        [(4 * MPa).to_base_units().magnitude],
        [(-6 * MPa).to_base_units().magnitude],
    ]
)

solution = np.linalg.solve(A, b)

M_y = solution[0, 0] * Pa
M_z = solution[1, 0] * Pa

M = (M_y**2 + M_z**2) ** (1 / 2)
theta = atan2(M_y.magnitude, M_z.magnitude) * ur.rad

print(f"\nProblem 2:")
print(f"M = {M}")
print(f"theta = {theta.to(deg)}")
