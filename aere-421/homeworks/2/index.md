# AERE 421 Homework 2

## 1.

The shear center is a very important span-wise position as it is the center of rotation under load. If a force is applied anywhere other than the shear center, it will cause torsion, which is undesirable as that changes the wing's angle of attack in an unpredictable manner, throwing off dynamics, and risking failure.

Open sections are detrimental to the performance of an aircraft due to the extreme loss in shear flow, giving way to torsion, for the same reasons listed above. More over, the drag introduced to any cavities would not help endurance.

## 2.

![](https://i.imgur.com/t7s6TOGm.png)

I found it most convenient to write a consistent, reproducible Python script for this problem.

```py
import pint
import math

ur = pint.UnitRegistry()

Sy = 4 * ur.kN

r = 12 * ur.cm
w = 25 * ur.cm

Ai = 1 * ur.cm**2

di = r
y1 = y2 = r
y3 = y4 = -r

Ixx = 4 * Ai * di**2
Br = Ai

q34 = -(Sy / Ixx) * Br * y3
q41 = q34 - (Sy / Ixx) * Br * y4
q12 = q41 - (Sy / Ixx) * Br * y1

# measuring about 3
A34 = 0 * ur.m**2
A41 = (1 / 2) * w * 2 * r + (1 / 2) * math.pi * r**2
A12 = (1 / 2) * w * 2 * r

T34 = 2 * A34 * q34
T41 = 2 * A41 * q41
T12 = 2 * A12 * q12

T = T34 + T41 + T12
epsilon = T / Sy

q34 = q34.to(ur.N / ur.mm)
q41 = q41.to(ur.N / ur.mm)
q12 = q12.to(ur.N / ur.mm)
epsilon = epsilon.to(ur.cm)

print(f"q34 = {q34}")
print(f"q41 = {q41}")
print(f"q12 = {q12}")
print(f"epsilon = {epsilon}")
```

And the output:

```
q34 = 8.333333333333332 newton / millimeter
q41 = 16.666666666666664 newton / millimeter
q12 = 8.333333333333332 newton / millimeter
epsilon = 56.34955592153876 centimeter
```

Transcribing that onto a drawing:

![](https://i.imgur.com/Dn8pm74.png)

## 3.

I am making a cut here:

![](https://i.imgur.com/BIut23jm.png)

And the area of $A_{25}$ in my code is found by subtracting these two triangles:

![](https://i.imgur.com/zv1M4ok.png)

Similarly, for $A_{53}$:

![](https://i.imgur.com/GjJ92Pw.png)

My code to implement the process, following the in-class example:

```py
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
```

The output:

```
Vy⋅ζ = 0.045238934211693⋅Vy⋅qs₀ + 0.112636109278707⋅Vy⋅(qs₀ - 4.16666666666667) + 0.06⋅Vy⋅(qs₀ - 2.08333333333333)
0 = 34.1093528101648⋅Vy⋅qs₀ + 56.3180546393536⋅Vy⋅(qs₀ - 4.16666666666667) + 30.0⋅Vy⋅(qs₀ - 2.08333333333333)

zeta = -5.67033364618427 centimeter
```

Visually, that's here:

![](https://i.imgur.com/iks3vAo.png)

## 4.

Once again, I wrote Python to speed things up a bit:

```py
import pint

ur = pint.UnitRegistry()

Sy = 4 * ur.kN

r = 12 * ur.cm
w = 25 * ur.cm
L = 1 * ur.m

Ai = 1 * ur.cm**2

y1 = y2 = r
y3 = y4 = -r
y5 = 0 * ur.m

Ixx = Ai * y1**2 + Ai * y2**2 + Ai * y3**2 + Ai * y4**2 + Ai * y5**2
M = Sy * L

sigma1 = (M * y1) / Ixx
sigma2 = (M * y2) / Ixx
sigma3 = (M * y3) / Ixx
sigma4 = (M * y4) / Ixx
sigma5 = (M * y5) / Ixx

F1 = sigma1 * Ai
F2 = sigma2 * Ai
F3 = sigma3 * Ai
F4 = sigma4 * Ai
F5 = sigma5 * Ai

F1 = F1.to(ur.kN)
F2 = F2.to(ur.kN)
F3 = F3.to(ur.kN)
F4 = F4.to(ur.kN)
F5 = F5.to(ur.kN)

print(f"F1 = {F1}")
print(f"F2 = {F2}")
print(f"F3 = {F3}")
print(f"F4 = {F4}")
print(f"F5 = {F5}")
```

The output is my answer:

```
F1 = 8.333333333333332 kilonewton
F2 = 8.333333333333332 kilonewton
F3 = -8.333333333333332 kilonewton
F4 = -8.333333333333332 kilonewton
F5 = 0.0 kilonewton
```
