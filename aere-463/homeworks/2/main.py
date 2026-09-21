import numpy as np
import matplotlib.pyplot as plt

lambda_ = 2.0
mu = 0.2

t1 = 0.1

delta_x = 0.1
delta_t = 0.01
steps = int(t1 / delta_t)

Vs_final = np.array(
    [5.000, 5.009, 5.045, 5.119, 5.231, 5.371, 5.522, 5.670, 5.800, 5.904, 6.008]
)

xs = np.arange(0, 1 + delta_x, delta_x)


def make_A():
    A = np.zeros((len(xs), len(xs)))

    # coefficients from first boundary condition
    A[0, 0] = 1

    # coefficients from second boundary condition
    A[-1, 8] = 1
    A[-1, 9] = -2
    A[-1, 10] = 1

    # start from second index till second last index to avoid overriding
    # boundary conditions
    for i in range(1, len(xs) - 1):
        A[i, i - 1] = -mu / (delta_x**2)
        A[i, i] = 1 / delta_t + (2 * mu) / (delta_x**2)
        A[i, i + 1] = -mu / (delta_x**2)

    return A


def make_B(Us):
    b = np.zeros((len(xs), 1))

    # first condition
    b[0, 0] = 5

    # second conditions (I know they're all 0 by default but I wanted to be
    # explicit about the fact that I DID consider the second one too here)
    b[-1, 0] = 0

    for i in range(1, len(xs) - 1):
        b[i, 0] = (1 / delta_t + lambda_ / delta_x) * Us[i] - (lambda_ / delta_x) * Us[
            i + 1
        ]

    return b


A = make_A()


def propagate(Us_initial):
    Us = Us_initial.copy()

    step = 0
    t = 0

    while step < steps:
        B = make_B(Us)
        Us = np.linalg.solve(A, B).flatten()
        t += delta_t
        step += 1

    return Us


def f(Us_initial):
    Us = propagate(Us_initial)
    return np.sum((Us - Vs_final) ** 2)


dU = 1e-5
dG = 1e-5


def gradient(Us):
    grad = np.zeros_like(Us, dtype=float)

    for idx in np.ndindex(Us.shape):
        Us_plus = Us.copy()
        Us_minus = Us.copy()

        Us_plus[idx] += dU
        Us_minus[idx] -= dU

        grad[idx] = (f(Us_plus) - f(Us_minus)) / (2.0 * dU)

    return grad


def hessian(Us):
    original_shape = Us.shape
    x = Us.flatten()
    n = len(x)

    H = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            x_ip_jp = x.copy()
            x_ip_jm = x.copy()
            x_im_jp = x.copy()
            x_im_jm = x.copy()

            x_ip_jp[i] += dU
            x_ip_jp[j] += dU

            x_ip_jm[i] += dU
            x_ip_jm[j] -= dU

            x_im_jp[i] -= dU
            x_im_jp[j] += dU

            x_im_jm[i] -= dU
            x_im_jm[j] -= dU

            H[i, j] = (
                f(x_ip_jp.reshape(original_shape))
                - f(x_ip_jm.reshape(original_shape))
                - f(x_im_jp.reshape(original_shape))
                + f(x_im_jm.reshape(original_shape))
            ) / (4.0 * dU**2)

    return H


def line_search(Us0, d, alpha0=1.0):
    loss0 = f(Us0)
    alpha = alpha0

    for _ in range(5):
        Us1 = Us0 + alpha * d
        loss1 = f(Us1)

        if loss1 < loss0:
            return alpha

        alpha *= 0.5

    return alpha


Us = np.full(Vs_final.shape, 5.0)
iteration = 0
loss = f(Us)

for iteration in range(100):
    loss = f(Us)

    grad = gradient(Us)
    grad_norm = np.linalg.norm(grad)

    print("i:", iteration, "loss:", loss, "gradient norm:", grad_norm)

    if grad_norm < dG:
        print("optimal point found")
        break

    H = hessian(Us)
    grad_flat = grad.flatten()

    try:
        d_flat = -np.linalg.pinv(H) @ grad_flat

    except np.linalg.LinAlgError:
        print("Hessian is singular. Stopping.")
        break

    d = d_flat.reshape(Us.shape)
    alpha = line_search(Us, d, alpha0=1.0)
    Us = Us + alpha * d

print("Final loss:", f(Us))
print("Final Us:", Us)
print("Final propagated Us:", propagate(Us))
print("Iterations:", iteration)
