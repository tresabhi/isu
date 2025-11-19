import pint

ur = pint.UnitRegistry()
km = ur.km
s = ur.s

h_1 = 200 * km
r_p3 = 120e6 * km

mu_sun = 132.7e9 * km**3 / s**2
mu_earth = 398600 * km**3 / s**2
a_earth = 149.6e6 * km
e_earth = 0.0167
r_earth = 6378 * km
R_earth = 147.4e6 * km

r_1 = r_earth + h_1
v_1 = (mu_earth / r_1) ** (1 / 2)

a_3 = (r_p3 + R_earth) / 2
v_a3 = (mu_sun * (2 / R_earth - 1 / a_3)) ** (1 / 2)

v_E = (mu_sun * (2 / R_earth - 1 / a_earth)) ** (1 / 2)

v_infinity = v_a3 - v_E
v_H = (v_infinity**2 + 2 * (mu_earth / r_1)) ** (1 / 2)

delta_v = v_H - v_1

print(f"v_infinity = {v_infinity}")
print(f"delta_v = {delta_v}")
