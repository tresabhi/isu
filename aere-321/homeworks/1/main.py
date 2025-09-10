import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

L = 84
E = 30_000
I = 55.25

W = sp.symbols("W")
A = 18.38 * W
B = 26.25 * W
C_1 = -2315.25 * W


def macaulay(x):
    return np.where(x < 0, 0, x)


def M(x):
    return (
        A * macaulay(x)
        + B * macaulay(x - 42)
        + (1 / 2) * W * (macaulay(x - 42) ** 2 - macaulay(x) ** 2)
    )


def y(x):
    return (1 / (E * I)) * (
        (1 / 6) * A * macaulay(x) ** 3
        + (1 / 6) * B * macaulay(x - 42) ** 3
        + (1 / 24) * W * (macaulay(x - 42) ** 4 - macaulay(x) ** 4)
        + C_1 * x
    )


x = np.linspace(0, L, 1000)


fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

ax1.plot(x, M(x) / W, color="tab:blue")
ax1.set_ylabel("M(x) / W")
ax1.axhline(0, color="k", lw=0.8)
ax1.grid(True)

ax2.plot(x, y(x) / W, color="tab:red")
ax2.set_xlabel("x")
ax2.set_ylabel("y(x) / W")
ax2.axhline(0, color="k", lw=0.8)
ax2.grid(True)

fig.tight_layout()
plt.show()
