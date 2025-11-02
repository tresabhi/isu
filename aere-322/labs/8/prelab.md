# AERE 322 Prelab 8

## 1.

I split the assembly into 3 parts:

![](https://i.imgur.com/tEqx0zN.png)

The areas (the area of part 3 doesn't matter as it won't show up in the parallel axis theorem):

$$
A_1 = A_2 = bt
$$

The local inertias:

$$
I_1 = I_2 = \frac{1}{12} bt^3
$$

$$
I_3 = \frac{1}{12} t (h - 2 \frac{1}{2} t)^3 = \frac{1}{12} t (h - t)^3
$$

Parallel axis theorem:

$$
I = I_1 + I_2 + I_3 + A_1 y_1^2 + A_2 y_2^2 + A_3 y_3^2
$$

$$
I = 2 I_1 + I_3 + 2 A_1 y_1^2
$$

$$
I = 2 \frac{1}{12} bt^3 + \frac{1}{12} t (h - t)^3 + 2 bt \left( \frac{h}{2} \right)^2
$$

$$
\boxed{I = \frac{1}{2} bh^2 t + \frac{1}{6} bt^3 + \frac{1}{12} t(h - t)^3}
$$
