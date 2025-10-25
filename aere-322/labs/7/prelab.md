# AERE 322 Prelab 7

## 3.

The moment under a small lateral deflection is the integral of the stress times the area over the cross section:

$$
M_r = y \int_A \sigma dA
$$

Sigma can be expressed as a function of y and a constant coefficient, thus pulling $y$ back in:

$$
M_r = \text{const} \int_A y^2 dA
$$

That's the moment of inertia!

$$
M_r = \text{const} I
$$

That leads us to the flexure formula:

$$
\sigma = \frac{M y}{I}
$$

The outermost elongation for an infinitesimal element $dx$ is:

$$
c d\theta = \epsilon_c dx = \frac{\sigma_c}{E} = \frac{M c}{E I} dx
$$

Rearranged:

$$
\frac{d \theta}{d x} = \frac{M}{E I}
$$

My psychologist prescribed me at least one small angle approximation per day after noon, or else I go insane as an engineer:

$$
\tan \theta \approx \frac{dy}{dx}
$$

This gives us a differential equation:

$$
\frac{d \theta}{d x} = \frac{d^2 y}{d x^2} = \frac{M}{E I}
$$

$$
\frac{d^2 y}{dx^2} + \frac{P y}{EI} = 0
$$

The solution to that is:

$$
y = A \sin \sqrt{\frac{P}{EI}} x + B \cos \sqrt{\frac{P}{EI}} x
$$

To solve this, we need end conditions:

$$
x = 0, ~ y = 0 \implies B = 0
$$

$$
x = L, ~ y = 0, \implies A = 0
$$

This grants us:

$$
\sqrt{\frac{P}{EI}} L = n \pi \impliedby n \in \N
$$

Or for $n = 1$:

$$
P = \boxed{\frac{\pi^2 E I}{L^2}}
$$

For a circular rod of radius $r$:

$$
I = \frac{\pi}{4} r^4
$$

$$
P = \frac{\pi^2 E}{L^2} \frac{\pi}{4} r^4 = \frac{\pi^3 E r^4}{4 L^2}
$$

Radius of gyration for a circle:

$$
\rho = \sqrt{\frac{I}{A}} = \sqrt{\frac{\pi r^4 / 4}{\pi r^2}} = \frac{r}{2}
$$

$$
\frac{L}{\rho} = \frac{L}{r/2} = \boxed{\frac{2L}{r}}
$$

A similar story for rectangles:

$$
I = \frac{bh^3}{12}
$$

$$
P = \frac{\pi^2 E}{L^2} \frac{bh^3}{12} = \frac{\pi^3 E b h^3}{12 L^2}
$$

$$
A = bh
$$

$$
\rho = \sqrt{\frac{I}{A}} = \sqrt{\frac{bh^3/12}{bh}} = \frac{h}{\sqrt{12}}
$$

$$
\frac{L}{\rho} = \frac{L}{h/\sqrt{12}} = \boxed{\frac{L \sqrt{12}}{h}}
$$

## 4.

```py
import pint
import math

ur = pint.UnitRegistry()

# Stainless 304 annealed cold finish steel
E_st = 29000 * ur.ksi
sigma_Y_st = 35 * ur.ksi

# 6061-T6 aluminum
E_al = 10000 * ur.ksi
sigma_Y_al = 40 * ur.ksi

cases = [
    (E_al, "circle", (3 / 8) * ur.inch, 30 * ur.inch, "pinned_pinned"),
    (
        E_al,
        "rectangle",
        ((1 / 4) * ur.inch, 1 * ur.inch),
        30 * ur.inch,
        "pinned_pinned",
    ),
    (E_st, "circle", (1 / 4) * ur.inch, 30 * ur.inch, "pinned_pinned"),
    (E_st, "circle", (1 / 4) * ur.inch, 24 * ur.inch, "pinned_pinned"),
    (E_st, "circle", (1 / 4) * ur.inch, 27.5 * ur.inch, "pinned_fixed"),
]

index = 1
for case in cases:
    E, shape, size, L, ends = case
    I, L_effective = 0, 0

    if shape == "circle":
        r = size / 2
        I = (math.pi / 4) * r**4
    elif shape == "rectangle":
        b, h = size
        I = (b * h**3) / 12
    else:
        raise ValueError(f"Unknown shape: {shape}")

    if ends == "fixed_fixed":
        L_effective = L / 2
    elif ends == "fixed_pinned" or ends == "pinned_fixed":
        L_effective = L / math.sqrt(2)
    elif ends == "pinned_pinned":
        L_effective = L
    elif ends == "fixed_free" or ends == "free_fixed":
        L_effective = 2 * L
    else:
        raise ValueError(f"Unknown ends: {ends}")

    P = (math.pi**2 * E * I) / (L_effective**2)
    P = P.to(ur.kip)

    L_rho = 0

    if shape == "circle":
        r = size / 2
        L_rho = (2 * L_effective) / r
    elif shape == "rectangle":
        b, h = size
        L_rho = (L_effective * math.sqrt(12)) / h

    L_rho = L_rho.magnitude

    print(f"Case {index}:")
    print(f"  L_eff =", L_effective)
    print(f"  P =", P)
    print(f"  L/rho =", L_rho, end="\n\n")

    index += 1
```
