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

As for the circular section, the game plan is this order of operations:

![](https://i.imgur.com/qcstOZ4.png)

The inertia of a full circle:

$$
I_\text{outer} = \frac{\pi}{4} R^4 = \frac{\pi}{4} \left( r + \frac{t}{2} \right)^4
$$

The inertia of the inner cutaway:

$$
I_\text{inner} = \frac{\pi}{4} \left( r - \frac{t}{2} \right)^4
$$

Inertia of the full rim:

$$
I_\text{rim} = I_\text{outer} - I_\text{inner} = \frac{\pi}{4} \left( r + \frac{t}{2} \right)^4 - \frac{\pi}{4} \left( r - \frac{t}{2} \right)^4 = \frac{\pi}{4} \left[ \left( r + \frac{t}{2} \right)^4 - \left( r - \frac{t}{2} \right)^4 \right]
$$

And the inertia of a wedge of angular size $\theta$:

$$
I_\text{wedge} = \theta \frac{\pi}{4} R^4 = 2 \theta_0 \frac{\pi}{4} R^4 = \theta_0 \frac{\pi}{2} R^4
$$

The wedge cutaway:

$$
I_\text{wedge cutaway} = \theta_0 \frac{\pi}{2} \left[ \left( r + \frac{t}{2} \right)^4 - \left( r - \frac{t}{2} \right)^4 \right]
$$

And total inertia:

$$
I = I_\text{rim} - I_\text{wedge cutaway}
$$

$$
I = \frac{\pi}{4} \left[ \left( r + \frac{t}{2} \right)^4 - \left( r - \frac{t}{2} \right)^4 \right] - \theta_0 \frac{\pi}{2} \left[ \left( r + \frac{t}{2} \right)^4 - \left( r - \frac{t}{2} \right)^4 \right]
$$

$$
I = \left( \frac{\pi}{4} - \theta_0 \frac{\pi}{2} \right) \left[ \left( r + \frac{t}{2} \right)^4 - \left( r - \frac{t}{2} \right)^4 \right]
$$

$$
\boxed{I = \pi \left( \frac{1}{4} - \frac{\theta_0}{2} \right) \left[ \left( r + \frac{t}{2} \right)^4 - \left( r - \frac{t}{2} \right)^4 \right]}
$$
