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
