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
A41 = (1 / 2) * w * 2 * r + math.pi * r**2
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
epsilon = 75.19911184307752 centimeter
```

Transcribing that onto a drawing:

![](https://i.imgur.com/9yAqZod.png)

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
