# AERE 351 Homework 4

## 1.

$$
E_0 = 0
$$

$$
E_1 = \frac{\pi}{2}
$$

$$
n = \frac{2 \pi}{T}
$$

$$
M = nt
$$

$$
M = 2 \pi \frac{t}{T}
$$

$$
M = E - e \sin E
$$

$$
2 \pi \frac{t}{T} = E - e \sin E
$$

$$
t = \frac{T}{2 \pi} ( E - e \sin E )
$$

$$
t_0 = \frac{T}{2 \pi} ( 0 - e \sin 0 ) = 0
$$

$$
t_1 = \frac{T}{2 \pi} \left( \frac{\pi}{2} - e \sin \frac{\pi}{2} \right) = \frac{T}{2 \pi} \left( \frac{\pi}{2} - e \right)
$$

$$
t_1 = \frac{T}{2 \pi} \left( \frac{\pi}{2} - e \right) = T \left( \frac{1}{4} - \frac{\pi}{2} e \right)
$$

$$
\Delta t = t_1 - t_0 = T \left( \frac{1}{4} - \frac{\pi}{2} e \right) - 0
$$

$$
\boxed{\Delta t = T \left( \frac{1}{4} - \frac{\pi}{2} e \right)}
$$

## 2.

Given:

$$
h_p = 200km
$$

$$
h_a = 600km
$$

$$
h_{min} = 400km
$$

From the Internet:

$$
R = 6378.1km
$$

$$
\mu = 3.98600 * 10^5 km^3/s^2
$$

Actual $r$ values:

$$
r_p = R + h_p = 6378.1km + 200km = 6578.1km
$$

$$
r_a = R + h_a = 6378.1km + 600km = 6978.1km
$$

$$
r_{min} = R + h_{min} = 6378.1km + 400km = 6778.1km
$$

Since the orbit is symmetric, I will be only considering the time spent between $h = h_{min}$ to $h = h_a$. Doubling this value should give me the time spent the two instances of $h_{min}$. But before that, some preliminary values:

$$
e = \frac{r_a - r_p}{r_a + r_p}
$$

$$
e = \frac{6978.1km - 6578.1km}{6978.1km + 6578.1km} = 0.0295
$$

$$
a = \frac{r_a + r_p}{2}
$$

$$
a = \frac{6978.1km + 6578.1km}{2} = 6778.1km
$$

True anomalies:

$$
r = \frac{a (1 - e^2)}{1 + e \cos \theta}
$$

$$
1 + e \cos \theta = \frac{a}{r} (1 - e^2)
$$

$$
e \cos \theta = \frac{a}{r} (1 - e^2) - 1
$$

$$
\cos \theta = \frac{a}{r e} (1 - e^2) - \frac{1}{e}
$$

$$
\theta = \arccos \left( \frac{a}{r e} (1 - e^2) - \frac{1}{e} \right)
$$

$$
\theta_0 = \arccos \left( \frac{6778.1km}{6778.1km * 0.0295} (1 - 0.0295^2) - \frac{1}{0.0295} \right) = 1.600rad
$$

$$
\theta_1 = \pi
$$

Eccentric anomalies:

$$
\tan \frac{\theta}{2} = \sqrt{\frac{1 + e}{1 - e}} \tan \frac{E}{2}
$$

$$
\sqrt{\frac{1 - e}{1 + e}} \tan \frac{\theta}{2} = \tan \frac{E}{2}
$$

$$
E = 2 \arctan \left( \sqrt{\frac{1 - e}{1 + e}} \tan \frac{\theta}{2} \right)
$$

$$
E_0 = 2 \arctan \left( \sqrt{\frac{1 - e}{1 + e}} \tan \frac{\theta_0}{2} \right)
$$

$$
E_0 = 2 \arctan \left( \sqrt{\frac{1 - 0.0295}{1 + 0.0295}} \tan \frac{1.600rad}{2} \right) = 1.571rad
$$

$$
E_1 = \pi
$$

Mean anomalies will be implicit:

$$
M = E - e \sin E
$$

$$
M_0 = E_0 - e \sin E_0
$$

$$
M_0 = 1.571 - 0.0295 \sin 1.571rad = 1.542rad
$$

$$
M_1 = \pi - \cancel{e \sin \pi} = \pi
$$

Times:

$$
M = \sqrt{\frac{\mu}{a^3}} t
$$

$$
t = M \sqrt{\frac{a^3}{\mu}}
$$

$$
t_0 = M_0 \sqrt{\frac{a^3}{\mu}}
$$

$$
t_0 = 1.542 * \sqrt{\frac{(6778.1km)^3}{3.98600 * 10^5 km^3/s^2}} = 1362.9s
$$

$$
t_1 = \pi * \sqrt{\frac{a^3}{\mu}}
$$

$$
t_1 = \pi * \sqrt{\frac{(6778.1km)^3}{3.98600 * 10^5 km^3/s^2}} = 2776.8s
$$

$$
\Delta t = 2 (t_1 - t_0)
$$

$$
\Delta t = 2 (t_1 - t_0) = 2 (2776.8s - 1362.9s) = \boxed{2827.8s}
$$

## 3.

Given:

$$
r_p = 7500km
$$

$$
r_a = 16000km
$$

$$
\theta_0 = 80\degree = 1.3963rad
$$

$$
\Delta t = 40min = 2400s
$$

From the internet:

$$
\mu = 3.98600 * 10^5 km^3/s^2
$$

Preliminary:

$$
e = \frac{r_a - r_p}{r_a + r_p}
$$

$$
e = \frac{16000km - 7500km}{16000km + 7500km} = 0.3617
$$

$$
a = \frac{r_a + r_p}{2}
$$

$$
a = \frac{16000km + 7500km}{2} = 11750km
$$

Time at $\theta_0$:

$$
E_0 = 2 \arctan \left( \sqrt{\frac{1 - e}{1 + e}} \tan \frac{\theta_0}{2} \right)
$$

$$
E_0 = 2 \arctan \left( \sqrt{\frac{1 - 0.3617}{1 + 0.3617}} \tan \frac{1.3963rad}{2} \right) = 1.0429rad
$$

$$
M_0 = E_0 - e \sin E_0
$$

$$
M_0 = 1.0429 - 0.3617 \sin 1.0429rad = 0.7304rad
$$

$$
t_0 = M_0 \sqrt{\frac{a^3}{\mu}}
$$

$$
t_0 = 0.7304 * \sqrt{\frac{(11750km)^3}{3.98600 * 10^5 km^3/s^2}} = 1473.5s
$$

$$
t_1 = t_0 + \Delta t = 1473.5s + 2400s = 3873.5s
$$

Eccentric anomaly at $t_1$:

$$
M = \sqrt{\frac{\mu}{a^3}} t
$$

$$
M_1 = \sqrt{\frac{\mu}{a^3}} t_1
$$

$$
M_1 = \sqrt{\frac{3.98600 * 10^5 km^3/s^2}{(11750km)^3}} * 3873.5s = 1.9201rad
$$

Newton-Raphson:

$$
E_{i+1} = E_i - \frac{E_i - e \sin E_i - M}{1 - e \cos E_i}
$$

According to the internet, I have a couple of options for choosing a good starting $E$ guess. Also, I am just realizing that I am using $E_0$ to describe the $E$ at $\theta_0$ and $E_0$ again for the starting guess. Oops. Let's call the guess $E_a$. But to keep things simple, I will just be using the previous $E$:

$$
E_a = E_0
$$

$$
E_b = E_a - \frac{E_a - e \sin E_a - M_1}{1 - e \cos E_a}
$$

$$
E_b = 1.0429 - \frac{1.0429 - 0.3617 \sin 1.0429 - 1.9201}{1 - 0.3617 \cos 1.0429} = 2.498
$$

$$
E_1 \approx E_c = 2.498 - \frac{2.498 - 0.3617 \sin 2.498 - 1.9201}{1 - 0.3617 \cos 2.498} = 2.218
$$

The second angle:

$$
\tan \frac{\theta}{2} = \sqrt{\frac{1 + e}{1 - e}} \tan \frac{E}{2}
$$

$$
\theta = 2 \arctan \left( \sqrt{\frac{1 + e}{1 - e}} \tan \frac{E}{2} \right)
$$

$$
\theta_1 = 2 \arctan \left( \sqrt{\frac{1 + e}{1 - e}} \tan \frac{E_1}{2} \right)
$$

$$
\theta_1 = 2 \arctan \left( \sqrt{\frac{1 + 0.3617}{1 - 0.3617}} \tan \frac{2.218}{2} \right) = \boxed{142.4\degree}
$$

## 4.

Given:

$$
r_p = 6600km
$$

$$
v_p = 1.2 v_{esc}
$$

$$
\theta_0 = -90\degree = - \frac{\pi}{2}
$$

$$
\theta_1 = 90\degree = \frac{\pi}{2}
$$

From the Internet:

$$
\mu = 3.98600 * 10^5 km^3/s^2
$$

Escape velocity:

$$
v_{esc} = \sqrt{\frac{2 \mu}{r}} = \sqrt{\frac{2 \mu}{r_p}}
$$

$$
v_{esc} = \sqrt{\frac{2 * 3.98600 * 10^5 km^3/s^2}{6600km}} = 10.99km/s
$$

Perigee velocity:

$$
v_p = 1.2 v_{esc} = 1.2 * 10.99km/s = 13.19km/s
$$

Eccentricity:

$$
v_p = \frac{\mu}{h} (1 + e) = \frac{\mu}{r_p v_p} (1 + e)
$$

$$
\frac{r_p v_p^2}{\mu} = 1 + e
$$

$$
e = \frac{r_p v_p^2}{\mu} - 1 = \frac{6600km * (13.19km/s)^2}{3.98600 * 10^5 km^3/s^2} - 1 = 1.881
$$

Hyperbolic anomaly:

$$
\tan \frac{\theta}{2} = \sqrt{\frac{e + 1}{e - 1}} \tanh \frac{F}{2}
$$

$$
F = 2 \operatorname{arctanh} \left( \sqrt{\frac{e - 1}{e + 1}} \tan \frac{\theta}{2} \right)
$$

$$
F_0 = 2 \operatorname{arctanh} \left( \sqrt{\frac{e - 1}{e + 1}} \tan \frac{\theta_0}{2} \right)
$$

$$
F_0 = 2 \operatorname{arctanh} \left( \sqrt{\frac{1.881 - 1}{1.881 + 1}} \tan \frac{- \frac{\pi}{2}}{2} \right) = -1.245
$$

$$
F_1 = 2 \operatorname{arctanh} \left( \sqrt{\frac{1.881 - 1}{1.881 + 1}} \tan \frac{\frac{\pi}{2}}{2} \right) = 1.245
$$

Mean anomalies:

$$
M = e \sinh F - F
$$

$$
M_0 = 1.881 \sinh -1.245 - (-1.245) = -1.750
$$

$$
M_1 = 1.881 \sinh 1.245 - 1.245 = 1.750
$$

Semi-major axis:

$$
v^2 = \mu \left( \frac{2}{r} - \frac{1}{a} \right)
$$

$$
\frac{v^2}{\mu} = \frac{2}{r} - \frac{1}{a}
$$

$$
\frac{2}{r} - \frac{v^2}{\mu} = \frac{1}{a}
$$

$$
a = \left[ \frac{2}{r} - \frac{v^2}{\mu} \right]^{-1} = \left[ \frac{2}{r_p} - \frac{v_p^2}{\mu} \right]^{-1}
$$

$$
a = \left[ \frac{2}{6600km} - \frac{(13.19km/s)^2}{3.98600 * 10^5 km^3/s^2} \right]^{-1} = -7494km
$$

Times:

$$
M = \sqrt{\frac{\mu}{-a^3}} t
$$

$$
t = \sqrt{\frac{-a^3}{\mu}} M
$$

$$
t_0 = \sqrt{\frac{-a^3}{\mu}} M_0 = \sqrt{\frac{-(-7494km)^3}{3.98600 * 10^5 km^3/s^2}} (-1.750) = -1798.21s
$$

$$
t_1 = \sqrt{\frac{-a^3}{\mu}} M_1 = \sqrt{\frac{-(-7494km)^3}{3.98600 * 10^5 km^3/s^2}} (1.750) = 1798.21s
$$

$$
\Delta t = t_1 - t_0 = 2 t_0 = 2 * 1798.21s = \boxed{3596.4s}
$$

Should've used symmetry, oh well.

## 5.

This problem doesn't actually mention what planet we're orbiting. A $T = 13082.26s$ roughly corresponding to a typical low-Earth orbit, so I am assuming this is Earth. Nevertheless, here is the code for the code for the preliminary before Q1 and Q2:

```m
r_0 = [-3205.996075776849; -6362.271475420068; -1040.716500858713];
r_dot_0 = [7.430811747148; -3.172540334054; -3.496235935739];
T = 13082.26;
N = 361;

y0 = [r_0; r_dot_0];
t_space = linspace(0, T, N);

[t, y1] = ode45(@orbit, t_space, y0);

plot3(y1(:, 1), y1(:, 2), y1(:, 3));
xlabel('x (km)');
ylabel('y (km)');
zlabel('z (km)');
grid on;

function dy_dt = orbit(~, y)
    mu = 3.98600 * 10 ^ 5;

    r = y(1:3);
    r_dot = y(4:6);

    r_abs = norm(r);
    r_ddot = -mu * r / r_abs ^ 3;

    dy_dt = [r_dot; r_ddot];
end
```

The plot:

![](https://i.imgur.com/dBou8Jp.png)

As for the first sub-question, this is my implementation for `kepl_to_cart`:

```m
function [x, y, z, x_dot, y_dot, z_dot] = kepl_to_cart(a, ecc, argp, raan, inc, theta, mu)
    e = ecc;

    p = a * (1 - e ^ 2);
    r_abs = p / (1 + e * cos(theta));

    r_e = r_abs * cos(theta);
    r_p = r_abs * sin(theta);
    r_k = 0;

    v_e = -sqrt(mu / p) * sin(theta);
    v_p = sqrt(mu / p) * (e + cos(theta));
    v_k = 0;

    R = rot_313(raan, inc, argp);
    r = R * [r_e; r_p; r_k];
    v = R * [v_e; v_p; v_k];

    x = r(1);
    y = r(2);
    z = r(3);
    x_dot = v(1);
    y_dot = v(2);
    z_dot = v(3);
end
```

And the script that plots the orbit:

```m
mu = 3.98600 * 10 ^ 5;

a = 12000;
ecc = 0.4;
argp = deg2rad(200);
raan = deg2rad(45);
inc = deg2rad(25);

theta_0 = 0;
theta_1 = deg2rad(360);
d_theta = deg2rad(1);

theta = theta_0:d_theta:theta_1;

N = numel(theta);
y2 = zeros(N, 6);

for i = 1:N
    th = theta(i);
    [x, y, z, x_dot, y_dot, z_dot] = kepl_to_cart(a, ecc, argp, raan, inc, th, mu);

    y2(i, :) = [x, y, z, x_dot, y_dot, z_dot];
end

plot3(y2(:, 1), y2(:, 2), y2(:, 3));
xlabel('x (km)');
ylabel('y (km)');
zlabel('z (km)');
grid on;
```

The plot:

![](https://i.imgur.com/Sqyr8o8.png)

This is undeniably the exact same orbit. Onto the second sub-question which requires the inverse of `cart_to_kepl` called `kepl_to_cart`:
