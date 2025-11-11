from math import sin, cos, sqrt, asin, acos, pi, atan2
import pint

ur = pint.UnitRegistry()
km = ur.kilometer
s = ur.second
deg = ur.degree

mu = 3.98600e5 * (km**3) / (s**2)

a = 12000 * km
e = 0.2

omega_1 = 15 * deg
i_1 = 120 * deg
Omega_1 = 45 * deg

omega_2 = omega_1
i_2 = 85 * deg
Omega_2 = 130 * deg

delta_Omega = Omega_2 - Omega_1
delta_i = i_2 - i_1

if (delta_Omega > 0 and delta_i > 0) or (delta_Omega < 0 and delta_i < 0):
    # Concordant

    raise NotImplementedError()
else:
    # Discordant

    alpha = acos(cos(i_1) * cos(i_2) + sin(i_1) * sin(i_2) * cos(delta_Omega))

    u_1_c = acos((cos(alpha) * cos(i_1) - cos(i_2)) / (sin(alpha) * sin(i_1)))
    u_2_c = acos((cos(alpha) * cos(i_2) - cos(i_1)) / (sin(alpha) * sin(i_2)))
    u_1_s = asin((sin(delta_Omega) * sin(i_2)) / sin(alpha))
    u_2_s = asin((sin(delta_Omega) * sin(i_1)) / sin(alpha))

    u_1 = atan2(u_1_s, u_1_c)
    u_2 = atan2(u_2_s, u_2_c)

    theta_1 = u_1 - omega_1
    theta_2 = u_2 - omega_2

    p = a * (1 - e**2)
    v_theta = ((mu / p) ** (1 / 2)) * (1 + e * cos(theta_1))
    delta_v = 2 * v_theta * sin(alpha / 2)

    print(delta_v)
