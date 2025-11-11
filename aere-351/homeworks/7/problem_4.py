from math import sin, cos, sqrt, asin, acos, atan2, pi
import pint

ur = pint.UnitRegistry()
km = ur.kilometer
s = ur.second
deg = ur.degree
rad = ur.radian

mu = 3.98600e5 * (km**3) / (s**2)

a = 12000 * km
e = 0.2
p = a * (1 - e**2)

omega_1 = 15 * deg
i_1 = 120 * deg
Omega_1 = 45 * deg

i_2 = 85 * deg
Omega_2 = 130 * deg

delta_Omega = Omega_2 - Omega_1
delta_i = i_2 - i_1

if (delta_Omega > 0 and delta_i > 0) or (delta_Omega < 0 and delta_i < 0):
    # Concordant

    raise NotImplementedError("I don't have the willpower")
else:
    # Discordant

    alpha = acos(cos(i_1) * cos(i_2) + sin(i_1) * sin(i_2) * cos(delta_Omega))

    cos_u_1 = (cos(i_2) - cos(alpha) * cos(i_1)) / (sin(alpha) * sin(i_1))
    cos_u_2 = (cos(alpha) * cos(i_2) - cos(i_1)) / (sin(alpha) * sin(i_2))
    sin_u_1 = (sin(delta_Omega) * sin(i_2)) / sin(alpha)
    sin_u_2 = (sin(delta_Omega) * sin(i_1)) / sin(alpha)

    u_1 = atan2(sin_u_1, cos_u_1)
    u_2 = atan2(sin_u_2, cos_u_2)

    theta_1 = 2 * pi - u_1 - omega_1
    theta_2 = theta_1
    omega_2 = 2 * pi - u_2 - theta_2

    v_theta = ((mu / p) ** (1 / 2)) * (1 + e * cos(theta_1))
    delta_v = 2 * v_theta * sin(alpha / 2)

    print(f"theta_1 = {theta_1.to(deg)}")
    print(f"theta_2 = {theta_2.to(deg)}")
    print(f"delta_v = {delta_v}")
    print(f"omega_2 = {omega_2.to(deg)}")
