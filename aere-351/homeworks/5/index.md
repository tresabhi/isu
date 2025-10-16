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

## 4.

This is similar to the last question, but backwards.

![](https://i.imgur.com/KEFFS9zm.png)

Implications from the question statement and diagram:

$$
h_a = h_p = h_a' = 500km
$$

$$
\theta = 180\degree - 60\degree = 2.094rad \implies h = 0
$$

From the Internet:

$$
R = 6378km
$$

$$
\mu = 3.98600 * 10^5 km^3/s^2
$$

Initial orbit:

$$
r_a = r_p = r_a' = R + h_a = 6378km + 500km = 6878km
$$

$$
a = r_a = r_p = 6878km
$$

$$
e = 0
$$

$$
p = a (1 - \cancel{e^2}) = a = 6878km
$$

$$
v = \sqrt{\frac{\mu}{p}} (1 + \cancel{e \cos \theta}) = \sqrt{\frac{\mu}{p}} = \sqrt{\frac{3.98600 * 10^5 km^3/s^2}{6878km}} = 7.613km/s
$$

Final orbit:

$$
r_a' = r_a = 6878km
$$

$$
\theta_2 = -60\deg = -1.047 rad \implies r = R = 6378km
$$

$$
r = \frac{p}{1 + e \cos \theta}
$$

$$
r_a' = r_a = \frac{p}{1 + e \cos \pi} = \frac{p}{1 - e}
$$

$$
r = R = \frac{p}{1 + e \cos \theta_2}
$$

$$
\frac{R}{r_a} = \frac{\frac{p}{1 + e \cos \theta_2}}{\frac{p}{1 - e}} = \frac{1 - e}{1 + e \cos \theta_2}
$$

$$
\frac{6378km}{6878km} = \frac{1 - e}{1 + e \cos (-1.047 rad)} \implies e = 0.04966
$$

$$
r_a = \frac{p}{1 - e}
$$

$$
p = r_a (1 - e) = 6878km * (1 - 0.04966) = 6536km
$$

$$
v_a' = v_\theta = \sqrt{\frac{\mu}{p}} (1 + e \cos \pi) = \sqrt{\frac{3.98600 * 10^5 km^3/s^2}{6536km}} (1 - 0.04966) = 7.4215km/s
$$

$$
\Delta v = v_a' - v_a = | 7.4215km/s - 7.613km/s | = \boxed{0.192km/s}
$$

## 5.

![](https://i.imgur.com/8X6bHV2.png)

Given:

$$
e_1 = 0.3
$$

$$
e_2 = 0.5
$$

$$
r_{p1} = 7000km
$$

$$
r_{p2} = 32000km
$$

Once again, there is no indication of what planet this question is referring to so I am assuming this is Earth. This leads the to following property:

$$
\mu = 3.98600 * 10^5 km^3/s^2
$$

Properties of orbit 1:

$$
e_1 = \frac{r_{a1} - r_{p1}}{r_{a1} + r_{p1}}
$$

$$
e_1 r_{a1} + e_1 r_{p1} = r_{a1} - r_{p1}
$$

$$
r_{a1} - e_1 r_{a1} = r_{p1} + e_1 r_{p1} = r_{a1} (1 - e_1)
$$

$$
r_{a1} = \frac{r_{p1} + e_1 r_{p1}}{1 - e_1} = \frac{7000km + 0.3 * 7000km}{1 - 0.3} = 13000km
$$

$$
p_1 = a_1 (1 - e_1^2) = \frac{r_{a1} + r_{p1}}{2} (1 - e_1^2) = \frac{13000km + 7000km}{2} (1 - 0.3^2) = 9100km
$$

$$
v_{p1} = \sqrt{\frac{\mu}{p_1}} (1 + e_1) = \sqrt{\frac{3.98600 * 10^5 km^3/s^2}{9100km}} (1 + 0.3) = 8.604 km/s
$$

$$
v_{a1} = \sqrt{\frac{\mu}{p_1}} (1 - e_1) = \sqrt{\frac{3.98600 * 10^5 km^3/s^2}{9100km}} (1 - 0.3) = 4.633 km/s
$$

Properties of orbit 2:

$$
r_{a2} = \frac{r_{p2} + e_1 r_{p2}}{1 - e_1} = \frac{32000km + 0.5 * 32000km}{1 - 0.5} = 96000km
$$

$$
p_2 = \frac{r_{a2} + r_{p2}}{2} (1 - e_2^2) = \frac{96000km + 32000km}{2} (1 - 0.5^2) = 48000km
$$

$$
v_{p2} = \sqrt{\frac{\mu}{p_2}} (1 + e_2) = \sqrt{\frac{3.98600 * 10^5 km^3/s^2}{48000km}} (1 + 0.5) = 4.323 km/s
$$

$$
v_{a2} = \sqrt{\frac{\mu}{p_2}} (1 - e_2) = \sqrt{\frac{3.98600 * 10^5 km^3/s^2}{48000km}} (1 - 0.5) = 1.441 km/s
$$

Solution 3:

$$
r_p = r_{p1} = 7000km \quad r_a = r_{a1} = 13000km
$$

$$
r_p' = r_{p1} = 7000km \quad r_a' = r_{a2} = 96000km
$$

$$
r_p'' = r_{p2} = 32000km \quad r_a'' = r_{a2} = 96000km
$$

$$
e' = \frac{r_a' - r_p'}{r_a' + r_p'} = \frac{96000km - 7000km}{96000km + 7000km} = 0.8641
$$

$$
a' = \frac{r_a' + r_p'}{2} = \frac{96000km + 7000km}{2} = 51500km
$$

$$
p' = a' (1 - e'^2) = 51500km * (1 - 0.8641^2) = 13047km
$$

$$
v_p = v_{p1} = 8.604 km/s
$$

$$
v_p' = \sqrt{\frac{\mu}{p'}} (1 + e') = \sqrt{\frac{3.98600 * 10^5 km^3/s^2}{13047km}} (1 + 0.8641) = 10.30 km/s
$$

$$
v_a' = \sqrt{\frac{\mu}{p'}} (1 - e') = \sqrt{\frac{3.98600 * 10^5 km^3/s^2}{13047km}} (1 - 0.8641) = 0.7512 km/s
$$

$$
v_a'' = v_{a2} = 1.441 km/s
$$

$$
\Delta v = v_p' - v_p + v_a'' - v_a' = 10.30 km/s - 8.604 km/s + 1.441 km/s - 0.7512 km/s = \boxed{2.386 km/s}
$$
