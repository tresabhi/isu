import pint

ur = pint.UnitRegistry()

Sy = 4000 * ur.N
Ai = 1 * ur.cm**2
Br = Ai

w = 20 * ur.cm
h = 15 * ur.cm
d = h / 2

Ixx = 4 * Ai * d**2

y1 = y2 = -d
y3 = y4 = d

q12 = -(Sy / Ixx) * (Br * y1)
q23 = q34 = q12

A312 = (1 / 2) * w * h
T = 2 * A312 * q12

epsilon = T / Sy

print(f"Ixx = {Ixx}")
print(f"q12 = {q12}")
print(f"epsilon = {epsilon}")
