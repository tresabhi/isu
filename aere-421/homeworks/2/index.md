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
