import math


def f(x):
    return math.sin(math.pi * x**2)


a = 0
b = 2
n = 4

I_exact = 0.2743355055837958535128042155760939140911560695297364317514505014912952237920376144547406645599696172


def trapezoid():
    if n <= 0:
        raise ValueError("n must be positive")

    delta_x = (b - a) / n

    I = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        I += f(a + i * delta_x)

    I *= delta_x

    return I


def homer():
    if n <= 0 or n % 2 != 0:
        raise ValueError("n must be a positive even integer for Simpson's 1/3 rule")

    delta_x = (b - a) / n

    I = f(a) + f(b)

    for i in range(1, n):
        I += (4 if i % 2 else 2) * f(a + i * delta_x)

    I *= delta_x / 3

    return I


I_trapezoid = trapezoid()
I_homer = homer()

print("Trapezoid:", I_trapezoid)
print("  Error = {:.6f}%".format(abs((I_trapezoid - I_exact) / I_exact) * 100))
print()

print("Homer:", I_homer)
print("  Error = {:.6f}%".format(abs((I_homer - I_exact) / I_exact) * 100))
print()

print("Exact:", I_exact)
