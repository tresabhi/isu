# AERE 463 Homework 2

Objective function

$$
f = \sum_{i = 0:10} (U_i^{t = 0.1} - V_i^{t = 0.1})^2
$$

Final $V$:

$$
V_{i = 0:10}^{t = 0.1} = [5.000, 5.009, 5.045, 5.119, 5.231, 5.371, 5.522, 5.670, 5.800, 5.904, 6.008]
$$

Initial guess for $U$:

$$
U_{i = 0:10} = 5.0
$$

Propagating the initial guess is trivialized by last week's code (`make_A` and `make_B` are identical to last week):

```py
A = make_A()


def propagate(Us_initial):
    Us = Us_initial.copy()

    step = 0

    while step < steps:
        B = make_B(Us)
        Us = np.linalg.solve(A, B).flatten()
        t += delta_t
        step += 1

    return Us
```

And the objective function:

```py
def f(Us_initial):
    Us = propagate(Us_initial)
    return np.sum((Us - Vs_final) ** 2)
```

I tried gradient decent with finite difference:

```py
epsilon = 1e-5


def gradient(Us):
    gradient = np.zeros_like(Us)

    for idx in np.ndindex(Us.shape):
        Us_plus = Us.copy()
        Us_minus = Us.copy()

        Us_plus[idx] += epsilon
        Us_minus[idx] -= epsilon

        gradient[idx] = (f(Us_plus) - f(Us_minus)) / (2 * epsilon)

    return gradient


learning_rate = 1e-4
iteration = 0
loss = f(Us)

while loss > 0.25:
    grad = gradient(Us)
    iteration += 1
    Us -= learning_rate * grad
    loss = f(Us)

    print(iteration, loss)
```

But this took 7450 iterations just to get to 0.25 loss which is horrendously slow. So I tried using a Newton method by adapting the code from `03_Rosenbrock_Newton.py` on Canvas to work with my ecosystem:

```py
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
```

This converges in just 3 iterations! The console output:

```
i: 0 loss: 3.4019330000000636 gradient norm: 3.4773037550578447
i: 1 loss: 1.9120805556117507e-07 gradient norm: 0.0002620126617914014
i: 2 loss: 2.3135808560513227e-19 gradient norm: 1.7787145001549826e-10
optimal point found
Final loss: 2.3135808560513227e-19
Final Us: [5.         5.0903571  5.19405994 5.3500698  5.51690892 5.67881658
 5.81490393 5.92367641 5.95366026 5.75642971 4.33704567]
Final propagated Us: [5.    5.009 5.045 5.119 5.231 5.371 5.522 5.67  5.8   5.904 6.008]
Iterations: 2
```

The most important bit the final loss (or `f(U)`):

```
Final loss: 2.3135808560513227e-19
```

And the converged initial $U$:

```
Final Us: [5.         5.0903571  5.19405994 5.3500698  5.51690892 5.67881658
 5.81490393 5.92367641 5.95366026 5.75642971 4.33704567]
```

Testing the propagated $U$ using $f(U)$:

```
Final propagated Us: [5.    5.009 5.045 5.119 5.231 5.371 5.522 5.67  5.8   5.904 6.008]
```

Which is pretty much the target:

$$
V_{i = 0:10}^{t = 0.1} = [5.000, 5.009, 5.045, 5.119, 5.231, 5.371, 5.522, 5.670, 5.800, 5.904, 6.008]
$$
