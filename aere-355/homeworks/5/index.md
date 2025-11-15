# AERE 355 Homework 5

## 1.

Given:

$$
\dot{\alpha} + 2 \alpha - q = 0
$$

$$
\ddot{\theta} + 10 \alpha + 15 \theta = -5 \delta
$$

Substitutions:

$$
x_1 = \alpha
$$

$$
x_2 = \theta
$$

$$
x_3 = \dot{\theta}
$$

Rewriting:

$$
\dot{x}_1 + 2 x_1 - q = 0
$$

$$
\dot{x}_1 = -2 x_1 + q
$$

$$
\dot{x}_2 = x_3
$$

$$
\dot{x}_3 + 10 x_1 + 15 x_2 = -5 \delta
$$

$$
\dot{x}_3 = -10 x_1 - 15 x_2 - 5 \delta
$$

Vectors:

$$
X = \begin{bmatrix}
  x_1 \\
  x_2 \\
  x_3
\end{bmatrix}
$$

$$
U = \begin{bmatrix}
  q \\
  \delta
\end{bmatrix}
$$

$$
\dot{X} = \begin{bmatrix}
  \dot{x}_1 \\
  \dot{x}_2 \\
  \dot{x}_3
\end{bmatrix} = \begin{bmatrix}
  -2 x_1 + q \\
  x_3 \\
  -10 x_1 - 15 x_2 - 5 \delta
\end{bmatrix}
$$

$$
\dot{X} = AX + BU
$$

$$
\dot{X} = \begin{bmatrix}
  -2 & 0 & 0 \\
  0 & 0 & 1 \\
  -10 & -15 & 0
\end{bmatrix} X + \begin{bmatrix}
  1 & 0 \\
  0 & 0 \\
  0 & -5
\end{bmatrix} U
$$

And now the for the MATLAB code:

```m
A = [-2 0 0; 0 0 1; -10 -15 0];
B = [1 0; 0 0; 0 -5];
X_0 = [0; 0; 0];
U = [0; 1];

f = @(t, x) A * x + B * U;

[t, x] = ode45(f, [0, 10], X_0);

disp("Eigenvalues of A:")
disp(eig(A))

plot(t, x)
legend('\alpha', '\theta', 'd\theta/dt')
xlabel('t')
ylabel('X')
```

This results in the following eigenvalues:

```
Eigenvalues of A:
   0.0000 + 3.8730i
   0.0000 - 3.8730i
  -2.0000 + 0.0000i
```

And the following plot for a unit step in $\delta$:

![](https://i.imgur.com/PPvecTa.png)

Setting `U = [1; 0];` instead of `U = [0; 1];` shows what would happen if we had a unit step in `q` instead of `delta`:

![](https://i.imgur.com/9bdSzBu.png)

And a `U = [1; 1]` shows what would happen if we had a unit step in both `q` and `delta`:

![](https://i.imgur.com/wADtJX0.png)

The question was very ambiguous on what's being stepped to I just did all three.

## 2.

Given:

$$
a = 1116.45ft/s
$$

$$
W = 23904lb
$$

$$
I_y = 126099 slug * ft^2
$$

$$
\rho = 2.3769 * 10^{-3} slug/ft^3
$$

$$
S = 542.5ft^2
$$

$$
C_{D_0} = 0.095
$$

$$
C_{L_0} = 0.737
$$

$$
C_{D_u} = C_{L_u} = 0
$$

$$
\bar{c} = 10.93ft
$$

$$
C_{m_q} = -8.0
$$

$$
C_{m_\alpha} = -0.80
$$

$$
C_{m_{\dot{\alpha}}} = -3.0
$$

$$
C_{L_\alpha} = 5.0
$$

Preliminaries:

$$
u_0 = 0.20 * 1116.45ft/s = 223.29ft/s
$$

$$
g = 9.81m/s^2
$$

$$
m = W / g = 23904lb / 9.81m/s^2 = 742.7slug
$$

$$
Q = \frac{1}{2} \rho u_0^2 = \frac{1}{2} * 2.3769 * 10^{-3} slug/ft^3 * (223.29ft/s)^2 = 0.4115psi
$$

$$
X_u = \frac{-(C_{D_u} + 2 C_{D_0}) Q S}{m u_0} = \frac{-(0 + 2 * 0.095) * 0.4115psi * 542.5ft^2}{742.7slug * 223.29ft/s} = -0.03683s^{-1}
$$

$$
Z_u = \frac{-(C_{L_u} + 2 C_{L_0}) Q S}{u_0 m} = \frac{-(0 + 2 * 0.737) * 0.4115psi * 542.5ft^2}{223.29ft/s * 742.7slug} = -0.2857s^{-1}
$$

$$
\omega_{n_p} = \sqrt{\frac{-Z_u g}{u_0}} = \sqrt{\frac{0.2857s^{-1} * 9.81m/s^2}{223.29ft/s}} = 0.2029s^{-1}
$$

$$
M_q = C_{m_q} \frac{\bar{c}}{2 u_0} Q S \frac{\bar{c}}{I_y} = -8.0 \frac{10.93ft}{2 * 223.29ft/s} * 0.4115psi * 542.5ft^2 * \frac{10.93ft}{126099 slug * ft^2} = -0.5456s^{-1}
$$

$$
M_w = C_{m_\alpha} \frac{Q S \bar{c}}{u_0 I_y} = -0.80 \frac{0.4115psi * 542.5ft^2 * 10.93ft}{223.29ft/s * 126099 slug * ft^2} = -0.03275 m^{-1} s^{-1}
$$

$$
M_\alpha = u_0 M_w = 223.29ft/s * -0.03275 m^{-1} s^{-1} = -2.229 s^{-2}
$$

$$
Z_w = -(C_{L_\alpha} + C_{D_0}) \frac{Q S}{u_0 m} = -(5.0 + 0.095) * \frac{0.4115psi * 542.5ft^2}{223.29ft/s * 742.7slug} = -0.9876s^{-1}
$$

$$
Z_\alpha = u_0 Z_w = 223.29ft/s * -0.9876s^{-1} = -220.5 ft/s^2
$$

$$
\omega_{n_{sp}} = \sqrt{\frac{Z_\alpha M_q}{u_0} - M_\alpha} = \sqrt{\frac{-220.5 ft/s^2 * -0.5456s^{-1}}{223.29ft/s} - (-2.229 s^{-2})} = 1.6637s^{-1}
$$

$$
M_{\dot{w}} = C_{m_{\dot{\alpha}}} \frac{\bar{c}}{2 u_0} \frac{Q S \bar{c}}{u_0 I_y} = -3.0 \frac{10.93ft}{2 * 223.29ft/s} * \frac{0.4115psi * 542.5ft^2 * 10.93ft}{223.29ft/s * 126099 slug * ft^2} = -0.003006 m^{-1}
$$

$$
M_{\dot{\alpha}} = u_0 M_{\dot{w}} = 223.29ft/s * -0.003006 m^{-1} = -0.2046 s^{-1}
$$

Long period (Phugoid approximation):

$$
\zeta_p = \frac{-X_u}{2 \omega_{n_p}} = \frac{0.03683s^{-1}}{2 * 0.2029s^{-1}} = \boxed{0.09076}
$$

Short period:

$$
\zeta_{sp} = -\frac{M_q + M_{\dot{\alpha}} + \frac{Z_\alpha}{u_0}}{2 \omega_{n_{sp}}} = -\frac{-0.5456s^{-1} + -0.2046s^{-1} + \frac{-220.5 ft/s^2}{223.29ft/s}}{2 * 1.6637s^{-1}} = \boxed{0.5222}
$$
