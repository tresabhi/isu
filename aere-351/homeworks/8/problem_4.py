import pint

ur = pint.UnitRegistry()
km = ur.km
s = ur.s

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
