# AERE 321 Homework 1

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

Here, $C_1$ is suspiciously large so I decided to plot it in Python. The code is fairly straight forward (I did have to define the Macaulay function which I was surprised to see not implemented already into a library). While I was at it, I also evaluated some "sanity check points", where the graphs must be $0$ in order to be physically accurate. I also calculated the minimum and maximum moments.

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


xs = np.linspace(0, L, 1000)
Ms = M(xs)
ys = y(xs)

min_M = np.min(Ms / W)
min_M_x = xs[np.argmin(Ms / W)]
max_M = np.max(Ms / W)
max_M_x = xs[np.argmax(Ms / W)]

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

ax1.plot(xs, Ms / W, color="tab:blue")
ax1.annotate("End moment constraint", xy=(0, 0), color="tab:blue")
ax1.annotate("End moment constraint", xy=(84, 0), color="tab:blue")
ax1.annotate(
    f"Max negative moment ({min_M_x: 0.2f}, {min_M: 0.2f})",
    xy=(min_M_x, min_M),
    color="tab:blue",
)
ax1.annotate(
    f"Max positive moment ({max_M_x: 0.2f}, {max_M: 0.2f})",
    xy=(max_M_x, max_M),
    color="tab:blue",
)
ax1.set_ylabel("M(x) / W")
ax1.axhline(0, color="k", lw=0.8)
ax1.grid(True)

ax2.plot(xs, ys / W, color="tab:red")
ax2.annotate("Pin constraint", xy=(0, 0), color="tab:red")
ax2.annotate("Roller constraint", xy=(42, 0), color="tab:red")
ax2.annotate("Roller constraint", xy=(84, 0), color="tab:red")
ax2.set_xlabel("x")
ax2.set_ylabel("y(x) / W")
ax2.axhline(0, color="k", lw=0.8)
ax2.grid(True)

fig.tight_layout()
plt.show()
```

There were a few calculation mistakes like forgetting the integration constants but after fixing them, finally, I got a graph that makes sense. The moments at both ends is $0$. The offset $y$ is also $0$ at both rollers and the one pin. 100% worth it.

![](https://i.imgur.com/mphpKoe.png)

Moving on, I was able to glean the following information:

$$
M_{min} = -109.93W
$$

$$
M_{max} = 168.91W
$$

This will be helpful when calculating the value for $W$ against the maximum allowable $\sigma = \sigma_{Y}$ at the very top and bottom surfaces. The shear however, I still need to calculate and graph. I can take the derivative of the moment but I choose to just reconstruct it from the static diagram.

![](https://i.imgur.com/J2f2D7k.png)

Here, I we can see that:

$$
|V|_{max} = 23.62W
$$

I don't have or need to know the value of $x_1$ for this problem but I'll calculate it anyway:

$$
\frac{18.83}{x_1} = \frac{23.62}{42 - x_1} \implies x_1 = 18.63"
$$

The value of $18.83$ in inches is suspiciously the same as $A = 18.83W$ but I shouldn't question is because of how symmetric the problem is about $x = 42"$.

Weird tangents aside, it's almost time to calculate the potential values of $W$, I just need a few values, starting with $I$:

![](https://i.imgur.com/yaTjdnr.png)

$$
A_1 = A_2 = bh = 6in^2
$$

$$
y_1 = b + \frac{1}{2}h = 6.5"
$$

$$
y_2 = \frac{1}{2} b = 3"
$$

$$
\bar y = \frac{\cancel{A_1} y_1 + \cancel{A_2} y_2}{\cancel{A_1} + \cancel{A_2}} = \frac{y_1 + y_2}{2} = 4.75"
$$

$$
d_1 = y_1 - \bar y = 6.5" - 4.75" = 1.75"
$$

$$
d_2 = y_2 - \bar y = 3" - 4.75" = -1.75"
$$

$$
I_1 = \frac{bh^3}{12} = \frac{6" * (1")^3}{12} = 0.5 in^4
$$

$$
I_2 = \frac{hb^3}{12} = \frac{1" * (6")^3}{12} = 18 in^4
$$

$$
I = I_1 + I_2 + A_1 d_1^2 + A_2 d_2^2
$$

$$
I = 0.5 in^4 + 18 in^4 + 6in^2 * (1.75")^2 + 6in^2 * (-1.75")^2 = 55.25in^4
$$

And now for $Q$, a value I still don't understand. I apologize if my drawing looks like children's doodles, I don't have a pen, just a mouse and a mighty will.

![](https://i.imgur.com/jzoHeTG.png)

$$
Q = bh(b - \bar y + \frac{1}{2}h) + (b - \bar y) h \frac{1}{2} (b - \bar y)
$$

$$
Q = bh(b - \bar y + \frac{1}{2}h) + \frac{1}{2} (b - \bar y)^2 h
$$

$$
Q = 6" * 1" * (6" - 4.75" + \frac{1}{2} * 1") + \frac{1}{2} (6" - 4.75")^2 * 1" = 11.28in^3
$$

Let's recover some $W$.

$$
M_{min} = -109.93W
$$

Thus, the top surface will be in tension:

$$
\sigma_Y = \frac{|M_{min}|b}{I}
$$

$$
|M_{min}| = \frac{I \sigma_Y}{b} = \frac{55.25in^4 * 350 ksi}{6"} = 3222.92 = 109.93W
$$

$$
\implies W = 29.32 kip/in
$$

The bottom:

$$
M_{max} = 168.91W
$$

$$
\sigma_Y = \frac{|M_{max}| h}{I}
$$

$$
|M_{max}| = \frac{I \sigma_Y}{h} = \frac{55.25in^4 * 350 ksi}{1"} = 19338 = 168.91W
$$

$$
\implies W = 114.5 kip/in
$$

The shear:

$$
\tau_Y = \frac{|V|_{max} Q}{I (b - \bar y + h)}
$$

$$
|V|_{max} = \frac{\tau_Y I (b - \bar y + h)}{Q} = \frac{190 ksi * 55.25in^4 * (6" - 4.75" + 1")}{11.28in^3} = 2094 = 23.62W
$$

$$
\implies W = 88.65 kip/in
$$

I am going with the minimum of these values which should ensure no other cases fail:

$$
\boxed{W = 29.32 kip/in}
$$

When the top surface is under tension,

$$
x = 42"
$$

The x-axis is under the maximum allowable stress:

$$
\sigma_x = \sigma_Y = 350 ksi
$$

There's nothing happening on the other axis:

$$
\sigma_z = \sigma_y = 0
$$

As for the shear here:

$$
\tau_{xy} = -23.62W = -692.54 ksi
$$

All other perpendicular shears are zero. Thus, this results in a simple state of stress cube of the very top surface of the T-beam:

![](https://i.imgur.com/NDuQ1GT.png)

One last thing the problem asks for is the normal and shear stress profiles of the cross section of the T-beam as a function of y. This will be better done with code. Here's my solution:

```py
import numpy as np
import pint
import matplotlib.pyplot as plt
import random

ur = pint.UnitRegistry()

b = 6 * ur.inch
h = 1 * ur.inch

A1 = b * h
A2 = h * b

y1 = b + (1 / 2) * h
y2 = (1 / 2) * b
y_bar = (A1 * y1 + A2 * y2) / (A1 + A2)

d1 = y1 - y_bar
d2 = y2 - y_bar

I1 = (b * h**3) / 12
I2 = (h * b**3) / 12
I = I1 + A1 * d1**2 + I2 + A2 * d2**2


ys = np.linspace(0, b.magnitude, 100) * ur.inch


def sigma_over_M(c):
    return c / I


def Q(y):
    y = y.magnitude
    _h = h.magnitude
    _b = b.magnitude
    _y_bar = y_bar.magnitude

    if y < 0:
        y = -y
        height_2 = _y_bar - y
        _A2 = _h * height_2
        _d2 = y + height_2 / 2
        return _A2 * _d2
    elif 0 <= y < _b - _y_bar:
        height_2 = y
        _A2 = _h * height_2
        _d2 = height_2 / 2
        height_1 = _h
        _A1 = height_1 * _b
        _d1 = height_2 + height_1 / 2
        return _A2 * _d2 + _A1 * _d1
    else:
        height_1 = _h + _b - _y_bar - y
        _A1 = height_1 * _b
        _d1 = (height_1) / 2 + y
        return _A1 * _d1


def tau_over_V(y):
    return Q(y) / (I * b)


sigma_over_Ms = sigma_over_M(ys - y_bar)

plt.plot(sigma_over_Ms.magnitude, ys.magnitude)
plt.xlabel(r"$\sigma(x) / M$")
plt.ylabel("y (inches)")
plt.grid(axis="both")
plt.show()

plt.plot([Q(y - y_bar) for y in ys], ys - y_bar)
plt.xlabel(r"$\tau(x) / V$")
plt.ylabel("y (inches)")
plt.grid(axis="both")
plt.show()
```

The plot for $\sigma(x) / M$ is simple:

![](https://i.imgur.com/TLsCQdt.png)

But the plot of $\tau(x) / V$ is a bit more involved:

![](https://i.imgur.com/qBJk8I1.png)

I did anticipate the $\tau(x) / V$ to look a bit different but I have spent hours on the code and I am unsure what is going on. So, I just drew the lines by hand for what it should've looked like, no numbers.

![](https://i.imgur.com/HQhIGRJ.png)

Regardless, I believe that's all problems 1) through 7) done, wildly out of order. Sorry, TA!
