# AERE 351 Homework 5

## 1.

Given:

$$
i_0 = 10\degree
$$

$$
r_a = 12000km
$$

$$
r_p = 8000km
$$

$$
i_1 = 30\degree
$$

$$
v_\infty = 3km/s
$$

$$
\Omega_0 = \Omega_1
$$

From the Internet:

$$
\mu = 3.98600 * 10^5 km^3/s^2
$$

Semi-major axis from residue velocity:

$$
v_\infty = \sqrt{\frac{\mu}{-a}}
$$

$$
a = -\frac{\mu}{v_\infty^2}
$$

$\Delta v$ for inclination change:

$$
\Delta v = \Delta v_\theta  = 2 v_\theta \sin \frac{\Delta i}{2}
$$

Vis-viva equation:

$$
v = \sqrt{\mu \left( \frac{2}{r} - \frac{1}{a} \right)}
$$

Finally, the combined equation for $\Delta v$ when doing an inclination change with a push to hyperbolic (cosine law):

$$
(\Delta v)^2 = v_0^2 + v_1^2 - 2 v_0 v_1 \cos \Delta i
$$

$$
\Delta v = \sqrt{v_0^2 + v_1^2 - 2 v_0 v_1 \cos \Delta i}
$$

Because this problem has so many repeating parts, I abstracted away a lot of the complexity into Python functions and wrote a script to solve this problem:

```py
from math import sin, cos, sqrt
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

a_0 = (r_p + r_a) / 2
e_0 = (r_a - r_p) / (r_a + r_p)
a_1 = -mu / (v_inf**2)


def vis_viva(r, a):
    return (mu * (2 / r - 1 / a)) ** (1 / 2)


def delta_v_plane_change(v, delta_i):
    return 2 * v * sin(delta_i / 2)


def delta_v_combined(v_0, v_1, delta_i):
    return (v_0**2 + v_1**2 - 2 * v_0 * v_1 * cos(delta_i)) ** (1 / 2)


v_p_0 = vis_viva(r_p, a_0)
v_a_0 = vis_viva(r_a, a_0)
v_p_1 = vis_viva(r_p, a_1)
v_a_1 = vis_viva(r_a, a_1)

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

from math import sin, cos, sqrt
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

a_0 = (r_p + r_a) / 2
e_0 = (r_a - r_p) / (r_a + r_p)
a_1 = -mu / (v_inf**2)


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


v_p_0 = vis_viva(r_p, a_0)
v_a_0 = vis_viva(r_a, a_0)
v_p_1 = vis_viva(r_p, a_1)
v_a_1 = vis_viva(r_a, a_1)

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
```

The output:

```
delta_v (case 1, order 1): 6.311186053547144 kilometer / second
delta_v (case 1, order 2): 5.376565821482492 kilometer / second
delta_v (case 1, order 3): 4.118689998883883 kilometer / second

delta_v (case 2, order 1): 6.546654590197828 kilometer / second
delta_v (case 2, order 2): 5.320593015623034 kilometer / second
delta_v (case 2, order 3): 4.226486101561274 kilometer / second
```
