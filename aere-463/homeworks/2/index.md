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

---

The final state (writing it in Python to copy to code easier):

```py
V_final = np.matrix(
    [5.000, 5.009, 5.045, 5.119, 5.231, 5.371, 5.522, 5.670, 5.800, 5.904, 6.008]
)
```

My derivations from last from for elements 1-9:

$$
- \frac{\mu}{\Delta x^2} U_{i - 1}^{n + 1} + \left( \frac{1}{\Delta t} + \frac{2 \mu}{\Delta x^2} \right) U_i^{n + 1} - \frac{\mu}{\Delta x^2} U_{i + 1}^{n + 1} = \left( \frac{1}{\Delta t} + \frac{\lambda}{\Delta x} \right) U_i^n - \frac{\lambda}{\Delta x} U_{i + 1}^n
$$

With the two remaining elements being boundary conditions:

$$
U_0 = 5.0
$$

$$
U_8 - 2 U_9 + U_{10} = 0
$$

The constants:

$$
\Delta x = 0.1
$$

$$
\Delta t = 0.01
$$

$$
\lambda = 2.0
$$

$$
\mu = 0.2
$$
