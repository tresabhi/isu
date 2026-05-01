# AERE 421 Homework 2

## 1.

This is the frequency at which the system oscillates if there is no damping, which lets it go back and forth forever, sinusoidally.

## 2.

Natural frequency is larger than damped frequency.

## 3.

Underdamped is when damping ratio is less than 1: **True**

Critically damped is when damping ratio is greater that 1: **False**

## 4.

From the problem:

$$
A_1 = 600mm^2 = 6*10^{-4} m^2
$$

$$
A_2 = 300mm^2 = 3*10^{-4} m^2
$$

$$
L_1 = 500mm = 0.5m
$$

$$
L_2 = 350mm = 0.35m
$$

$$
\rho = 2850 kg/m^3
$$

$$
E = 70GPa = 70*10^9Pa
$$

Expanding the $\alpha$'s:

$$
\alpha_1
$$

From the hint (I am pretty sure there was a typo in the notes; the $A_2 A_2$ should've been $A_2 L_2$):

$$
\frac{\rho}{6} \begin{bmatrix}
  2 L_1 A_1 + 2 L_2 A_2 & A_2 L_2 \\
  A_2 L_2 & 2 A_2 L_2
\end{bmatrix} \begin{bmatrix}
  \ddot{u_2} \\
  \ddot{u_3}
\end{bmatrix} + \begin{bmatrix}
  \alpha_1 + \alpha_2 & -\alpha_2 \\
  -\alpha_2 & \alpha_2
\end{bmatrix} \begin{bmatrix}
  u_2 \\
  u_3
\end{bmatrix} = \begin{bmatrix}
  0 \\
  0
\end{bmatrix}
$$

## 5.

I wrote a script for Quiz 5, so I will be using it again here:

```py
import pint

ur = pint.UnitRegistry()

m = 60 * ur.kg
k = 300 * ur.N / ur.m
c = 30 * ur.N * ur.s / ur.m

Y = 50 * ur.mm
omega = 50 / ur.s

X_Y = (
    (k**2 + (c * omega) ** 2) / ((k - m * omega**2) ** 2 + (c * omega) ** 2)
) ** (1 / 2)

X = X_Y * Y

print(X)
```

The output:

```
0.5108981522063187 millimeter
```

Or, in $\LaTeX$, wit better sig-figs:

$$
\boxed{X = 0.51\text{mm}}
$$
