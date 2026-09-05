# AERE 463 Homework 1

Domain:

![](https://i.imgur.com/glv3gZg.png)

Governing equation:

$$
\frac{\partial U}{\partial t} + \lambda \frac{\partial U}{\partial x} - \mu \frac{\partial^2 U}{\partial x^2} = 0
$$

Constants:

$$
\lambda = 2.0
$$

$$
\mu = 0.2
$$

Range:

$$
x \in [0.0, 1.0]
$$

Boundary conditions:

$$
U_0 = 5.0
$$

$$
U_{10} = 2 U_9 - U_8
$$

Initial condition:

$$
U(x, t = 0) = -5x^2 + 5
$$

Target:

$$
t = 0.1
$$

Discretization:

$$
\Delta t = 0.01
$$

$$
\Delta x = 0.1
$$

$$
\frac{U_i^{n + 1} - U_i^n}{\Delta t} + \lambda \frac{U_{i + 1}^n - U_i^n}{\Delta x} - \mu \frac{U_{i + 1}^{n + 1} - 2 U_i^{n + 1} + U_{i - 1}^{n + 1}}{\Delta x^2} = 0
$$

Distributed:

$$
\frac{1}{\Delta t} U_i^{n + 1} - \frac{1}{\Delta t} U_i^n + \frac{\lambda}{\Delta x} U_{i + 1}^n - \frac{\lambda}{\Delta x} U_i^n - \frac{\mu}{\Delta x^2} U_{i + 1}^{n + 1} + \frac{2 \mu}{\Delta x^2} U_i^{n + 1} - \frac{\mu}{\Delta x^2} U_{i - 1}^{n + 1} = 0
$$

Grouped:

$$
- \frac{\mu}{\Delta x^2} U_{i - 1}^{n + 1} + \left( \frac{1}{\Delta t} + \frac{2 \mu}{\Delta x^2} \right) U_i^{n + 1} - \frac{\mu}{\Delta x^2} U_{i + 1}^{n + 1} = \left( \frac{1}{\Delta t} + \frac{\lambda}{\Delta x} \right) U_i^n - \frac{\lambda}{\Delta x} U_{i + 1}^n
$$

That should be enough to fill out the $9$ out of $11$ equations in the matrix. I do not have the willpower to write out all the equations just to shove them into a matrix in $\LaTeX$. So, I'll automate the matrix in the code.

Rewriting the boundary conditions to be easier to put into the matrix:

$$
U_0 = 5.0
$$

$$
U_8 - 2 U_9 + U_{10} = 0
$$
