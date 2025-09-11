import numpy as np
import pint
import matplotlib.pyplot as plt
import random

ur = pint.UnitRegistry()

b = 6 * ur.inch
h = 1 * ur.inch

A1 = b * h
A2 = h * b

y1 = b + (1 / 2) * h
y2 = (1 / 2) * b
y_bar = (A1 * y1 + A2 * y2) / (A1 + A2)

d1 = y1 - y_bar
d2 = y2 - y_bar

I1 = (b * h**3) / 12
I2 = (h * b**3) / 12
I = I1 + A1 * d1**2 + I2 + A2 * d2**2


ys = np.linspace(0, b.magnitude, 100) * ur.inch


def sigma_over_M(c):
    return c / I


def Q(y):
    y = y.magnitude
    _h = h.magnitude
    _b = b.magnitude
    _y_bar = y_bar.magnitude

    if y < 0:
        y = -y
        height_2 = _y_bar - y
        _A2 = _h * height_2
        _d2 = y + height_2 / 2
        return _A2 * _d2
    elif 0 <= y < _b - _y_bar:
        height_2 = y
        _A2 = _h * height_2
        _d2 = height_2 / 2
        height_1 = _h
        _A1 = height_1 * _b
        _d1 = height_2 + height_1 / 2
        return _A2 * _d2 + _A1 * _d1
    else:
        height_1 = _h + _b - _y_bar - y
        _A1 = height_1 * _b
        _d1 = (height_1) / 2 + y
        return _A1 * _d1


def tau_over_V(y):
    return Q(y) / (I * b)


sigma_over_Ms = sigma_over_M(ys - y_bar)

plt.plot(sigma_over_Ms.magnitude, ys.magnitude)
plt.xlabel(r"$\sigma(x) / M$")
plt.ylabel("y (inches)")
plt.grid(axis="both")
plt.show()

plt.plot([Q(y - y_bar) for y in ys], ys - y_bar)
plt.xlabel(r"$\tau(x) / V$")
plt.ylabel("y (inches)")
plt.grid(axis="both")
plt.show()
