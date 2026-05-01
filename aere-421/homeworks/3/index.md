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
A_1 = 600mm^2
$$

$$
A_2 = 300mm^2
$$

$$
L_1 = 500mm
$$

$$
L_2 = 350mm
$$

$$
\rho = 2850 kg/m^3
$$

$$
E = 70GPa
$$

Expanding the $\alpha$'s:

$$
\alpha_1 = \frac{A_1 E}{L_1} = \frac{600mm^2 * 70GPa}{500mm} = 8.4×10^7 N/m
$$

$$
\alpha_2 = \frac{A_2 E}{L_2} = \frac{300mm^2 * 70GPa}{350mm} = 6×10^7 N/m
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

Substitutions:

$$
u_2 = \bar{u}_2 \cos \omega t
$$

$$
u_3 = \bar{u}_3 \cos \omega t
$$

$$
\ddot{u}_2 = -\omega^2 \bar{u}_2 \cos \omega t
$$

$$
\ddot{u}_3 = -\omega^2 \bar{u}_3 \cos \omega t
$$

Putting them in:

$$
\frac{\rho}{6} \begin{bmatrix}
  2 L_1 A_1 + 2 L_2 A_2 & A_2 L_2 \\
  A_2 L_2 & 2 A_2 L_2
\end{bmatrix} \begin{bmatrix}
  -\omega^2 \bar{u}_2 \cos \omega t \\
  -\omega^2 \bar{u}_3 \cos \omega t
\end{bmatrix} + \begin{bmatrix}
  \alpha_1 + \alpha_2 & -\alpha_2 \\
  -\alpha_2 & \alpha_2
\end{bmatrix} \begin{bmatrix}
  \bar{u}_2 \cos \omega t \\
  \bar{u}_3 \cos \omega t
\end{bmatrix} = \begin{bmatrix}
  0 \\
  0
\end{bmatrix}
$$

Pulling out the cosine:

$$
\frac{\rho}{6} \begin{bmatrix}
  2 L_1 A_1 + 2 L_2 A_2 & A_2 L_2 \\
  A_2 L_2 & 2 A_2 L_2
\end{bmatrix} \begin{bmatrix}
  -\omega^2 \bar{u}_2 \\
  -\omega^2 \bar{u}_3
\end{bmatrix} \cos \omega t + \begin{bmatrix}
  \alpha_1 + \alpha_2 & -\alpha_2 \\
  -\alpha_2 & \alpha_2
\end{bmatrix} \begin{bmatrix}
  \bar{u}_2 \\
  \bar{u}_3
\end{bmatrix} \cos \omega t = 0
$$

$$
\frac{\rho}{6} \begin{bmatrix}
  2 L_1 A_1 + 2 L_2 A_2 & A_2 L_2 \\
  A_2 L_2 & 2 A_2 L_2
\end{bmatrix} \begin{bmatrix}
  -\omega^2 \bar{u}_2 \\
  -\omega^2 \bar{u}_3
\end{bmatrix} + \begin{bmatrix}
  \alpha_1 + \alpha_2 & -\alpha_2 \\
  -\alpha_2 & \alpha_2
\end{bmatrix} \begin{bmatrix}
  \bar{u}_2 \\
  \bar{u}_3
\end{bmatrix} = 0
$$

Pulling out the $\omega$:

$$
-\omega^2 \frac{\rho}{6} \begin{bmatrix}
  2 L_1 A_1 + 2 L_2 A_2 & A_2 L_2 \\
  A_2 L_2 & 2 A_2 L_2
\end{bmatrix} \begin{bmatrix}
  \bar{u}_2 \\
  \bar{u}_3
\end{bmatrix} + \begin{bmatrix}
  \alpha_1 + \alpha_2 & -\alpha_2 \\
  -\alpha_2 & \alpha_2
\end{bmatrix} \begin{bmatrix}
  \bar{u}_2 \\
  \bar{u}_3
\end{bmatrix} = 0
$$

$$
-\omega^2 \frac{\rho}{6} \begin{bmatrix}
  2 L_1 A_1 + 2 L_2 A_2 & A_2 L_2 \\
  A_2 L_2 & 2 A_2 L_2
\end{bmatrix} + \begin{bmatrix}
  \alpha_1 + \alpha_2 & -\alpha_2 \\
  -\alpha_2 & \alpha_2
\end{bmatrix} = 0
$$

The second matrix, I have numbers for in base units:

$$
\begin{bmatrix}
  \alpha_1 + \alpha_2 & -\alpha_2 \\
  -\alpha_2 & \alpha_2
\end{bmatrix} = \begin{bmatrix}
  8.4 + 6 & -6 \\
  -6 & 6
\end{bmatrix} ×10^7 N/m = \begin{bmatrix}
  14.8 & -6 \\
  -6 & 6
\end{bmatrix} ×10^7 N/m
$$

The first matrix:

$$
\frac{\rho}{6} \begin{bmatrix}
  2 L_1 A_1 + 2 L_2 A_2 & A_2 L_2 \\
  A_2 L_2 & 2 A_2 L_2
\end{bmatrix}
$$

$$
\frac{\rho}{6} 2 L_1 A_1 = \frac{2850 kg/m^3}{6} * 2 * 500mm * 600mm^2 = 0.285 kg
$$

$$
\frac{\rho}{6} 2 L_2 A_2 = \frac{2850 kg/m^3}{6} * 2 * 350mm * 300mm^2 = 0.09975 kg
$$

$$
\frac{\rho}{6} 2 L_1 A_1 + \frac{\rho}{6} 2 L_2 A_2 = 0.285 kg + 0.09975 kg = 0.3848 kg
$$

$$
\frac{\rho}{6} A_2 L_2 = \frac{2850 kg/m^3}{6} * 350mm * 300mm^2 = 0.04988 kg
$$

$$
\frac{\rho}{6} \begin{bmatrix}
  2 L_1 A_1 + 2 L_2 A_2 & A_2 L_2 \\
  A_2 L_2 & 2 A_2 L_2
\end{bmatrix} = \begin{bmatrix}
  0.3848 & 0.04988 \\
  0.04988 & 0.04988
\end{bmatrix} kg
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

$$
$$
