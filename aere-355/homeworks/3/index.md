# AERE 355 Homework 3

## 1.

![](https://i.imgur.com/eV1c0y2.png)

Given:

$$
\psi = -20\deg
$$

$$
\theta = 7\deg
$$

$$
\phi = 0\deg
$$

$$
\text{z-y-x}
$$

$$
V_a = 267.987 x_b + 40 y_b + 32.905 z_b ~ ft/s
$$

### a.

This will be very difficult to do with "by hand" (I know I use LaTeX but the process is similar) so I will be using Python for the following matrix equation:

![](https://i.imgur.com/TuSGfEm.png)

My implementation:

```py
import numpy as np
import math

psi = np.deg2rad(-20)
theta = np.deg2rad(7)
phi = np.deg2rad(0)

C_psi = math.cos(psi)
C_theta = math.cos(theta)
C_phi = math.cos(phi)

S_psi = math.sin(psi)
S_theta = math.sin(theta)
S_phi = math.sin(phi)

R = np.matrix(
    [
        [
            C_theta * C_psi,
            S_phi * S_theta * C_psi - C_phi * S_psi,
            C_phi * S_theta * C_psi + S_phi * S_psi,
        ],
        [
            C_theta * S_psi,
            S_phi * S_theta * S_psi + C_phi * C_psi,
            C_phi * S_theta * S_psi - S_phi * C_psi,
        ],
        [-S_theta, S_phi * C_theta, C_phi * C_theta],
    ]
)

V = np.matrix(
    [
        [267.987],
        [40],
        [32.905],
    ]
)

dr_dt = R * V

print(dr_dt)
```

The output:

```
[[ 2.67397415e+02]
 [-5.47575889e+01]
 [ 3.31388642e-04]]
```

Finally:

$$
\begin{bmatrix*}
  \frac{dx}{dt} \\
  \frac{dy}{dt} \\
  \frac{dz}{dt}
\end{bmatrix*} = \begin{bmatrix*}
  267.4 \\
  -54.76 \\
  0
\end{bmatrix*} \frac{ft}{s}
$$
