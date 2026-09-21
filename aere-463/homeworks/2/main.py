import numpy as np
import matplotlib.pyplot as plt

lambda_ = 2.0
mu = 0.2

t1 = 0.1

delta_x = 0.1
delta_t = 0.01
steps = int(t1 / delta_t)

Vs_final = np.array(
    [5.000, 5.009, 5.045, 5.119, 5.231, 5.371, 5.522, 5.670, 5.800, 5.904, 6.008]
)

xs = np.arange(0, 1 + delta_x, delta_x)
Us = np.full(Vs_final.shape, 5.0)


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


A = make_A()


def propagate(Us_initial):
    Us = Us_initial.copy()

    step = 0

    while step < steps:
        B = make_B(Us)
        Us = np.linalg.solve(A, B).flatten()
        t += delta_t
        step += 1

    return Us
