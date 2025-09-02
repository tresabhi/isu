# %%

from matplotlib import pyplot as plt
import numpy as np

v0 = 130
theta = 40 * np.pi / 180
g = 9.8

t = np.linspace(0, 10, 100)

x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t ** 2

plt.plot(x, y)
plt.arrow(x[0], y[0], np.cos(theta) * 15, np.sin(theta) * 15, width=15)
plt.xlabel('Horizontal distance in meters')
plt.ylabel('Vertical distance in meters')
plt.title('Path of the projectile')
