# %%

from matplotlib import pyplot as plt
import numpy as np

dollars = 10000
r = 0.02
dt = 0.1
s = 5000
years = 30

t = np.arange(0, years + dt, dt)
balance_history = np.zeros(len(t))

for index in range(len(t)):
  balance_history[index] = dollars
  delta_dollars = (r * dollars + s) * dt
  dollars += delta_dollars

plt.plot(t, balance_history)
plt.grid()
