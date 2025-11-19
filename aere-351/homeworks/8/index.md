# AERE 351 Homework 8

## 1.

Given/from the Internet:

$$
\mu_\odot = 1.327*10^{11}km^3/s^2
$$

$$
r_E = 1.496*10^8km
$$

$$
R_E = 6371km
$$

$$
a_A = 1.5 r_E = 1.5 * 1.496*10^8km = 2.244*10^8km
$$

$$
e_A = 0.2
$$

$$
h_S = 400km
$$

$$
r_S = R_E + h_S = 6371km + 400km = 6771km
$$

$$
\mu_E = 3.98600 * 10^5 km^3/s^2
$$

Asteroid's orbit:

$$
r_{aA} = a_A (1 + e_A) = 2.244*10^8km (1 + 0.2) = 2.6928*10^8 km
$$

$$
r_{pA} = a_A (1 - e_A) = 2.244*10^8km (1 - 0.2) = 1.7952*10^8 km
$$

$$
v_{aA} = \sqrt{\mu_S \left( \frac{2}{r_{aA}} - \frac{1}{a_A} \right)}
$$

$$
v_{aA} = \sqrt{1.327*10^{11}km^3/s^2 \left( \frac{2}{2.6928*10^8km} - \frac{1}{2.244*10^8km} \right)} = 19.855 km/s
$$

Earth's orbit:

$$
v_{E} = \sqrt{\frac{\mu_\odot}{r_E}} = \sqrt{\frac{1.327*10^{11}km^3/s^2}{1.496*10^8km}} = 29.78 km/s
$$

Transfer orbit:

$$
a_T = \frac{r_E + r_{aA}}{2} = \frac{1.496*10^8km + 2.6928*10^8km}{2} = 2.0944*10^8km
$$

$$
v_{pT} = \sqrt{\mu_\odot \left( \frac{2}{r_E} - \frac{1}{a_T} \right)}
$$

$$
v_{pT} = \sqrt{1.327*10^{11}km^3/s^2 \left( \frac{2}{1.496*10^8km} - \frac{1}{2.0944*10^8km} \right)} = 33.771 km/s
$$

Satellites's orbit (initially):

$$
v_S = \sqrt{\frac{\mu_E}{r_S}} = \sqrt{\frac{3.98600 * 10^5 km^3/s^2}{6771km}} = 7.673 km/s
$$

Residue:

$$
v_\infty = v_{pT} - v_E = 33.771 km/s - 29.78 km/s = 3.99 km/s
$$

Velocity at perigee of the escape hyperbola:

$$
v_{pH} = \sqrt{v_\infty^2 + 2 \frac{\mu_E}{r_S}} = \sqrt{(3.99km/s)^2 + 2 \frac{3.98600 * 10^5 km^3/s^2}{6771km}} = 11.561 km/s
$$

Boost from Earth orbit to escape hyperbola:

$$
\Delta v = v_{pH} - v_S = 11.561 km/s - 7.673 km/s = \boxed{3.89 km/s}
$$

I just realized we only need the departure velocity. I prepared the velocities to get the total delta v for the rendezvous too, oh well. Transfer time:

$$
T_T = 2 \pi \sqrt{\frac{a_T^3}{\mu_\odot}} = 2 \pi \sqrt{\frac{(2.0944*10^8km)^3}{1.327*10^{11}km^3/s^2}} = 5.228×10^7s
$$

$$
\Delta T = \frac{T_T}{2} = \frac{5.228×10^7s}{2} = 2.614×10^7s
$$

$$
n_A = \sqrt{\frac{\mu_\odot}{a_A^3}} = \sqrt{\frac{1.327*10^{11}km^3/s^2}{(2.244*10^8km)^3}} = 1.084×10^-7Hz
$$

$$
\Delta \theta = n_A \Delta T = 1.084×10^-7Hz * 2.614×10^7s = 2.834rad
$$

$$
\beta = \pi - \Delta \theta = \pi - 2.834rad = 0.3076 rad = \boxed{17.62°}
$$

Now, for all that again, but this time for the pericenter. These values stay the same:

$$
n_A = 1.084×10^-7Hz
$$

These don't:

$$
a_T = \frac{r_E + r_{pA}}{2} = \frac{1.496*10^8km + 1.7952*10^8 km}{2} = 1.6456×10^8 km
$$

$$
T_T = 2 \pi \sqrt{\frac{a_T^3}{\mu_\odot}} = 2 \pi \sqrt{\frac{(1.6456*10^8km)^3}{1.327*10^{11}km^3/s^2}} = 3.641×10^7s
$$

$$
\Delta T = \frac{T_T}{2} = \frac{3.641×10^7s}{2} = 1.821×10^7s
$$

$$
\Delta \theta = n_A \Delta T = 1.084×10^-7Hz * 1.821×10^7s = 1.974rad
$$

$$
\beta = \pi - \Delta \theta = \pi - 1.974rad = 1.1676rad = \boxed{66.90°}
$$

$$
a_T = \frac{r_E + r_{pA}}{2} = \frac{1.496*10^8km + 1.7952*10^8 km}{2} = 1.6456×10^8 km
$$

$$
v_{pT} = \sqrt{\mu_\odot \left( \frac{2}{r_E} - \frac{1}{a_T} \right)}
$$

$$
v_{pT} = \sqrt{1.327*10^{11}km^3/s^2 * \left( \frac{2}{1.496*10^8km} - \frac{1}{1.6456*10^8km} \right)} = 31.107 km/s
$$

$$
v_\infty = v_{pT} - v_E = 31.107 km/s - 29.78 km/s = 1.33 km/s
$$

$$
v_{pH} = \sqrt{v_\infty^2 + 2 \frac{\mu_E}{r_S}} = \sqrt{(1.33 km/s)^2 + 2 \frac{3.98600 * 10^5 km^3/s^2}{6771km}} = 10.93 km/s
$$

$$
\Delta v = v_{pH} - v_S = 10.93 km/s - 7.673 km/s = \boxed{3.257 km/s}
$$

## 2.

From the Internet:

$$
\mu_\odot = 1.327*10^{11}km^3/s^2
$$

$$
r_M = 2.279×10^8 km
$$

$$
r_J = 7.784×10^8 km
$$

$$
m_\odot = 1.989 × 10^{30} kg
$$

$$
m_M = 6.39 × 10^{23} kg
$$

$$
m_J = 1.89813 × 10^{27} kg
$$

Velocities:

$$
v_M = \sqrt{\frac{\mu_\odot}{r_M}} = \sqrt{\frac{1.327*10^{11}km^3/s^2}{2.279×10^8 km}} = 24.13 km/s
$$

$$
v_J = \sqrt{\frac{\mu_\odot}{r_J}} = \sqrt{\frac{1.327*10^{11}km^3/s^2}{7.784×10^8 km}} = 13.06 km/s
$$

Transfer orbit:

$$
a_T = \frac{r_M + r_J}{2} = \frac{2.279×10^8 km + 7.784×10^8 km}{2} = 5.031×10^8 km
$$

$$
v_{pT} = \sqrt{\mu_\odot \left( \frac{2}{r_M} - \frac{1}{a_T} \right)}
$$

$$
v_{pT} = \sqrt{1.327*10^{11}km^3/s^2 * \left( \frac{2}{2.279×10^8 km} - \frac{1}{5.031×10^8 km} \right)} = 30.01 km/s
$$

$$
v_{aT} = \sqrt{\mu_\odot \left( \frac{2}{r_J} - \frac{1}{a_T} \right)}
$$

$$
v_{aT} = \sqrt{1.327*10^{11}km^3/s^2 * \left( \frac{2}{7.784×10^8 km} - \frac{1}{5.031×10^8 km} \right)} = 8.786 km/s
$$

Boosts:

$$
\Delta v = v_{pT} - v_M + v_J - v_{aT} = 30.01 km/s - 24.13 km/s + 13.06 km/s - 8.786 km/s = \boxed{10.15 km/s}
$$

Periods:

$$
T_M = 2 \pi \sqrt{\frac{r_M^3}{\mu_\odot}} = 2 \pi \sqrt{\frac{(2.279×10^8 km)^3}{1.327*10^{11}km^3/s^2}} = 5.934×10^7s
$$

$$
T_J = 2 \pi \sqrt{\frac{r_J^3}{\mu_\odot}} = 2 \pi \sqrt{\frac{(7.784×10^8 km)^3}{1.327*10^{11}km^3/s^2}} = 3.746×10^8s
$$

$$
T_S = \frac{T_M T_J}{|T_M - T_J|} = \frac{5.934×10^7s \times 3.746×10^8s}{|5.934×10^7s - 3.746×10^8s|} = \boxed{7.051×10^7s}
$$

Spheres of influence:

$$
r_{SOI,M} = \left( \frac{m_M}{m_\odot} \right)^{2/5} r_M = \left( \frac{6.39 × 10^{23} kg}{1.989 × 10^{30} kg} \right)^{2/5} 2.279×10^8 km = \boxed{576091 km}
$$

$$
r_{SOI,J} = \left( \frac{m_J}{m_\odot} \right)^{2/5} r_J = \left( \frac{1.89813 × 10^{27} kg}{1.989 × 10^{30} kg} \right)^{2/5} 7.784×10^8 km = \boxed{4.820×10^7 km}
$$

## 3.

This problem throws the assumption of Earth being in a perfectly circular orbit out the window. This calls for a higher level or precision. To address this, I will derive and list all the equations I will need to solve this problem and implement it in Python. These values were kindly provided by the problem (1 = Earth orbit, 2 = hyperbolic escape orbit, 3 = target orbit around sun):

$$
h_1 = 200km
$$

$$
r_{p3} = 120 * 10^6km
$$

Additionally provided:

$$
\mu_{sun} = 132.7*10^9km^3/s^2
$$

$$
\mu_{earth} = 398600km^3/s^2
$$

$$
a_{earth} = 149.6*10^6km
$$

$$
e_{earth} = 0.0167
$$

$$
r_{earth} = 6378km
$$

$$
R_{earth} = 147.4*10^6km
$$

Actual parking radius:

$$
r_1 = r_{earth} + h_1
$$

Parking velocity:

$$
v_1 = \sqrt{\frac{\mu_{earth}}{r_1}}
$$

The final orbit:

$$
a_3 = \frac{r_{p3} + R_{earth}}{2}
$$

$$
v_{a3} = \sqrt{\mu_{sun} \left( \frac{2}{R_{earth}} - \frac{1}{a_3} \right)}
$$

Earth velocity on that fine day:

$$
v_E = \sqrt{\mu_{sun} \left( \frac{2}{R_{earth}} - \frac{1}{a_{earth}} \right)}
$$

Residue:

$$
v_\infty = v_E - v_{a3}
$$

Hyperbolic velocity after boost from Earth orbit:

$$
v_H = \sqrt{v_\infty^2 + 2 \frac{\mu_{earth}}{r_1}}
$$

The boost:

$$
\Delta v = v_H - v_1
$$

The above implemented in Python:

```py
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

v_infinity = v_E - v_a3
v_H = (v_infinity**2 + 2 * (mu_earth / r_1)) ** (1 / 2)

delta_v = v_H - v_1

print(f"v_infinity = {v_infinity}")
print(f"delta_v = {delta_v}")
```

The output:

```
v_infinity = 1.7986079741242769 kilometer / second
delta_v = 3.3703395487144547 kilometer / second
```
