# AERE 421 Homework 2

## 1.

This is the frequency at which the system oscillates if there is no damping, which lets it go back and forth forever, sinusoidally.

## 2.

Natural frequency is larger than damped frequency.

## 3.

Underdamped is when damping ratio is less than 1: **True**

Critically damped is when damping ratio is greater that 1: **False**

## 4.

TODO

## 5.

I wrote a script for Quiz 5, so I will be using it again here:

```py
import pint

ur = pint.UnitRegistry()

m = 60 * ur.kg
k = 300 * ur.N / ur.m
c = 30 * ur.N * ur.s / ur.m

Y = 50 * ur.mm
omega = 50 / ur.s

X_Y = (
    (k**2 + (c * omega) ** 2) / ((k - m * omega**2) ** 2 + (c * omega) ** 2)
) ** (1 / 2)

X = X_Y * Y

print(X)
```

The output:

```
0.5108981522063187 millimeter
```

Or, in $\LaTeX$, wit better sig-figs:

$$
X = 0.51\text{mm}
$$
