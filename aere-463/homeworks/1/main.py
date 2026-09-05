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

    # second (useless, but explicit)
    b[-1, 0] = 0

    for i in range(1, len(xs) - 1):
        b[i, 0] = (1 / delta_t + lambda_ / delta_x) * Us[i] - (lambda_ / delta_x) * Us[
            i + 1
        ]

    return b


# A is constant I just realized; let's cache it
A = make_A()

# I tried doing a while loop for t < t1 but due to floating point issues it
# would often go over t1, so here's a fixed step count

step = 0
steps = int(t1 / delta_t)

while step < steps:
    B = make_B(Us)
    Us = np.linalg.solve(A, B).flatten()
    t += delta_t
    step += 1

print(f"{t=}")

plt.plot(xs, Us, marker="o")

plt.xlabel("x")
plt.ylabel("U")
plt.title(f"U vs x at t = {t:.2f}")

plt.grid()
plt.show()
