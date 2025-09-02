# %%

from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0, 50.5, 0.5)
y = 5 * x + 10


plt.plot(x, y)
plt.xlabel('This is the x axis')
plt.ylabel('This is the y axis')
plt.title('This is the title')
plt.grid()
