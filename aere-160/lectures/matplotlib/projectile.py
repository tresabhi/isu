# %%

from matplotlib import pyplot as plt
import numpy as np


v0 = 125  # initial velocity
theta = 30 * np.pi / 180  # launch angle
g = 9.8  # gravity

t = np.linspace(0, 10, 100)

# calculate the x values
x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t ** 2

plt.plot(x, y)
plt.xlabel('Horizontal distance in meters')
plt.ylabel('Vertical distance in meters')
plt.title('Path of a cannon ball')
