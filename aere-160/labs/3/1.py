# %%

import numpy as np
import pint
from matplotlib import pyplot as plt

ur = pint.UnitRegistry()

ur.define("dollar = [currency]")
ur.define("dollars = dollar")

dollars_0 = 2000.0 * ur.dollars
s = 5000 * ur.dollars / ur.year
r = 0.02 / ur.year

dt = 0.1 * ur.year
t = np.arange(0, 30, dt.to(ur.year).magnitude) * ur.year

dollars_history = np.zeros(len(t)) * ur.dollars

dollars = dollars_0
for index in range(len(t)):
  dollars_history[index] = dollars
  d_dollars = (r * dollars + s) * dt
  dollars += d_dollars

plt.figure()
plt.plot(t.to(ur.year).magnitude, dollars_history.to(
    ur.dollars).magnitude / 1000, '--')

math_class_formula = s * (np.exp(r * t) - 1) / r + dollars_0 * np.exp(r * t)

plt.plot(t.to(ur.year).magnitude, math_class_formula.to(
    ur.dollars).magnitude / 1000, ':')
plt.xlabel('Time (years)')
plt.ylabel('Total savings (thousands of dollars)')
plt.legend(('Calculated by numerical integration', 'Math class formula'))
