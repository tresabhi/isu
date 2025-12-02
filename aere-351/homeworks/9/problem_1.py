import numpy as np
from math import cos, sin
import pint

omega = np.deg2rad(25)
Omega = np.deg2rad(178)
i = np.deg2rad(15)

h = 250
R = 6378
r_p = R + h

mu = 3.98600 * 10**5


R = np.matrix(
    [
        [
            cos(omega) * cos(Omega) - sin(omega) * cos(i) * sin(Omega),
            -sin(omega) * cos(Omega) - cos(omega) * cos(i) * sin(Omega),
            sin(i) * sin(Omega),
        ],
        [
            cos(omega) * sin(Omega) + sin(omega) * cos(i) * cos(Omega),
            -sin(omega) * sin(Omega) + cos(omega) * cos(i) * cos(Omega),
            -sin(i) * cos(Omega),
        ],
        [sin(omega) * sin(i), cos(omega) * sin(i), cos(i)],
    ]
)

v = R * np.matrix([[1.6], [8.2], [0]])
r = R * np.matrix([[r_p], [0], [0]])

h = np.cross(v.T, r.T).T
e = np.cross(v.T, h.T).T / mu - r / r_p

print(np.linalg.norm(e))
