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

Eigenvalues, courtesy of MATLAB:

```m
A = [
     -2, 0, 0;
     0, 0, 1;
     -10, -15, 0;
     ];

eigenvalues = eig(A);

disp(eigenvalues)
```

Output:

```
   0.0000 + 3.8730i
   0.0000 - 3.8730i
  -2.0000 + 0.0000i
```

Eigenvalues:

$$
\lambda_{1,2} = \pm 3.8730i
$$

$$
\lambda_2 = -2
$$
