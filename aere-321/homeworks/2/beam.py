import numpy as np
import matplotlib.pyplot as plt

L = 1


def v_324(x):
    return 2 * L * (x + L) - (x + L) ** 2


def v_321(x):
    return L**2 - x**2


x = np.linspace(-L, L, 400)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))

ax1.plot(x, v_324(x), color="tab:red")
ax1.set_title("v_324(x)")
ax1.set_ylabel("v_324(x)")
ax1.grid(True)

ax2.plot(x, v_321(x), color="tab:blue")
ax2.set_title("v_321(x)")
ax2.set_xlabel("x")
ax2.set_ylabel("v_321(x)")
ax2.grid(True)

plt.tight_layout()
plt.show()
