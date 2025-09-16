# AERE 351 HW 2

## 1

### a.

Given:

$$
\overset{...}{x} = -4 \ddot y + 3 \dot x - 5 x + 2 y + 8 \ddot x - 2 \dot y
$$

$$
\overset{...}{y} = 5 x - 7 \dot y + 2 \ddot x
$$

Definitions:

$$
x_1 = x, \quad x_2 = \dot x = \dot x_1, \quad x_3 = \ddot x = \dot x_2
\\
y_1 = y, \quad y_2 = \dot y = \dot y_1, \quad y_3 = \ddot y = \dot y_2
$$

Substitution:

$$
\dot x_3 = -4 y_3 + 3 x_2 - 5 x_1 + 2 y_1 + 8 x_3 - 2 y_2
$$

$$
\dot y_3 = 5 x_1 - 7 y_2 + 2 x_3
$$

Definition of $z$ involving $x$ and $y$:

$$
z = \begin{bmatrix}
  x_1 \\
  x_2 \\
  x_3 \\
  y_1 \\
  y_2 \\
  y_3
\end{bmatrix}, \quad

\dot z = \begin{bmatrix}
  \dot x_1 \\
  \dot x_2 \\
  \dot x_3 \\
  \dot y_1 \\
  \dot y_2 \\
  \dot y_3
\end{bmatrix}
$$

Identities re-written:

$$
\dot x_1 = x_2
$$

$$
\dot x_2 = x_3
$$

$$
\dot x_3 = - 5 x_1 + 3 x_2 + 8 x_3 + 2 y_1 - 2 y_2 - 4 y_3
$$

$$
\dot y_1 = y_2
$$

$$
\dot y_2 = y_3
$$

$$
\dot y_3 = 5 x_1 + 2 x_3 - 7 y_2
$$

Everything put together in a matrix equation:

$$
\begin{bmatrix}
  \dot x_1 \\
  \dot x_2 \\
  \dot x_3 \\
  \dot y_1 \\
  \dot y_2 \\
  \dot y_3
\end{bmatrix} = \begin{bmatrix}
  0 & 1 & 0 & 0 & 0 & 0 \\
  0 & 0 & 1 & 0 & 0 & 0 \\
  -5 & 3 & 8 & 2 & -2 & -4 \\
  0 & 0 & 0 & 0 & 1 & 0 \\
  0 & 0 & 0 & 0 & 0 & 1 \\
  5 & 0 & 2 & 0 & -7 & 0
\end{bmatrix} \begin{bmatrix}
  x_1 \\
  x_2 \\
  x_3 \\
  y_1 \\
  y_2 \\
  y_3
\end{bmatrix}
$$

Hence:

$$
\boxed{\dot z = A z}
$$

Where:

$$
\boxed{A = \begin{bmatrix}
  0 & 1 & 0 & 0 & 0 & 0 \\
  0 & 0 & 1 & 0 & 0 & 0 \\
  -5 & 3 & 8 & 2 & -2 & -4 \\
  0 & 0 & 0 & 0 & 1 & 0 \\
  0 & 0 & 0 & 0 & 0 & 1 \\
  5 & 0 & 2 & 0 & -7 & 0
\end{bmatrix}}
$$

### b.

Given:

$$
\ddot r = \frac{\mu}{r^3} r
$$

The flattening:

$$
x_1 = x, \quad x_2 = \dot x = \dot x_1, \quad x_3 = \ddot x = \dot x_2
\\
y_1 = y, \quad y_2 = \dot y = \dot y_1, \quad y_3 = \ddot y = \dot y_2
\\
z_1 = z, \quad z_2 = \dot z = \dot z_1, \quad z_3 = \ddot z = \dot z_2
$$

The contents of $r$:

$$
r = \begin{bmatrix}
x \\
y \\
z
\end{bmatrix}
$$

Packing $r$ into a column vector:

$$
w = \begin{bmatrix}
  r \\
  \dot r
\end{bmatrix} \implies \begin{bmatrix}
  x \\
  y \\
  z \\
  \dot x \\
  \dot y \\
  \dot z
\end{bmatrix}
$$

$$
\dot w = \begin{bmatrix}
  \dot r \\
  \ddot r
\end{bmatrix} \implies \begin{bmatrix}
  \dot x \\
  \dot y \\
  \dot z \\
  \ddot x \\
  \ddot y \\
  \ddot z
\end{bmatrix} = \begin{bmatrix}
  x_2 \\
  y_2 \\
  z_2 \\
  x_3 \\
  y_3 \\
  z_3
\end{bmatrix} = \begin{bmatrix}
  x_2 \\
  y_2 \\
  z_2 \\
  \frac{\mu}{r^3} x_1 \\
  \frac{\mu}{r^3} y_1 \\
  \frac{\mu}{r^3} z_1
\end{bmatrix}
$$

Resolving $r^3$:

$$
r^3 = |r|^3 = \left( \sqrt{x^2 + y^2 + z^2} \right)^3 = (x^2 + y^2 + z^2)^{3/2}
$$

MATLAB code:

```m
r_0 = [5000; 10000; 2100];
r_dot_0 = [-5; 2; 1.5];
w_0 = [r_0; r_dot_0];

T = 4 * 60 * 60;

% the default settings for ode45 are too lax
options = odeset('RelTol', 1e-9, 'AbsTol', 1e-10);
[t, y] = ode45(@orbit, [0, T], w_0, options);

plot3(y(:, 1), y(:, 2), y(:, 3));
xlabel('x (km)');
ylabel('y (km)');
zlabel('z (km)');
grid on;

final_state = y(end, 1:3);
disp(final_state);

function dw_dt = orbit(~, w)
    % matlab complains if I declare this above like all other constants
    mu = 3.98 * 10 ^ 5;

    r = w(1:3);
    r_dot = w(4:6);
    % I am sure there's a built in function for this but I like component-wise
    r_cubed = (r(1) ^ 2 + r(2) ^ 2 + r(3) ^ 2) ^ (3/2);
    r_ddot = (-mu .* r) ./ r_cubed;

    dw_dt = [r_dot; r_ddot];
end
```

Plot:

![](https://i.imgur.com/R1R5ZOv.png)

Console output:

```
1.0e+03 *
-8.5505   -3.5230    0.4822
```
