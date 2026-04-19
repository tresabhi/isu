import pint
import math
import sympy

ur = pint.UnitRegistry()

Sy = 4 * ur.kN

Ai = 1 * ur.cm**2
r = 12 * ur.cm
w = 25 * ur.cm
t = 0.5 * ur.mm

l = (w**2 - r**2) ** (1 / 2)

Br = Ai
y1 = y2 = r
y3 = y4 = -r
y5 = 0 * ur.m

Ixx = Ai * y1**2 + Ai * y2**2 + Ai * y3**2 + Ai * y4**2 + Ai * y5**2

qb12 = -(1 / Ixx) * Br * y1
qb25 = qb12 - (1 / Ixx) * Br * y2
qb53 = qb25 - (1 / Ixx) * Br * y5
qb34 = qb53 - (1 / Ixx) * Br * y3
qb41 = qb34 - (1 / Ixx) * Br * y4

# about 1 again
A12 = 0 * ur.m**2
A25 = (1 / 2) * r * (w + l) - (1 / 2) * l * r
A53 = 2 * r * (w + l) - 2 * (1 / 2) * r * l - A25 - (1 / 2) * 2 * r * w
A34 = (1 / 2) * 2 * r * w
A41 = (1 / 2) * math.pi * r**2
A = (1 / 2) * math.pi * r**2 + 2 * r * w + (1 / 2) * 2 * r * l

l12 = l25 = l53 = l34 = w
l41 = (1 / 2) * 2 * math.pi * r

qb12 = qb12.to_base_units().magnitude
qb25 = qb25.to_base_units().magnitude
qb53 = qb53.to_base_units().magnitude
qb34 = qb34.to_base_units().magnitude
qb41 = qb41.to_base_units().magnitude

A12 = A12.to_base_units().magnitude
A25 = A25.to_base_units().magnitude
A53 = A53.to_base_units().magnitude
A34 = A34.to_base_units().magnitude
A41 = A41.to_base_units().magnitude
A = A.to_base_units().magnitude

l12 = l12.to_base_units().magnitude
l25 = l25.to_base_units().magnitude
l53 = l53.to_base_units().magnitude
l34 = l34.to_base_units().magnitude
l41 = l41.to_base_units().magnitude

t = t.to_base_units().magnitude
Sy = Sy.to_base_units().magnitude

qb0 = sympy.symbols("qs0")
zeta, Vy = sympy.symbols("zeta Vy")

eq_torque = sympy.Eq(
    Vy * zeta,
    (qb12 + qb0) * Vy * 2 * A12
    + (qb25 + qb0) * Vy * 2 * A25
    + (qb53 + qb0) * Vy * 2 * A53
    + (qb34 + qb0) * Vy * 2 * A34
    + (qb41 + qb0) * Vy * 2 * A41,
)

q12 = (qb12 + qb0) * Vy * 2 * A12
q25 = (qb25 + qb0) * Vy * 2 * A25
q53 = (qb53 + qb0) * Vy * 2 * A53
q34 = (qb34 + qb0) * Vy * 2 * A34
q41 = (qb41 + qb0) * Vy * 2 * A41

eq_q_sum = sympy.Eq(
    0,
    (q12 / t) * l12
    + (q25 / t) * l25
    + (q53 / t) * l53
    + (q34 / t) * l34
    + (q41 / t) * l41,
)

sympy.pretty_print(eq_torque)
sympy.pretty_print(eq_q_sum)

print()

zeta_sol = sympy.solve(eq_torque.subs(qb0, sympy.solve(eq_q_sum, qb0)[0]), zeta)[0]
zeta_sol = float(zeta_sol)
zeta_sol *= ur.m
zeta_sol = zeta_sol.to(ur.cm)

print("zeta =", zeta_sol)
