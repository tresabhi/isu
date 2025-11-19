import pint
from math import acos

ur = pint.UnitRegistry()
km = ur.km
s = ur.s

e = 0.1
h_p = 200 * km

e_prime = 0.2
h_p_prime = 150 * km

mu_sun = 132.7e9 * km**3 / s**2
mu_earth = 398600 * km**3 / s**2
mu_mercury = 22930 * km**3 / s**2

R_earth = 149.6e6 * km
R_mercury = 57.91e6 * km

r_earth = 6378 * km
r_mercury = 2440 * km

a_T = (R_earth + R_mercury) / 2

v_pT = (mu_sun * 2 / R_mercury - 1 / a_T) ** (1 / 2)
v_aT = (mu_sun * 2 / R_earth - 1 / a_T) ** (1 / 2)

v_earth = (mu_sun / R_earth) ** (1 / 2)
v_mercury = (mu_sun / R_mercury) ** (1 / 2)

v_infinity_earth = abs(v_aT - v_earth)
v_infinity_mercury = abs(v_pT - v_mercury)

r_p = R_earth + h_p
a = r_p / (1 - e)
v_p = (mu_earth * (2 / r_p - 1 / a)) ** (1 / 2)

r_p_prime = R_mercury + h_p_prime
a_prime = r_p_prime / (1 - e_prime)
v_p_prime = (mu_mercury * (2 / r_p_prime - 1 / a_prime)) ** (1 / 2)

v_H = (v_infinity_earth**2 + 2 * (mu_earth / r_p)) ** (1 / 2)
delta_v = v_H - v_p

v_H_prime = (v_infinity_mercury**2 + 2 * (mu_mercury / r_p_prime)) ** (1 / 2)
delta_v_prime = v_H_prime - v_p_prime

delta_v_total = delta_v + delta_v_prime
beta = acos(1 / (1 + ((r_p * v_infinity_earth**2) / mu_earth)))
delta = abs(a_prime) * (e_prime**2 - 1) ** (1 / 2)


print("delta_v (near Earth) =", delta_v)
print("delta_v (near Mercury) =", delta_v_prime)
print("delta_v_total =", delta_v_total, "\n")

print("beta =", beta)
print("delta =", delta)
