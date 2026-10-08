# AERE 463 Homework 3

I am going to transcribe things into here so I can transform them into Python easier. Aero solver:

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

Forces:

$$
L = 10 (\Gamma_0 + \Gamma_1)
$$

$$
D = \Gamma_0 \sin \theta_0 + \Gamma_1 \sin \theta_1
$$

Stress:

$$
\sigma = (d_0 + d_1) * 10^4
$$

Objective function:

$$
f = D
$$

Constraints:

$$
L - 1 = 0
$$

$$
\sigma - 1 \le 0
$$

Initial design variables:

$$
\theta = [0.1, 0.1]^T
$$

$$
t = [1, 1]^T
$$
