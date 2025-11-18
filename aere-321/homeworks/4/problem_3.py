import pint

ur = pint.UnitRegistry()

V = 150 * ur.N
h = 10 * ur.mm
b = 40 * ur.mm

v_bar = ((7 / 2) * b + 2 * h) / 5
I = (
    2 * h * b**3
    + 2 * b * h * (v_bar - b / 2) ** 2
    + h * b**3
    + b * h * (b + h - b / 2 - v_bar) ** 2
    + 2 * b * h**3
    + 2 * b * h * (b + h / 2 - v_bar) ** 2
)


def q_1(x):
    return (V / I) * ((3 / 2) * b + h - v_bar) * (b / 2) * x


def q_2(x):
    return (V / I) * (
        ((3 / 2) * b + h - v_bar) * (b + h) * h
        + 2 * ((3 / 2) * b + h - v_bar - x / 2) * b * x
    )


def q_3(x):
    return (
        (V / I)
        * (
            ((3 / 2) * b + h - v_bar) * (b + h) * h
            + 2 * ((3 / 2) * b + h - v_bar - (b + h) / 2) * b * (b + h)
        )
        * (1 - x / (b + h / 2))
    )


print("Joint near B:")
print("End of q_1 =", q_1(b / 2 + h / 2))
print("Start of q_2 =", q_2(0 * ur.mm))

print("\nJoint near A:")
print("End of q_2 =", q_2(b + h))
print("Start of q_3 =", q_3(0 * ur.mm))

print("\nCenter of q_1:")
print("q_1 =", q_1(0 * ur.mm))

print("\nEnd of q_3:")
print("q_3 =", q_3(b + h / 2))

print("\nB =", q_1(h / 2))
print("A =", q_1(h / 2 + b))
