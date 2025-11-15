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
