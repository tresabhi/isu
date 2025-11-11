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

![](https://i.imgur.com/wOqiofK.png)

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

## 2.

Given:

$$
\omega_1 = 20\degree
$$

$$
r_{a1} = 11000km
$$

$$
r_{p1} = 10000km
$$

$$
\omega_2 = 80\degree
$$

$$
e_2 = 0.4
$$

$$
r_{p2} = 8000km
$$

From the Internet:

$$
\mu = 3.98600 * 10^5 km^3/s^2
$$

To reach orbit 3 from 1:

$$
\Delta \omega = \omega_2 - \omega_1 = 60\degree
$$

$$
r_{p3} = r_{p1}
$$

$$
r_{a3} = r_{a1}
$$

$$
e_3 = e_1
$$

$$
a_3 = a_1
$$

The smallest intersection:

$$
\theta_1 = \frac{\Delta \omega}{2} = \frac{60\degree}{2} = 30\degree
$$

$$
\theta_3 = \theta_1 - \Delta \omega = 30\degree - 60\degree = -30\degree
$$

$$
e_1 = \frac{r_{a1} - r_{p1}}{r_{a1} + r_{p1}} = \frac{11000km - 10000km}{11000km + 10000km} = 0.04762
$$

$$
a_1 = \frac{r_{a1} + r_{p1}}{2} = \frac{11000km + 10000km}{2} = 10500km
$$

$$
p_1 = a_1 (1 - e_1^2) = 10500km * (1 - 0.04762^2) = 10476km
$$

Velocity as a column vectors:

$$
v_1 = \sqrt{\frac{\mu}{p_1}} \begin{bmatrix}
  -\sin \theta_1 \\
  e_1 + \cos \theta_1
\end{bmatrix}
$$

$$
v_1 = \sqrt{\frac{3.98600 * 10^5 km^3/s^2}{10476km}} \begin{bmatrix}
  -\sin 30\degree \\
  0.04762 + \cos 30\degree
\end{bmatrix} = \begin{bmatrix}
  -3.084 \\
  5.636
\end{bmatrix} km/s
$$

$$
v_3 = \sqrt{\frac{\mu}{p_3}} \begin{bmatrix}
  -\sin \theta_3 \\
  e_3 + \cos \theta_3
\end{bmatrix} = \sqrt{\frac{\mu}{p_1}} \begin{bmatrix}
  -\sin \theta_3 \\
  e_1 + \cos \theta_3
\end{bmatrix}
$$

$$
v_3 = \sqrt{\frac{3.98600 * 10^5 km^3/s^2}{10476km}} \begin{bmatrix}
  -\sin -30\degree \\
  0.04762 + \cos -30\degree
\end{bmatrix} = \begin{bmatrix}
  3.084 \\
  5.636
\end{bmatrix} km/s
$$

Transforming the velocities to a common coordinate system:

$$
v_1' = R_1 v_1 = \begin{bmatrix}
  \cos \omega_1 & -\sin \omega_1 \\
  \sin \omega_1 & \cos \omega_1
\end{bmatrix} v_1
$$

$$
v_1' = \begin{bmatrix}
  \cos 20\degree & -\sin 20\degree \\
  \sin 20\degree & \cos 20\degree
\end{bmatrix} \begin{bmatrix}
  -3.084 \\
  5.636
\end{bmatrix} = \begin{bmatrix}
  -4.826 \\
  4.241
\end{bmatrix} km/s
$$

$$
v_3' = R_3 v_3 = \begin{bmatrix}
  \cos \omega_3 & -\sin \omega_3 \\
  \sin \omega_3 & \cos \omega_3
\end{bmatrix} v_3
$$

$$
\omega_3 = \omega_2 = 80\degree
$$

$$
v_3' = \begin{bmatrix}
  \cos 80\degree & -\sin 80\degree \\
  \sin 80\degree & \cos 80\degree
\end{bmatrix} \begin{bmatrix}
  3.084 \\
  5.636
\end{bmatrix} = \begin{bmatrix}
  -5.015 \\
  4.016
\end{bmatrix} km/s
$$

The difference:

$$
\Delta v_a = |v_1' - v_3'| = \sqrt{(-4.826 - (-5.015))^2 + (4.241 - 4.016)^2} = 0.2938 km/s
$$

Now we turn raise our apogee to that of orbit 2 while keeping the perigee of orbit 3, creating an intermediate orbit 4:

$$
v_{p3} = v_{p1} = \sqrt{\frac{\mu}{p_1}} (1 + e_1) = \sqrt{\frac{3.98600 * 10^5 km^3/s^2}{10476km}} (1 + 0.04762) = 6.462km/s
$$

$$
r_{p4} = r_{p3} = r_{p1} = 10000km
$$

$$
e_2 = \frac{r_{a2} - r_{p2}}{r_{a2} + r_{p2}}
$$

$$
e_2 = 0.4 = \frac{r_{a2} - 8000km}{r_{a2} + 8000km} \implies r_{a2} = 18667km
$$

$$
a_2 = \frac{r_{a2} + r_{p2}}{2} = \frac{18667km + 8000km}{2} = 13334km
$$

$$
p_2 = a_2 (1 - e_2^2) = 13334km (1 - 0.4^2) = 11201 km
$$

$$
r_{a4} = r_{a2} = 18667km
$$

$$
a_4 = \frac{r_{a4} + r_{p4}}{2} = \frac{18667km + 10000km}{2} = 14334km
$$

$$
e_4 = \frac{r_{a4} - r_{p4}}{r_{a4} + r_{p4}} = \frac{18667km - 10000km}{18667km + 10000km} = 0.3023
$$

$$
p_4 = a_4 (1 - e_4^2) = 14334km (1 - 0.3023^2) = 13024km
$$

$$
v_{p4} = \sqrt{\frac{\mu}{p_4}} (1 + e_4) = \sqrt{\frac{3.98600 * 10^5 km^3/s^2}{13024km}} (1 + 0.3023) = 7.205 km/s
$$

$$
\Delta v_b = v_{p4} - v_{p3} = 7.205 km/s - 6.462 km/s = 0.743 km/s
$$

Finally, the perigee raises from orbit 4 to match orbit 2:

$$
v_{a4} = \sqrt{\frac{\mu}{p_4}} (1 - e_4) = \sqrt{\frac{3.98600 * 10^5 km^3/s^2}{13024km}} (1 - 0.3023) = 3.860 km/s
$$

$$
v_{a2} = \sqrt{\frac{\mu}{p_2}} (1 - e_2) = \sqrt{\frac{3.98600 * 10^5 km^3/s^2}{11201km}} (1 - 0.4) = 3.579 km/s
$$

$$
\Delta v_c = v_{a4} - v_{a2} = 3.860 km/s - 3.579 km/s = 0.281 km/s
$$

Finally:

$$
\Delta v = \Delta v_a + \Delta v_b + \Delta v_c = 0.2938 km/s + 0.743 km/s + 0.281 km/s = \boxed{1.318 km/s}
$$

And now for the total time elapsed. Since the first burn was a direct hop from orbit 1 to 3, there will be no term for that:

$$
\Delta t_a = 0
$$

Times for transfer within orbits 3 and 4:

$$
\theta_3 = -30\degree
$$

$$
\theta_3' = 0
$$

$$
E = 2 \arctan \left( \sqrt{\frac{1 - e}{1 + e}} \tan \frac{\theta}{2} \right)
$$

$$
E_3 = 2 \arctan \left( \sqrt{\frac{1 - 0.04762}{1 + 0.04762}} \tan \frac{-30\degree}{2} \right) = -0.5003 rad
$$

$$
E_3' = 0
$$

$$
M_3 = E_3 - e_3 \sin E_3 = -0.5003 - 0.04762 \sin (-0.5003) = -0.4775
$$

$$
M_3' = 0
$$

$$
M = \sqrt{\frac{\mu}{a^3}} t
$$

$$
t = \sqrt{\frac{a^3}{\mu}} M
$$

$$
t_3 = \sqrt{\frac{a_3^3}{\mu}} M_3 = \sqrt{\frac{(10500km)^3}{3.98600 * 10^5 km^3/s^2}} (-0.4775) = -813.75s
$$

$$
t_3' = 0
$$

$$
\Delta t_b = t_3' - t_3 = 813.75s
$$

The other transfer orbit goes from the perigee to the apogee, so that's half the revolution:

$$
\Delta t_c = \frac{1}{2} T_4 = \frac{1}{2} 2 \pi \sqrt{\frac{a^3}{\mu}} = \pi \sqrt{\frac{(a_4^3)}{\mu}} = \pi \sqrt{\frac{(14334km)^3}{3.98600 * 10^5 km^3/s^2}} = 8539.5s
$$

Finally:

$$
\Delta t = \Delta t_a + \Delta t_b + \Delta t_c = 0 + 813.75s + 8539.5s = \boxed{9353.25s}
$$

## 3.

From the last problem:

$$
p_1 = 10476km
$$

$$
p_2 = 11201km
$$

$$
e_1 = 0.04762
$$

$$
e_2 = 0.4
$$

$$
\omega_1 = 20\degree
$$

$$
\omega_2 = 80\degree
$$

System of equations:

$$
r_1 = \frac{p_1}{1 + e_1 \cos \theta_1} = r_2 = \frac{p_2}{1 + e_2 \cos \theta_2}
$$

$$
\omega_1 + \theta_1 = \omega_2 + \theta_2
$$
