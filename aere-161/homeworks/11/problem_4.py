"""
Abhigyaan Deep AER E 161

Purpose: Plot the deflection of a beam
"""

import numpy as np
from matplotlib import pyplot as plt

# declare the variables
P = 10  # force kN
l = 8  # beam length m
I = 350e6  # moment of inertia mm^4
E = 200  # Young's Modulus GPa


# define the function
def deflection(P, l, I, E, x):
    # apply and return the formula
    return -((P * x**2) / (6 * E * I)) * (3 * l - x)


# create a range using the length itself as the ending point
x = np.arange(0, l, 0.01)
# apply the function for all x values
y = deflection(P, l, I, E, x)

# plot and add text
plt.plot(x, y)
plt.title("Beam Deflection")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.grid()
plt.show()
