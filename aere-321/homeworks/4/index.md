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
\bar{v} = \frac{wl * l/2 + wl * (l + w/2)}{2wl} = \frac{l/2 + l + w/2}{2}
$$

$$
\bar{v} = \frac{200mm/2 + 200mm + 50mm/2}{2} = 162.5 mm
$$

This gives me the position of the origin in relation to the edge of the stem:

![](https://i.imgur.com/NjJD6cr.png)

This allows me to get the inertia about the $z$ axis:

$$
I_z = wl^3 + wl * (l/2 - \bar{v})^2 + lw^3 + lw * (l - \bar{v} + w/2)^2
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

Smells like a job for a computer for which I came up with a fairly trivial Python code:

```python
import pint
from math import sin, cos

ur = pint.UnitRegistry()

N = ur.N
m = ur.m
kN = 1000 * N
deg = ur.deg
mm = ur.mm
MPa = ur.MPa

l = 200 * mm
w = 50 * mm

M = 2 * kN * m
theta = 60 * deg

M_y = M * sin(theta)
M_z = M * cos(theta)

v_bar = (l / 2 + l + w / 2) / 2
I_y = w * l**3 + l * w**3
I_z = (
    w * l**3
    + w * l * (l / 2 - v_bar) ** 2
    + l * w**3
    + l * w * (l - v_bar + w / 2) ** 2
)


def sigma_x(z, y):
    return (M_y / I_y) * z - (M_z / I_z) * y


sigma_x_A = sigma_x(l / 2, w + l - v_bar).to(MPa)
sigma_x_B = sigma_x(-l / 2, w + l - v_bar).to(MPa)
sigma_x_C = sigma_x(l / 2, l - v_bar).to(MPa)
sigma_x_D = sigma_x(-l / 2, l - v_bar).to(MPa)
sigma_x_E = sigma_x(w / 2, l - v_bar).to(MPa)
sigma_x_F = sigma_x(-w / 2, l - v_bar).to(MPa)
sigma_x_G = sigma_x(w / 2, -v_bar).to(MPa)
sigma_x_H = sigma_x(-w / 2, -v_bar).to(MPa)

print(f"sigma_x_A = {sigma_x_A}")
print(f"sigma_x_B = {sigma_x_B}")
print(f"sigma_x_C = {sigma_x_C}")
print(f"sigma_x_D = {sigma_x_D}")
print(f"sigma_x_E = {sigma_x_E}")
print(f"sigma_x_F = {sigma_x_F}")
print(f"sigma_x_G = {sigma_x_G}")
print(f"sigma_x_H = {sigma_x_H}")
```

This results in the following output:

```
sigma_x_A = 0.2336283230085337 megapascal
sigma_x_B = -0.5814544099650556 megapascal
sigma_x_C = 0.33300720499611136 megapascal
sigma_x_D = -0.4820755279774779 megapascal
sigma_x_E = 0.02735118013101541 megapascal
sigma_x_F = -0.17641950311238191 megapascal
sigma_x_G = 0.42486670808132604 megapascal
sigma_x_H = 0.22109602483792873 megapascal

Maximum magnitude of sigma_x = 0.5814544099650556 megapascal
```

This, the maximum compressive stress occurs at point B with $\sigma_{xB} = -0.5815MPa$ and the maximum tensile stress occurs at point G with $\sigma_{xG} = 0.4249MPa$.

## 2.

From the last question, I know what the maximum tensile stress happens at point G and vice versa at point B. Thus, I can set the equations equal to each other:

$$
\sigma_{max} = \sigma_{xG} = 4MPa
$$

$$
\sigma_{min} = \sigma_{xB} = -6MPa
$$

Expressions for $\sigma_{xB}$ and $\sigma_{xG}$:

$$
\sigma_{xB} = \frac{M_y}{I_y} (-l / 2) - \frac{M_z}{I_z} (w + l - \bar{v})
$$

$$
\sigma_{xG} = \frac{M_y}{I_y} (w / 2) - \frac{M_z}{I_z} (-\bar{v})
$$

Of course $M_y$ and $M_z$ are functions of $M$ and $\theta$, where $\theta = 60\degree$:

$$
\sigma_{xB} = \frac{M \sin \theta}{I_y} (-l / 2) - \frac{M \cos \theta}{I_z} (w + l - \bar{v})
$$

$$
\sigma_{xG} = \frac{M \sin \theta}{I_y} (w / 2) - \frac{M \cos \theta}{I_z} (-\bar{v})
$$

That's 2 equations and 1 known. But that's nothing to worry, I will simply get 2 solutions, and I pick the lower one. Solving for $M$ from each is easy:

$$
\sigma_{xB} = M \left( \frac{\sin \theta}{I_y} (-l / 2) - \frac{\cos \theta}{I_z} (w + l - \bar{v}) \right)
$$

$$
\sigma_{xG} = M \left( \frac{\sin \theta}{I_y} (w / 2) - \frac{\cos \theta}{I_z} (-\bar{v}) \right)
$$

Finally:

$$
M = \frac{\sigma_{xB}}{\frac{\sin \theta}{I_y} (-l / 2) - \frac{\cos \theta}{I_z} (w + l - \bar{v})}
$$

$$
M = \frac{\sigma_{xG}}{\frac{\sin \theta}{I_y} (w / 2) - \frac{\cos \theta}{I_z} (-\bar{v})}
$$

M from B:

$$
M = \frac{-6MPa}{\frac{\sin 60\degree}{4.25*10^{-4}m^4} (-200mm / 2) - \frac{\cos 60\degree}{4.891*10^8mm^4} (50mm + 200mm - 162.5 mm)} = 20.46 kN m
$$

M from G:

$$
M = \frac{4MPa}{\frac{\sin 50\degree}{4.25*10^{-4}m^4} (50mm / 2) - \frac{\cos 60\degree}{4.891*10^8mm^4} (- 162.5 mm)} = 18.94 kN m
$$

Thus, the maximum moment is:

$$
\boxed{M_{max} = 18.94 kN * m}
$$

## 3.

![](https://i.imgur.com/Xt8IdjV.png)

Everything here is a function of $y$ here, measured from the neutral surface, something not given. The beam can be segmented into 5 segments, all $10mm$ by $40mm$:

![](https://i.imgur.com/pTAPJZM.png)

The temporary coordinate system:

![](https://i.imgur.com/zpSmhfN.png)

This time I will be using $b$ and $h$ instead of $l$ and $w$ like last problem because sometimes, personally speaking, it got a bit ambiguous which is the smaller dimension.

$$
h = 40mm
$$

$$
b = 10mm
$$

$$
\bar{v} = \frac{2bh * (b/2) + bh * (b + h - b/2) + 2bh * (b + h/2)}{5bh}
$$

$$
\bar{v} = \frac{2(b/2) + (b + h - b/2) + 2(b + h/2)}{5}
$$

$$
\bar{v} = \frac{2(10mm/2) + (10mm + 40mm - 10mm/2) + 2(10mm + 20mm/2)}{5} = 19mm
$$

![](https://i.imgur.com/fbeTSog.png)

The value for $I = I_x$ can also be calculated now. The bottom two segments:

$$
I_A = 2hb^3 + 2bh * (\bar{v} - b/2)^2
$$

The top segment in the middle:

$$
I_B = hb^3 + bh * (b + h - b/2 - \bar{v})^2
$$

The two vertical segments on the side:

$$
I_C = 2bh^3 + 2bh * (b + h/2 - \bar{v})^2
$$

All together:

$$
I = I_A + I_B = I_C
$$

$$
I = 2hb^3 + 2bh * (\bar{v} - b/2)^2 + hb^3 + bh * (b + h - b/2 - \bar{v})^2 + 2bh^3 + 2bh * (b + h/2 - \bar{v})^2
$$

$$
I = 259 cm^4
$$

Finally, it's time to get the shear flows, starting with the top segment with :

![](https://i.imgur.com/JnI1Imm.png)

$$
q_1 = \frac{V}{I} Q_1 = \frac{V}{I} \bar{y}' A' = \frac{V}{I} (b + h + b/2 - \bar{v}) (bx)
$$

$$
\boxed{q_1 = \frac{V}{I} \left( \frac{3}{2}b + h - \bar{v} \right) b x}
$$

The vertical segment's local coordinate system has $x$ starting from the top, going down to the middle of the bottom segment:

![](https://i.imgur.com/Gxo5r99.png)

$$
Q_2 = (b + h + b/2 - \bar{v}) * (b + h)h + 2 * (b + h + b/2 - \bar{v} - x/2) * bx
$$

$$
Q_2 = \left( \frac{3}{2}b + h - \bar{v} \right) (b + h)h + 2 \left( \frac{3}{2}b + h - \bar{v} - \frac{x}{2} \right) bx
$$

$$
q_2 = \frac{V}{I} Q_2
$$

$$
\boxed{q_2 = \frac{V}{I} \left[ \left( \frac{3}{2}b + h - \bar{v} \right) (b + h)h + 2 \left( \frac{3}{2}b + h - \bar{v} - \frac{x}{2} \right) bx \right]}
$$
