from math import sin, cos, acos, radians, pi
import pint

ur = pint.UnitRegistry()
km = ur.kilometer
s = ur.second
deg = ur.degree

mu = 3.98600e5 * (km**3) / (s**2)

r_p_1 = 10000 * km
r_a_1 = 11000 * km
omega_1 = 20 * deg

r_p_2 = 8000 * km
e_2 = 0.4
omega_2 = 80 * deg

a_1 = (r_p_1 + r_a_1) / 2
e1 = (r_a_1 - r_p_1) / (r_a_1 + r_p_1)
a2 = r_p_2 / (1 - e_2)
r_a2 = a2 * (1 + e_2)
delta_w = (omega_2 - omega_1).to("radian").magnitude

a3 = a_1
e3 = e1
w3 = omega_2


def r_orbit(a, e, w, theta):
    return a * (1 - e**2) / (1 + e * cos(theta - w))


theta_transfer = (omega_1 + w3) / 2

r1 = r_orbit(
    a_1, e1, omega_1.to("radian").magnitude, theta_transfer.to("radian").magnitude
)
v1 = (mu * (2 / r1 - 1 / a_1)) ** (1 / 2)

v3 = v1
delta_v1 = 2 * v1 * sin(abs((w3 - omega_1).to("radian").magnitude) / 2)

r_p3 = r_p_1
r_a4 = r_a2

a4 = (r_p3 + r_a4) / 2

v_p3 = (mu * (2 / r_p3 - 1 / a3)) ** (1 / 2)
v_p4 = (mu * (2 / r_p3 - 1 / a4)) ** (1 / 2)
delta_v2 = abs(v_p4 - v_p3)

r_a4 = r_a2
v_a4 = (mu * (2 / r_a4 - 1 / a4)) ** (1 / 2)
v_a2 = (mu * (2 / r_a4 - 1 / a2)) ** (1 / 2)
delta_v3 = abs(v_a2 - v_a4)

T_transfer = pi * (a4**3 / mu) ** (1 / 2)

delta_v_total = delta_v1 + delta_v2 + delta_v3

print(f"Intersection true anomaly θ = {theta_transfer.to('degree'):.2f}")
print(f"Δv1 (reorientation): {delta_v1.to('km/s'):.4f}")
print(f"Δv2 (at perigee): {delta_v2.to('km/s'):.4f}")
print(f"Δv3 (at apogee): {delta_v3.to('km/s'):.4f}")
print(f"Total Δv: {delta_v_total.to('km/s'):.4f}")
print(f"Transfer time: {T_transfer.to('hour'):.2f}")
