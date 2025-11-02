# AERE 321 Project 2

Much like project 1, I chose Python to solve the problem due to its $0$ based indexing and better syntax compared to MATLAB.

## Flowchart

I created the following flowchart in Figma (which you can check out here: https://www.figma.com/board/TmVnMqbOfEi4gnI4sYEOjV) to represent my code in its entirety:

![](https://i.imgur.com/P7GpY7h.png)

Here, orange represents the input, blue represents any useful console outputs or plots, and the white are the intermediate steps.

## Deformation Plot Derivation

From slide 11, I acquired the beam deflection equation:

$$
\frac{d^2y}{dx^2} = \frac{M}{EI}
$$

Integration leads to:

$$
y = \frac{1}{EI} \left( -k_{32} \frac{x^2}{2} + k_{22} \frac{x^3}{6} \right) + c_1 x + c_2
$$

And since:

$$
(x, y) = (0, 1) \And \frac{dy}{dx} = 0 \implies c_1 = 0
$$

$$
(x, y) = (L, 0) \And \frac{dy}{dx} = 0 \implies c_2 = 1
$$

Furthermore:

$$
k_{32} = \frac{6EI}{L^2}
$$

$$
k_{22} = \frac{12EI}{L^3}
$$

This makes:

$$
y(x) = -\frac{3x^2}{L^2} + \frac{2x^3}{L^3} + 1
$$

Now, at this point, I will be totally honest, I do not understand how Hermite shape functions come to play here but I followed [ACS College of Engineering's guide to beam analysis](https://www.acsce.edu.in/acsce/wp-content/uploads/2020/03/Beam-analysis-Module-3.pdf) which rewrites the equation above as:

$$
y(x) = N_1(x) v_1 + N_2(x) \theta_1 + N_3(x) v_2 + N_4(x) \theta_2
$$

And according to the Wikipedia page on [Hermite polynomials](https://en.wikipedia.org/wiki/Cubic_Hermite_spline), the functions that serve me the best are:

$$
\begin{align*}
  N_1(x) &= 1 - 3\left(\frac{x}{L}\right)^2 + 2\left(\frac{x}{L}\right)^3 \\
  N_2(x) &= x \left( 1 - 2\frac{x}{L} + \left(\frac{x}{L}\right)^2 \right) \\
  N_3(x) &= 3\left(\frac{x}{L}\right)^2 - 2\left(\frac{x}{L}\right)^3 \\
  N_4(x) &= x \left( -\frac{x}{L} + \left(\frac{x}{L}\right)^2 \right)
\end{align*}
$$

Thus, in local coordinates:

$$
u(x) = N_1(x) u_1 + N_2(x) u_2
$$

$$
v(x) = N_3(x) v_1 + N_4(x) v_2
$$

And in global, the offset coordinates are:

$$
\begin{bmatrix}
x_g \\
y_g
\end{bmatrix} = \begin{bmatrix}
x_0 \\
y_0
\end{bmatrix} + \begin{bmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta
\end{bmatrix} \begin{bmatrix}
x + u(x) \\
y(x)
\end{bmatrix}
$$
