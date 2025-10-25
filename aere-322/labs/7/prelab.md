# AERE 322 Prelab 7

## 3.

The moment under a small lateral deflection is the integral of the stress times the area over the cross section.

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
