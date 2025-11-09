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

Preliminaries:

$$
v_\infty = \sqrt{\frac{\mu}{-a}}
$$

$$
a_1 = -\frac{\mu}{v_\infty^2}
$$

$$
v_{a1} = \sqrt{v_\infty^2 - 2\frac{\mu}{r_a}}
$$

Because this problem has so many repeating parts, I abstracted away a lot of the complexity into Python functions and wrote a script to solve this problem:
