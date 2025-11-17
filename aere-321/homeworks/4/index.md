# AERE 321 Homework 3

## 1.

![](https://i.imgur.com/qy8ZRZvm.png)

Given:

$$
M = 2kN m
$$

$$
\theta = 60\degree
$$

$$
l = 200mm
$$

$$
w = 50mm
$$

Inertia about the $y$ axis:

$$
I_y = wl^3 + lw^3
$$

$$
I_y = 50mm * (200mm)^3 + 200mm * (50mm)^3 = 4.25*10^{-4}m^4
$$

The problem is ambiguous on where the origin is, so I will place a temporary origin at the bottom of the stem:

![](https://i.imgur.com/CVVe4H8.png)

The idea is that I will find the centroid with this coordinate system and place the real $y, ~ z$ axes there.

$$
\bar{u} = 0
$$

$$
\bar{v} = \frac{wl * l/2 + wl * (l + b/2)}{2wl} = \frac{l/2 + l + b/2}{2}
$$

$$
\bar{v} = \frac{200mm/2 + 200mm + 50mm/2}{2} = 162.5 mm
$$

This gives me the position of the origin in relation to the edge of the stem:

![](https://i.imgur.com/NjJD6cr.png)

This allows me to get the inertia about the $z$ axis:

$$
I_z = wl^3 + wl * (l/2 - \bar{v})^2 + lw^3 + lw * (l - \bar{v} + b/2)^2
$$

$$
I_z = 50mm * (200mm)^3 + 50mm * 200mm * (200mm / 2 - 162.5mm)^2 + 200mm * (50mm)^3 + 200mm * 50mm * (200mm - 162.5mm + 25mm / 2)^2
$$

$$
I_z = 4.891*10^8mm^4
$$

And the product of inertia:

$$
I_{xy} = 0 + wl * 0 * 0 + 0 + lw * 0 * (l/2 + w/2) = 0
$$

The orientation of the neutral axis because of this should be $0$:

$$
\tan 2\theta_p = \frac{-I_{xy}}{(I_x - I_y) / 2} = 0
$$

$$
\theta_p = \frac{1}{2} \arctan 0 = \boxed{0}
$$

Thus, the neutral axis is just the origin. That was part (b) of the question, so I will go go back to part (a) that I never addressed. Decomposing the torque:

$$
M_z = M \cos \theta = 2kN m \cos 60\degree = 1 kN m
$$

$$
M_y = M \sin \theta = 2kN m \sin 60\degree = 1.732 kN m
$$

And since $L_{yz} = 0$, I can get away with using the highly simplified stress equation from lecture slide 31:

$$
\sigma_x = \frac{M_y}{I_y} z - \frac{M_z}{I_z} y
$$

There's a lot of points that I suspect the maximum stress might exist:

![](https://i.imgur.com/C0w3m4B.png)

Smells like a job for a computer.
