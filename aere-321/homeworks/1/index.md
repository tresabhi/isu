# AERE 321 HW 1

A faithful recreation of the beam in question:

![](https://i.imgur.com/nkMaOhQ.png)

Given:

$$
L = 84"
$$

$$
L / 2 = 42"
$$

$$
h = 1"
$$

$$
b = 6"
$$

$$
E = 30,000 ksi
$$

$$
\sigma_Y = 350 ksi
$$

$$
\tau_Y = 190 ksi
$$

The complexity of this problem will skyrocket since I will be normalizing by dividing by $W$ so I will write the equations without units but under the hood, it's all inches and kips.

$$
M(x) = A \langle x \rangle + B \langle x - 42 \rangle + \frac{1}{2} W (\langle x - 42 \rangle^2 - \langle x \rangle^2)
$$

$$
\theta(x) = \frac{1}{EI} \int M(x) ~ dx = \frac{1}{EI} \left[ \frac{1}{2} A \langle x \rangle^2 + \frac{1}{2} B \langle x - 42 \rangle^2 + \frac{1}{6} W (\langle x - 42 \rangle^3 - \langle x \rangle^3) + C_1 \right]
$$

$$
y(x) = \int \theta(x) ~ dx = \frac{1}{EI} \left[ \frac{1}{6} A \langle x \rangle^3 + \frac{1}{6} B \langle x - 42 \rangle^3 + \frac{1}{24} W (\langle x - 42 \rangle^4 - \langle x \rangle^4) + C_1 x + C_2 \right]
$$

The end constraints are very revealing:

$$
y(0) = 0 = 0 + 0 + (0 - 0) + 0 + C_2 \implies C_2 = 0
$$

Thus,

$$
\boxed{M(x) = A \langle x \rangle + B \langle x - 42 \rangle + \frac{1}{2} W (\langle x - 42 \rangle^2 - \langle x \rangle^2)}
$$

and

$$
\boxed{y(x)EI = \frac{1}{6} A \langle x \rangle^3 + \frac{1}{6} B \langle x - 42 \rangle^3 + \frac{1}{24} W (\langle x - 42 \rangle^4 - \langle x \rangle^4) + C_1 x}
$$

Note that I moved EI to the left hand side for the sake of simplicity. Nevertheless, yet another constraint is directly in the middle of the beam:

$$
y(42)EI = 0 = \frac{1}{6} A (84)^3 + 0 + \frac{1}{24} W (0 - (42)^4) + C_1 * 42
$$

$$
\implies C_1= 3087W - 294A
$$

Something similar happens at the very end of the beam:

$$
y(84)EI = 0 = \frac{1}{6} A (84)^3 + \frac{1}{6} B (42)^3 + \frac{1}{24} W ((42)^4 - (84)^4) + C_1 * 84
$$

$$
\implies C_1 = -1176A - 147B + 23152.5W
$$

Moving onto the moment, $M(0)$ turns out to be useless but the other end, not so much:

$$
M(84) = 0 = A(84) + B(42) + frac{1}{2} W (42^2 - 84^2)
$$

$$
\implies A = 31.5W - 0.5B
$$

Now for a little trick that I figured out to preserve my sanity. Since everything's normalized by $W$, I will just declare new symbols:

$$
A' = A / W
$$

$$
B' = B / W
$$

$$
C_1' = C_1 / W
$$

This lets me create a system of equations that I can just chuck into a solver:

$$
C_1' = 3087 - 294A'
$$

$$
C_1' = -1176A' - 147B' + 23152.5
$$

$$
A' = 31.5 - 0.5B'
$$

My solver gives me:

$$
\boxed{A = 18.38W}
$$

$$
\boxed{B = 26.25W}
$$

$$
C_1 = -2315.25W
$$

This would be a good time to solve for $C$ (the force, not the constant of integration; confusion, I know):

$$
\sum F_y = A + B + C - 42W = 0
$$

$$
18.38W + 26.25W + C - 42W = 0
$$

$$
\implies \boxed{C = -2.63W}
$$

Here, $C_1$ is suspiciously large so I decided to plot it in Python. The code is fairly straight forward (I did have to define the Macaulay function which I was surprised to see not implemented already into a library):

```py
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

L = 84
E = 30_000
I = 55.25

W = sp.symbols("W")
A = 18.38 * W
B = 26.25 * W
C_1 = -2315.25 * W


def macaulay(x):
    return np.where(x < 0, 0, x)


def M(x):
    return (
        A * macaulay(x)
        + B * macaulay(x - 42)
        + (1 / 2) * W * (macaulay(x - 42) ** 2 - macaulay(x) ** 2)
    )


def y(x):
    return (1 / (E * I)) * (
        (1 / 6) * A * macaulay(x) ** 3
        + (1 / 6) * B * macaulay(x - 42) ** 3
        + (1 / 24) * W * (macaulay(x - 42) ** 4 - macaulay(x) ** 4)
        + C_1 * x
    )


x = np.linspace(0, L, 1000)


fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

ax1.plot(x, M(x) / W, color="tab:blue")
ax1.set_ylabel("M(x) / W")
ax1.axhline(0, color="k", lw=0.8)
ax1.grid(True)

ax2.plot(x, y(x) / W, color="tab:red")
ax2.set_xlabel("x")
ax2.set_ylabel("y(x) / W")
ax2.axhline(0, color="k", lw=0.8)
ax2.grid(True)

fig.tight_layout()
plt.show()
```

This results make intuitive sense in all manner:

![](https://i.imgur.com/4ed08Dz.png)
