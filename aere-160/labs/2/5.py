# %%

from matplotlib import pyplot as plt
import numpy as np

t = 0.30
x = np.linspace(0, 1, 100)
y = 5 * t * (0.2969 * np.sqrt(x) - 0.1260 * x - 0.3516 *
             x ** 2 + 0.2843 * x ** 3 - 0.1015 * x ** 4)

plt.plot(x, y)
plt.plot(x, -y)
plt.ylim(-1, 1)
plt.grid()
plt.title("NACA 0030 Airfoil")
