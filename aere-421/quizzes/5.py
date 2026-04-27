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
