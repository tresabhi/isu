# AERE 421 Homework 3

Hello, grader of my homework! I am once again trying out GitHub-flavored Markdown with embedded $\LaTeX$ for my homeworks. I will be submitted my work as a PDF on Canvas but you can see the source code [here](https://github.com/tresabhi/isu/blob/main/aere-421/homeworks/3/index.md).

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

Combined matrix:

$$
\det \begin{bmatrix}
  14.8\times10^7 - \omega^2(0.38475) & -6\times10^7 - \omega^2(0.049875) \\
  -6\times10^7 - \omega^2(0.049875) & 6\times10^7 - \omega^2(0.049875)
\end{bmatrix} = 0
$$

$$
\det \begin{bmatrix}
  a & b \\
  c & d
\end{bmatrix} = ad - bc
$$

This is going to get very ugly, so I will let a symbolic solver handle the rest:

```py
import sympy

omega = sympy.Symbol("omega")

a = 14.8 * 10**7 - omega**2 * 0.38475
b = -6 * 10**7 - omega**2 * 0.049875
c = -6 * 10**7 - omega**2 * 0.049875
d = 6 * 10**7 - omega**2 * 0.049875

det = a * d - b * c

omega_solutions = sympy.solve(det, omega)

print(omega_solutions)
```

The output:

```
[-45016.4050910056, -12490.0257387210, 12490.0257387210, 45016.4050910056]
```

The negative solutions are due to the square root, so, assuming principal roots, the $\omega$ values are:

$$
\omega_1 = \boxed{12490Hz}
$$

$$
\omega_2 = \boxed{45016Hz}
$$

And to get the eigenvector, or the mode shapes, I extended the script to compute $a$, $b$, $c$, and $d$ using the first, positive solution:

```py
u1 = omega_solutions[2]

a = a.subs(omega, u1)
b = b.subs(omega, u1)
c = c.subs(omega, u1)
d = d.subs(omega, u1)

print(a, b, c, d)
```

The output:

```
87978714.1484822 -67780537.0548264 -67780537.0548264 52219462.9451736
```

That's:

$$
a = 87978714.1484822
$$

$$
b = -67780537.0548264
$$

$$
c = -67780537.0548264
$$

$$
d = 52219462.9451736
$$

$$
\begin{bmatrix}
  a & b \\
  c & d
\end{bmatrix} \begin{bmatrix}
  \bar{u}_2 \\
  \bar{u}_3
\end{bmatrix} = 0
$$

Setting $\bar{u}_3 = 1$:

$$
\begin{bmatrix}
  a & b \\
  c & d
\end{bmatrix} \begin{bmatrix}
  \bar{u}_2 \\
  1
\end{bmatrix} = 0
$$

$$
a \bar{u}_2 + b = 0
$$

$$
\bar{u}_2 = -b / a = 67780537.0548264 / 87978714.1484822 = 0.7704
$$

So for $\omega_1$, that's:

$$
\begin{bmatrix}
  \bar{u}_2 \\
  \bar{u}_3 \\
\end{bmatrix} = \boxed{\begin{bmatrix}
  0.7704 \\
  1 \\
\end{bmatrix}}
$$

Extending the script for the second frequency:

```py
a = a.subs(omega, u1)
b = b.subs(omega, u1)
c = c.subs(omega, u1)
d = d.subs(omega, u1)

print(a, b, c, d)
```

The output:

```
-631686920.835412 -161070526.774961 -161070526.774961 -41070526.7749609
```

From the same logic as above:

$$
\bar{u}_2 = 161070526.774961 / -631686920.835412 = -0.2550
$$

$$
\begin{bmatrix}
  \bar{u}_2 \\
  \bar{u}_3 \\
\end{bmatrix} = \boxed{\begin{bmatrix}
  -0.2550 \\
  1 \\
\end{bmatrix}}
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
