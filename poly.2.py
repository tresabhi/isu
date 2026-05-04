epsilon = 1e-8
# c = [1, 1, -1, -1, -1]
c = [1, 1, -1, -1]

N = len(c) - 1
x = [0] * N


def polynomial():
    global c, x

    y = c[0]

    for i in range(N):
        power = i + 1
        y += c[power] * x[i] ** power

    return y


y = polynomial()

iterations = 0

while abs(y) >= epsilon:
    c_ = c[N]

    for i in range(N - 1, 0, -1):
        c_ = c_ * x[i - 1] + c[i - 2]

    x[0] = -c[0] / c_

    for i in range(2, N + 1):
        x[i - 1] = (x[i - 1] + x[0]) / 2

    y = polynomial()

    iterations += 1
    print(iterations, y, x)
