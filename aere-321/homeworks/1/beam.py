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


xs = np.linspace(0, L, 1000)
Ms = M(xs)
ys = y(xs)

min_M = np.min(Ms / W)
min_M_x = xs[np.argmin(Ms / W)]
max_M = np.max(Ms / W)
max_M_x = xs[np.argmax(Ms / W)]

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

ax1.plot(xs, Ms / W, color="tab:blue")
ax1.annotate("End moment constraint", xy=(0, 0), color="tab:blue")
ax1.annotate("End moment constraint", xy=(84, 0), color="tab:blue")
ax1.annotate(
    f"Max negative moment ({min_M_x: 0.2f}, {min_M: 0.2f})",
    xy=(min_M_x, min_M),
    color="tab:blue",
)
ax1.annotate(
    f"Max positive moment ({max_M_x: 0.2f}, {max_M: 0.2f})",
    xy=(max_M_x, max_M),
    color="tab:blue",
)
ax1.set_ylabel("M(x) / W")
ax1.axhline(0, color="k", lw=0.8)
ax1.grid(True)

ax2.plot(xs, ys / W, color="tab:red")
ax2.annotate("Pin constraint", xy=(0, 0), color="tab:red")
ax2.annotate("Roller constraint", xy=(42, 0), color="tab:red")
ax2.annotate("Roller constraint", xy=(84, 0), color="tab:red")
ax2.set_xlabel("x")
ax2.set_ylabel("y(x) / W")
ax2.axhline(0, color="k", lw=0.8)
ax2.grid(True)

fig.tight_layout()
plt.show()
