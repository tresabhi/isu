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

Putting them together was fairly simple. The part where I had to be careful was applying the boundary conditions to the first and last rows of the matrix and now override them with the `for` loop. Nevertheless, here's what I came up with:

```py
import numpy as np
import matplotlib.pyplot as plt

lambda_ = 2.0
mu = 0.2

t1 = 0.1

delta_x = 0.1
delta_t = 0.01

xs = np.arange(0, 1 + delta_x, delta_x)

t = 0
Us = -5 * xs**2 + 5


def make_A():
    A = np.zeros((len(xs), len(xs)))

    # coefficients from first boundary condition
    A[0, 0] = 1

    # coefficients from second boundary condition
    A[-1, 8] = 1
    A[-1, 9] = -2
    A[-1, 10] = 1

    # start from second index till second last index to avoid overriding
    # boundary conditions
    for i in range(1, len(xs) - 1):
        A[i, i - 1] = -mu / (delta_x**2)
        A[i, i] = 1 / delta_t + (2 * mu) / (delta_x**2)
        A[i, i + 1] = -mu / (delta_x**2)

    return A


def make_B(Us):
    b = np.zeros((len(xs), 1))

    # first condition
    b[0, 0] = 5

    # second conditions (I know they're all 0 by default but I wanted to be
    # explicit about the fact that I DID consider the second one too here)
    b[-1, 0] = 0

    for i in range(1, len(xs) - 1):
        b[i, 0] = (1 / delta_t + lambda_ / delta_x) * Us[i] - (lambda_ / delta_x) * Us[
            i + 1
        ]

    return b


# A is constant I just realized lol, let's avoid recomputing it every time
A = make_A()

print(A)

# I tried doing a while loop for t < t1 but due to floating point issues it
# would often go over t1, so imma just use a step counter instead

step = 0
steps = int(t1 / delta_t)

while step < steps:
    B = make_B(Us)
    Us = np.linalg.solve(A, B).flatten()
    t += delta_t
    step += 1

print(f"final t = {t}")

plt.plot(xs, Us, marker="o")

plt.xlabel("x")
plt.ylabel("U")
plt.title(f"U vs x at t = {t:.2f}")

plt.grid()
plt.show()

```

The $A$ matrix that it produced:

```py
[[  1.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.]
 [-20. 140. -20.   0.   0.   0.   0.   0.   0.   0.   0.]
 [  0. -20. 140. -20.   0.   0.   0.   0.   0.   0.   0.]
 [  0.   0. -20. 140. -20.   0.   0.   0.   0.   0.   0.]
 [  0.   0.   0. -20. 140. -20.   0.   0.   0.   0.   0.]
 [  0.   0.   0.   0. -20. 140. -20.   0.   0.   0.   0.]
 [  0.   0.   0.   0.   0. -20. 140. -20.   0.   0.   0.]
 [  0.   0.   0.   0.   0.   0. -20. 140. -20.   0.   0.]
 [  0.   0.   0.   0.   0.   0.   0. -20. 140. -20.   0.]
 [  0.   0.   0.   0.   0.   0.   0.   0. -20. 140. -20.]
 [  0.   0.   0.   0.   0.   0.   0.   0.   1.  -2.   1.]]
```

And the plot that this makes:

![](https://i.imgur.com/AgK7VCs.png)
