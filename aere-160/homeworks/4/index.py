# %%

from matplotlib import pyplot as plt
import numpy as np
import pint

ur = pint.UnitRegistry()

# F_gravity = (G * m1 * m2) / (r ** 2)
G = 6.674e-11 * ur.m ** 3 / (ur.kg * ur.s ** 2)
m_earth = 5.98e24 * ur.kg
m_object = 30500 * ur.kg
r_earth = 12700000 / 2 * ur.m
r_orbit = r_earth + (2000 * ur.km).to(ur.m)

r = np.linspace(r_earth, r_orbit, 1000)
# if it converts to ur.N, everything worked well :)
F_gravity = (G * m_earth * m_object / (r ** 2)).to(ur.N)

plt.plot(r, F_gravity)
plt.xlabel('Distance from the center of the Earth (m)')
plt.ylabel('Force of gravity (N)')
plt.title('Force of gravity on an object moving away from the center of the Earth')
plt.grid()
