# AERE 351 Homework 5

## 1.

The goal is to reach $E$ from $\theta$ and $e$. I am assuming we're only dealing with elliptical orbits. Thankfully, there's a real neat formula that we derived in class relating the two sets of variables:

$$
\tan \frac{\theta}{2} = \sqrt{\frac{1 + e}{1 - e}} \tan \frac{E}{2}
$$

$$
\sqrt{\frac{1 - e}{1 + e}} \tan \frac{\theta}{2} = \tan \frac{E}{2}
$$

$$
E = 2 \arctan \left( \sqrt{\frac{1 - e}{1 + e}} \tan \frac{\theta}{2} \right)
$$

`true_to_ecc` implementation:

```m
function E = true_to_ecc(e, theta)
    E = 2 * atan(sqrt((1 - e) / (1 + e)) * tan(theta / 2));
end
```

Now for $E$ and $e$ to $M$:

$$
M = E - e \sin E
$$

It think it'll be cleaner to not substitute in the equation for $E$ so I am leaving $M$ as is. My `ecc_to_mean` implementation:

```m
function M = ecc_to_mean(e, E)
    M = E - e * sin(E);
end
```

Finally, the script for plotting:

```m
es = 0:0.05:0.95;
thetas = deg2rad(0:1:359);

figure(1); hold on; grid on;
title('E vs M');
xlabel('M (rad)');
ylabel('E (rad)');

figure(2); hold on; grid on;
title('θ vs M');
xlabel('M (rad)');
ylabel('\theta (deg)');

for e = es
    Es = true_to_ecc(e, thetas);
    Ms = ecc_to_mean(e, Es);

    figure(1);
    plot(Ms, Es, "DisplayName", sprintf("e = %.2f", e));

    figure(2);
    plot(rad2deg(thetas), rad2deg(Es), "DisplayName", sprintf("e = %.2f", e));
end
```

This leads to the following plots:

![](https://i.imgur.com/7juEUNW.png)

![](https://i.imgur.com/xxaYl3g.png)

I then modified `true_to_ecc` to handle hyperbolic orbits:

```m
function E = true_to_ecc(e, theta)

    if e < 1
        E = 2 * atan(sqrt((1 - e) / (1 + e)) * tan(theta / 2));
    elseif e == 1
        E = theta;
    else
        E = 2 * atanh(sqrt((e - 1) / (e + 1)) * tan(theta / 2));
    end

end
```

And the hyperbolic plotting script:

```m
es = 1:0.5:4;
thetas = deg2rad(1:1:110);

figure(1); hold on; grid on;
title('E vs M');
xlabel('M (rad)');
ylabel('E (rad)');

figure(2); hold on; grid on;
title('θ vs M');
xlabel('M (rad)');
ylabel('\theta (deg)');

for e = es
    Es = true_to_ecc(e, thetas);
    Ms = ecc_to_mean(e, Es);

    figure(1);
    semilogy(Ms, Es, "DisplayName", sprintf("e = %.2f", e));

    figure(2);
    semilogy(rad2deg(thetas), rad2deg(Es), "DisplayName", sprintf("e = %.2f", e));
end
```

This gives the following plots:

![](https://i.imgur.com/ZCRtBTY.png)

![](https://i.imgur.com/ZuYxliS.png)

The plots make sense since the axis are subject to the logarithmic scaling of `semilogy` so we see good resolution at low values of $E$ but the points get more discrete (and somewhat nonsensical due to precision issues) as $E$ gets larger.

## 2.

For `mean_to_ecc`, I tried to calculate the residue and stop when reaching a residue of below $10^{-4}$ and even $10^{-8}$ but it always seemed to stop after like 1 or 2 iterations. So I went for a fixed $50% iterations. My implementation for `mean_to_ecc`

```m
function E = mean_to_ecc(e, M)
    E = M;

    for i = 1:50
        E = E - ((E - e .* sin(E) - M) ./ (1 - e .* cos(E)));
    end

end
```

And `ecc_to_true`:

```m
function theta = ecc_to_true(E, e)
    theta = 2 * atan(sqrt((1 + e) / (1 - e)) * tan(E / 2));
end
```

The plot script is a simple fork from the previous question:

```m
Ms = deg2rad(0:1:359);
es = 0:0.05:0.95;

figure(1); hold on; grid on;
title('E vs M');
xlabel('M (rad)');
ylabel('E (rad)');

figure(2); hold on; grid on;
title('θ vs M');
xlabel('M (rad)');
ylabel('\theta (deg)');

for e = es
    Es = mean_to_ecc(e, Ms);
    thetas = ecc_to_true(Es, e);

    figure(1);
    plot(Ms, Es, "DisplayName", sprintf("e = %.2f", e));

    figure(2);
    plot(Ms, rad2deg(thetas), "DisplayName", sprintf("e = %.2f", e));
end
```

The plots:

![](https://i.imgur.com/nZ0x8td.png)

![](https://i.imgur.com/XHWQsVU.png)

For the next part, once again, I patched `mean_to_ecc` to work with hyperbolic orbits:

```m
function E = mean_to_ecc(e, M)
    E = M;

    if e == 1
        return
    end

    for i = 1:50

        if e < 1
            E = E - ((E - e .* sin(E) - M) ./ (1 - e .* cos(E)));
        else
            E = E - ((e .* sinh(E) - E - M) ./ (e .* cosh(E) - 1));
        end

    end

end
```

And `ecc_to_true`:

```m
function theta = ecc_to_true(E, e)

    if e < 1
        theta = 2 * atan(sqrt((1 + e) / (1 - e)) * tan(E / 2));
    elseif e == 1
        theta = E;
    else
        theta = 2 * atan(sqrt((e + 1) / (e - 1)) * tanh(E / 2));
    end

end
```

The plots:

![](https://i.imgur.com/HdDT2Fa.png)

![](https://i.imgur.com/gxnKA5S.png)

## 3.

Given:

$$
R = 6378km
$$

$$
h_a = 278km
$$

$$
h_p = -196km
$$

From the Internet:

$$
\mu = 3.98600 * 10^5 km^3/s^2
$$

Actual radii:

$$
r_a = R + h_a = 6378km + 278km = 6656km
$$

$$
r_p = R + h_p = 6378km - 196km = 6182km
$$

Current velocity at the apogee:

$$
a = \frac{r_a + r_p}{2} = \frac{6656km + 6182km}{2} = 6419km
$$

$$
e = \frac{r_a - r_p}{r_a + r_p} = \frac{6656km - 6182km}{6656km + 6182km} = 0.03692
$$

$$
p = a (1 - e^2) = 6419km (1 - 0.03692^2) = 6410km
$$

$$
v_a = \sqrt{\frac{\mu}{p}} (1 - e) = \sqrt{\frac{3.98600 * 10^5 km^3/s^2}{6410km}} (1 - 0.03692) = 7.595km/s
$$

Target velocity at apogee for a circular orbit:

$$
r_p' = r_a
$$

$$
a' = \frac{r_a + r_p}{2} = \frac{2r_a}{2} = r_a = 6656km
$$

$$
e' = 0
$$

$$
p' = a (1 - e^2) = a = 6656km
$$

$$
v_a' = \sqrt{\frac{\mu}{p'}} (1 - e') = \sqrt{\frac{3.98600 * 10^5 km^3/s^2}{6656km}} = 7.739km/s
$$

Delta velocity:

$$
\Delta v = v_a' - v_a = 7.739km/s - 7.595km/s = \boxed{0.144km/s}
$$
