from math import sin, cos
import pint

ur = pint.UnitRegistry()
km = ur.kilometer
s = ur.second
deg = ur.degree

mu = 3.98600e5 * (km**3) / (s**2)

r_p = 8000 * km
r_a = 12000 * km
i_1 = 10 * deg
i_2 = 30 * deg
delta_i = abs(i_2 - i_1)

v_inf = 3 * km / s

a_elliptical = (r_p + r_a) / 2
e_elliptical = (r_a - r_p) / (r_a + r_p)

a_hyperbolic = -mu / (v_inf**2)


def vis_viva(r, a):
    return (mu * (2 / r - 1 / a)) ** (1 / 2)


def delta_v_plane_change(v, delta_i):
    return 2 * v * sin(delta_i / 2)


def delta_v_combined(v_0, v_1, delta_i):
    v_y = v_1 * cos(delta_i)
    v_z = v_1 * sin(delta_i)

    delta_v_y = v_y - v_0
    delta_v_z = v_z

    return (delta_v_y**2 + delta_v_z**2) ** (1 / 2)


v_p_0 = vis_viva(r_p, a_elliptical)
v_a_0 = vis_viva(r_a, a_elliptical)
v_p_1 = vis_viva(r_p, a_hyperbolic)
v_a_1 = vis_viva(r_a, a_hyperbolic)


delta_v_case_1_order_1 = abs(v_p_1 - v_p_0) + delta_v_plane_change(v_p_1, delta_i)
delta_v_case_1_order_2 = delta_v_plane_change(v_p_0, delta_i) + abs(v_p_1 - v_p_0)
delta_v_case_1_order_3 = delta_v_combined(v_p_0, v_p_1, delta_i)

delta_v_case_2_order_1 = abs(v_a_1 - v_a_0) + delta_v_plane_change(v_a_1, delta_i)
delta_v_case_2_order_2 = delta_v_plane_change(v_a_0, delta_i) + abs(v_a_1 - v_a_0)
delta_v_case_2_order_3 = delta_v_combined(v_a_0, v_a_1, delta_i)

print("delta_v (case 1, order 1):", delta_v_case_1_order_1)
print("delta_v (case 1, order 2):", delta_v_case_1_order_2)
print("delta_v (case 1, order 3):", delta_v_case_1_order_3, end="\n\n")

print("delta_v (case 2, order 1):", delta_v_case_2_order_1)
print("delta_v (case 2, order 2):", delta_v_case_2_order_2)
print("delta_v (case 2, order 3):", delta_v_case_2_order_3)
