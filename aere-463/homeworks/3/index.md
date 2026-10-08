# AERE 463 Homework 3

Aero solver:

$$
\begin{bmatrix}
  (\theta_0 + d_0)^2 + 3 & 1 \\
  1 & (\theta_1 + d_1)^2 + 5
\end{bmatrix} \begin{bmatrix}
  \Gamma_0 \\
  \Gamma_1
\end{bmatrix} = \begin{bmatrix}
  \theta_0 + d_0 \\
  \theta_1 + d_1
\end{bmatrix}
$$

Structural solver:

$$
\begin{bmatrix}
  10 t_0 - \theta_0 & 1 \\
  1 & 10 t_1 - \theta_1
\end{bmatrix} \begin{bmatrix}
  d_0 \\
  d_1
\end{bmatrix} = \begin{bmatrix}
  \Gamma_0^2 \\
  \Gamma_1^2
\end{bmatrix}
$$
