import pint

ur = pint.UnitRegistry()

q_avg = 100 * ur.N * ur.m
d1 = 50 * ur.cm
h1 = 200 * ur.cm
dw = 20 * ur.cm
hw = 20 * ur.cm

q1 = q_avg * (1 + dw / d1)
q2 = q_avg * (1 + hw / (2 * h1))
q3 = q_avg * (1 - (dw * hw) / (d1 * h1))

print(f"q1 = {q1}")
print(f"q2 = {q2}")
print(f"q3 = {q3}")
