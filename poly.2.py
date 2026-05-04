# c = [1, 1, -1, -1, -1]
# c = [1, 1, -1, -1]
c = [-4, 0, 1]

epsilon = 1e-8

N = len(c) - 1
x = [0] * N


def f(x):
    global c

    y = c[0]
    x_powered = x

    for i in range(N):
        y += c[i + 1] * x_powered
        x_powered *= x

    return y


def f_(x):
    global c

    y = 0
    x_powered = 1

    for i in range(1, N + 1):
        y += i * c[i] * x_powered
        x_powered *= x

    return y


y = f(x[0])
iterations = 0

while abs(y) >= epsilon:
    c_ = c[N]

    for i in range(N - 1, 0, -1):
        c_ = c_ * x[i - 1] + c[i - 2]

    x[0] = -c[0] / c_

    for i in range(2, N + 1):
        # x[i - 1] = (
        #     x[i - 1] - f(x[i - 1]) / f_(x[i - 1]) + x[0] - f(x[0]) / f_(x[0])
        # ) / 2
        x[i - 1] = (x[i - 1] + x[0]) / 2

    y = f(x[0])

    iterations += 1
    # print(f"({iterations}) f({x[0]}) = {y}")
    print(x)

    if iterations == 3:
        break
