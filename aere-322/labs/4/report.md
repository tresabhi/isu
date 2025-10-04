# AERE 322 Report 4

Target:

$$
x = L \implies y = - \frac{L^3}{EI} \left( \frac{5 w_2}{162} - \frac{w_1}{216} \right)
$$

Diagram:

![](https://i.imgur.com/C86iihU.png)

Statics:

$$
\sum F_y = 0 = A - w_1 + B - w_2
$$

$$
A = w_1 - B + w_2
$$

$$
\sum M_{x = \frac{2}{3} L} = 0 = M - A \frac{2}{3} L + w_1 \frac{1}{3} L - w_2 \frac{1}{3} L
$$

$$
0 = M - \frac{2}{3} A L + \frac{1}{3} w_1 L - \frac{1}{3} w_2 L
$$

$$
M = \frac{2}{3} A L - \frac{1}{3} w_1 L + \frac{1}{3} w_2 L
$$

Superposition:

$$
M(x) = -M \langle x - 0 \rangle^0 + A \langle x - 0 \rangle^1 - w_1 \langle x - \frac{1}{3} L \rangle^1 + B \langle x - \frac{2}{3} L \rangle^1 - w_2 \langle x - L \rangle^1
$$

$$
M(x) = -M + A x - w_1 \langle x - \frac{1}{3} L \rangle^1 + B \langle x - \frac{2}{3} L \rangle^1
$$

$$
\theta(x) = \frac{1}{EI} \left[ -M x + \frac{1}{2} A x^2 - \frac{1}{2} w_1 \langle x - \frac{1}{3} L \rangle^2 + \frac{1}{2} B \langle x - \frac{2}{3} L \rangle^2 \right] + C_1
$$

$$
\theta(0) = 0 = 0 + C_1 \implies C_1 = 0
$$

$$
\theta(x) = \frac{1}{EI} \left[ -M x + \frac{1}{2} A x^2 - \frac{1}{2} w_1 \langle x - \frac{1}{3} L \rangle^2 + \frac{1}{2} B \langle x - \frac{2}{3} L \rangle^2 \right]
$$

$$
y(x) = \frac{1}{EI} \left[ -\frac{1}{2} M x^2 + \frac{1}{6} A x^3 - \frac{1}{6} w_1 \langle x - \frac{1}{3} L \rangle^3 + \frac{1}{6} B \langle x - \frac{2}{3} L \rangle^3 \right] + C_2
$$

$$
y(0) = 0 = 0 + C_2 \implies C_2 = 0
$$

$$
y(x) = \frac{1}{EI} \left[ -\frac{1}{2} M x^2 + \frac{1}{6} A x^3 - \frac{1}{6} w_1 \langle x - \frac{1}{3} L \rangle^3 + \frac{1}{6} B \langle x - \frac{2}{3} L \rangle^3 \right]
$$

$$
y(\frac{2}{3} L) = 0 = \frac{1}{EI} \left[ -\frac{1}{2} M \frac{4}{9} L^2 + \frac{1}{6} A \frac{8}{27} L^3 - \frac{1}{6} w_1 \langle \frac{2}{3} L - \frac{1}{3} L \rangle^3 + \frac{1}{6} B \langle \cancel{\frac{2}{3} L - \frac{2}{3} L} \rangle^3 \right]
$$

$$
0 = -\frac{1}{2} M \frac{4}{9} L^2 + \frac{1}{6} A \frac{8}{27} L^3 - \frac{1}{6} w_1 \left( \frac{1}{3} L \right)^3
$$

$$
0 = -\frac{1}{2} M \frac{4}{9} L^2 + \frac{1}{6} A \frac{8}{27} L^3 - \frac{1}{6} w_1 \frac{1}{27} L^3
$$

$$
0 = -\frac{2}{9} M L^2 + \frac{4}{81} A L^3 - \frac{1}{162} w_1 L^3
$$

Recall statics:

$$
0 = M - \frac{2}{3} A L + \frac{1}{3} w_1 L - \frac{1}{3} w_2 L
$$

$$
0 = M L^2 - \frac{2}{3} A L^3 + \frac{1}{3} w_1 L^3 - \frac{1}{3} w_2 L^3
$$

$$
0 = \frac{2}{9} M L^2 - \frac{2}{9} \frac{2}{3} A L^3 + \frac{2}{9} \frac{1}{3} w_1 L^3 - \frac{2}{9} \frac{1}{3} w_2 L^3
$$

$$
0 = \frac{2}{9} M L^2 - \frac{4}{27} A L^3 + \frac{2}{27} w_1 L^3 - \frac{2}{27} w_2 L^3
$$

Adding equations:

$$
0 = \cancel{\frac{2}{9} M L^2} - \frac{4}{27} A L^3 + \frac{2}{27} w_1 L^3 - \frac{2}{27} w_2 L^3 -\cancel{\frac{2}{9} M L^2} + \frac{4}{81} A L^3 - \frac{1}{162} w_1 L^3
$$

$$
0 = -\frac{8}{81} A L^3 + \frac{11}{162} w_1 L^3 - \frac{2}{27} w_2 L^3
$$

$$
\frac{8}{81} A L^3 = \frac{11}{162} w_1 L^3 - \frac{2}{27} w_2 L^3
$$

$$
A = \frac{11}{16} w_1 - \frac{3}{4} w_2
$$

Recall statics:

$$
A = w_1 - B + w_2 = \frac{11}{16} w_1 - \frac{3}{4} w_2
$$

$$
- B = -\frac{5}{16} w_1 - \frac{7}{4} w_2
$$

$$
B = \frac{5}{16} w_1 + \frac{7}{4} w_2
$$

Final statics recall:

$$
M = \frac{2}{3} \left ( \frac{11}{16} w_1 - \frac{3}{4} w_2 \right) L - \frac{1}{3} w_1 L + \frac{1}{3} w_2 L
$$

$$
M = \frac{11}{24} w_1 L - \frac{1}{2} w_2 L - \frac{1}{3} w_1 L + \frac{1}{3} w_2 L
$$

$$
M = \frac{1}{8} w_1 L - \frac{1}{6} w_2 L
$$

Deflection at $x = L$:

$$
y(L) = \frac{1}{EI} \left[ -\frac{1}{2} M L^2 + \frac{1}{6} A L^3 - \frac{1}{6} w_1 \langle L - \frac{1}{3} L \rangle^3 + \frac{1}{6} B \langle L - \frac{2}{3} L \rangle^3 \right]
$$

$$
y(L) = \frac{1}{EI} \left[ -\frac{1}{2} M L^2 + \frac{1}{6} A L^3 - \frac{1}{6} w_1 \langle \frac{2}{3} L \rangle^3 + \frac{1}{6} B \langle \frac{1}{3} L \rangle^3 \right]
$$

$$
y(L) = \frac{1}{EI} \left[ -\frac{1}{2} \left( \frac{1}{8} w_1 L - \frac{1}{6} w_2 L \right) L^2 + \frac{1}{6} \left( \frac{11}{16} w_1 - \frac{3}{4} w_2 \right) L^3 - \frac{1}{6} w_1 \frac{8}{27} L^3 + \frac{1}{6} \left( \frac{5}{16} w_1 + \frac{7}{4} w_2 \right) \frac{1}{27} L^3 \right]
$$

$$
y(L) = \frac{1}{EI} \left[ \left( \frac{1}{12} w_2 - \frac{1}{16} w_1 \right) L^3 + \left( \frac{11}{96} w_1 - \frac{1}{8} w_2 \right) L^3 - \frac{4}{81} w_1 L^3 + \left( \frac{5}{96} w_1 + \frac{7}{24} w_2 \right) \frac{1}{27} L^3 \right]
$$

$$
y(L) = \frac{L^3}{EI} \left( \frac{w_1}{216} - \frac{5 w_2}{162} \right)
$$

$$
\boxed{y(L) = - \frac{L^3}{EI} \left( \frac{5 w_2}{162} - \frac{w_1}{216} \right)}
$$
