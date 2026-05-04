c = [1, 1, -1, -1, -1]
# c = [1, 1, -1, -1]

wi = 1
w1 = 2

epsilon = 1e-8

N = len(c) - 1
x = [0] * N


def f(x):
    global c

    y = c[0]

    for i in range(N):
        power = i + 1
        y += c[power] * x**power

    return y


y = f(x[0])

iterations = 0

while abs(y) >= epsilon:
    c_ = c[N]

    for i in range(N - 1, 0, -1):
        c_ = c_ * x[i - 1] + c[i - 2]

    x[0] = -c[0] / c_

    for i in range(2, N + 1):
        x[i - 1] = (wi * x[i - 1] + w1 * x[0]) / (wi + w1)

    y = f(x[0])

    iterations += 1
    print(f"({iterations}) f({x[0]}) = {y}")
