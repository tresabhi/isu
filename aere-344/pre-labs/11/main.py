import numpy as np
import math
import matplotlib.pyplot as plt

Gamma = 2 * math.pi
r = 5 * 10**-3
nu = 10**-5

t = np.linspace(0, 10, 100)

# v_r = 0
# v_theta = (Gamma / (2 * math.pi * r)) * (1 - np.exp(-(r**2) / (4 * nu * t)))
# v = np.sqrt(v_r**2 + v_theta**2)
omega = (Gamma / (4 * math.pi * nu * t)) * np.exp(-(r**2) / (4 * nu * t))

# plt.title("Vorticity Magnitude vs Time")
# plt.xlabel("t [s]")
# plt.ylabel("v [m/s]")
# plt.plot(t, v)
# plt.grid()
# plt.show()

plt.title("Vorticity Magnitude vs Time")
plt.xlabel("t [s]")
plt.ylabel("omega [1/s]")
plt.plot(t, omega)
plt.grid()
plt.show()
