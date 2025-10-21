# AERE 355 Homework 3

My main source of equations for the latter problems:

![](https://i.imgur.com/pkv9kkQ.png)

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
\end{bmatrix*} \approx \begin{bmatrix*}
  267.4 \\
  -54.76 \\
  0
\end{bmatrix*} \frac{ft}{s}
$$

### b.

With wind of $40 ft/s$ from the Southeast, the readings on board the airplane will need to be compensated for. The coordinate system is a bit goofy so I drew it out:

![](https://i.imgur.com/ZNlvuMC.png)

Thus, the wind in the fixed frame is:

$$
W_f = -40 \sqrt{2} x_f - 40 \sqrt{2} y_f ~ ft/s
$$

And the wind in the inertial frame:

$$
W_i = R^{-1} W_f
$$

The adjusted wind readings in inertial frame:

$$
V' = V + W_i
$$

And finally, the adjusted velocity in fixed frame:

$$
V_f' = R V'
$$

Python code for all that is just a fork from the last question:

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

W_f = np.matrix(
    [
        [-40 * math.sqrt(2)],
        [-40 * math.sqrt(2)],
        [0],
    ]
)

W_i = R**-1 * W_f

V_prime = V + W_i

V_f_prime = R * V_prime

print(V_f_prime)
```

The output:

```
[[ 2.10828873e+02]
 [-1.11326131e+02]
 [ 3.31388642e-04]]
```

This makes sense since the $z$ component is unchanged and the other values are lower in magnitude since we're now compensation for the fact the wind gives us a "fake velocity" because the sensors are relative to the wind.

$$
V_f' \approx \begin{bmatrix*}
  210.8 \\
  -111.3 \\
  0
\end{bmatrix*} \frac{ft}{s}
$$

## 2.

![](https://i.imgur.com/quJgF10.png)

![](https://i.imgur.com/XXt5TlE.png)

Given:

$$
C_{l_p} = ~ ?
$$

$$
C_{n_r} = ~ ?
$$

$$
C_{L_{\alpha_w}} = C_{L_{\alpha_v}} = 0.1 \deg^{-1} \quad \text{(2D)}
$$

$$
c_t = 4.4 ft
$$

$$
c_r = 9 ft
$$

$$
\eta_v = 1
$$

Some preliminaries:

$$
AR = \frac{b^2}{S} = \frac{(36ft)^2}{232ft^2} = 5.586
$$

$$
\lambda = \frac{c_t}{c_r} = \frac{4.4}{9} = 0.4889
$$

$$
V_v = \frac{S_v l_v}{S b} = \frac{37ft^2 * 18.5ft}{232ft^2 * 36ft} = 0.08196
$$

2D slope from degrees to radians:

$$
C_{L_{\alpha_w}} = C_{L_{\alpha_v}} = 0.1 \deg^{-1} = 5.73 rad^{-1} \quad \text{(2D)}
$$

2D to 3D:

$$
C_{L_{\alpha_w}} = C_{L_{\alpha_v}} = \frac{5.73}{1 + \frac{5.73}{\pi 5.586}} = 4.32 rad^{-1} \quad \text{(3D)}
$$

Estimation:

$$
C_{l_p} = - \frac{C_{L_\alpha}}{12} \frac{1 + 3 \lambda}{1 + \lambda}
$$

$$
C_{l_p} = - \frac{4.32}{12} \frac{1 + 3 * 0.4889}{1 + 0.4889} = \boxed{-0.5964 rad^{-1}}
$$

$$
C_{n_r} = -2 \eta_v V_v \frac{l_v}{b} C_{L_{\alpha_v}}
$$

$$
C_{n_r} = -2 * 1 * 0.08196 * \frac{18.5ft}{36ft} * 4.32 = \boxed{-0.3639 rad^{-1}}
$$

## 3.

Given:

$$
C_{L_{\alpha_v}} = 0.1 \deg^{-1} \quad \text{(2D)}
$$

$$
S_v = 900ft^2
$$

$$
b_v / 2 = 32.6ft
$$

$$
l_v = 105ft
$$

$$
AR_w = 6.96
$$

$$
\Lambda_{c/4_w} = 35\deg
$$

$$
z_w/d = 0.3
$$

$$
l_f = 230ft
$$

$$
S_{fs} = 5075 ft^2
$$

$$
x_m = 95ft
$$

$$
w_f = 22ft
$$

$$
h_1 = 24ft
$$

$$
h_2 = 17ft
$$

$$
h = 28ft
$$

$$
\eta_v = 1
$$

$$
\text{Sea level conditions}
$$

$$
V = \text{Mach} ~ 0.25
$$

![](https://i.imgur.com/Kc8dV2l.png)

![](https://i.imgur.com/iYqbo7C.png)

Find:

$$
C_{y_\beta} = ~ ?
$$

$$
C_{n_\beta} = ~ ?
$$

$$
C_{n_r} = ~ ?
$$

Derivation:

$$
\eta_v \left( 1 + \frac{d \sigma}{d \beta} \right) = 0.724 + 3.06 \frac{S_v / S}{1 + \cos \Lambda_{c/4_w}} + 0.4 \frac{z_w}{d} + 0.009 AR_w
$$

$$
\eta_v \left( 1 + \frac{d \sigma}{d \beta} \right) = 0.724 + 3.06 \frac{\frac{900ft^2}{5500ft^2}}{1 + \cos 35\deg} + 0.4 * 0.3 + 0.009 * 6.96 = 1.182
$$

$$
C_{L_{\alpha_v}} = 0.1 \deg^{-1} = 5.73 rad^{-1} \quad \text{(2D)}
$$

$$
C_{L_{\alpha_v}} = \frac{5.73}{1 + \frac{5.73}{\pi 5.586}} = 4.32 rad^{-1} \quad \text{(3D)}
$$

$$
C_{y_\beta} = -\eta \frac{S_v}{S} C_{L_{\alpha_v}} \left( 1 + \frac{d \sigma}{d \beta} \right)
$$

$$
C_{y_\beta} = - \frac{900ft^2}{5500ft^2} * 4.32 * 1.182 = \boxed{-0.8356}
$$

$$
a = 1116.45 ft/s
$$

$$
v = 1.5723 * 10^{-4} ft^2/s
$$

$$
V = 0.25a = 0.25 * 1116.45 ft/s = 279.11 ft/s
$$

$$
R_{l_f} = V \frac{l_f}{v}
$$

$$
R_{l_f} = 279.11 ft/s * \frac{230ft}{1.5723 * 10^{-4} ft^2/s} = 4.083*10^8 = 408.3*10^6
$$

![](https://i.imgur.com/ejcLsKE.png)

$$
k_{Rl} \approx 2.3
$$

$$
\frac{x_m}{l_f} = \frac{95ft}{230ft} = 0.413
$$

$$
\frac{l_f^2}{S_{fs}} = \frac{(230ft)^2}{5075 ft^2} = 10.42 \approx 10
$$

$$
\sqrt{\frac{h_1}{h_2}} = \sqrt{\frac{24ft}{17ft}} = 1.188 \approx 1.2
$$

$$
\frac{h}{w_f} = \frac{28ft}{22ft} = 1.273 \approx 1
$$

![](https://i.imgur.com/0KQ2lzl.png)

$$
k_n \approx 0.0011
$$

$$
C_{n_{\beta_{wf}}} = -k_n k_{Rl} \frac{S_{fs} l_f}{S b} \quad (\text{in} ~ \deg^{-1})
$$

$$
C_{n_{\beta_{wf}}} = -0.0011 * 2.3 * \frac{5075 ft^2 * 230ft}{5500ft^2 * 195.68ft} = -0.002744\deg^{-1} = -0.15722 rad^{-1}
$$

$$
V_v = \frac{S_v l_v}{S b} = \frac{900ft^2 * 105ft}{5500ft^2 * 195.68ft} = 0.08781
$$

$$
C_{n_\beta} = C_{n_{\beta_{wf}}} + \eta_v V_v C_{L_{\alpha_v}} \left( 1 + \frac{d \sigma}{d \beta} \right)
$$

$$
C_{n_\beta} = -0.15722 + 0.08781 * 4.32 * 1.182 = \boxed{0.2912 rad^{-1}}
$$
