# AERE 355 Homework 6

## 1.

Following the matrix equation listed on page 9 in the chapter 5 notes, along with `ode45`, I came up with the following MATLAB code (with an anonymous function wrapping the `dynamics` function to pass the variables declared in `plot_dynamics`):

```m
plot_dynamics(deg2rad(2));
plot_dynamics(deg2rad(10));
legend('\delta_r = 2 deg', '\delta_r = 10 deg');

function plot_dynamics(delta_r)
    zeta = 0.2;
    omega_n = 3.142;
    g_s = -0.9;

    T = 4 * 2 * pi / omega_n;

    x_0 = [0; 0];

    [t, x] = ode45(@(~, x) dynamics(x, zeta, omega_n, g_s, delta_r), [0, T], x_0);

    plot(t, x(:, 2));
    hold on;
    grid on;

    xlabel('Time (s)');
    ylabel('\psi (deg)');

    function x_dot = dynamics(x, zeta, omega_n, g_s, delta_r)
        A = [
             -2 * zeta * omega_n, -omega_n ^ 2;
             1, 0
             ];
        B = [
             g_s * omega_n ^ 2;
             0
             ];

        x_dot = A * x + B * delta_r;
    end

end
```

This creates a pretty plot:

![](https://i.imgur.com/4JNWIp3.png)

For airplane B, I forked the code from airplane A:

```m
plot_dynamics(deg2rad(2));
plot_dynamics(deg2rad(10));
legend('\delta_r = 2 deg', '\delta_r = 10 deg');

function plot_dynamics(delta_r)
    zeta = 0.4;
    omega_n = 1.257;
    g_s = -1.2;

    T = 4 * 2 * pi / omega_n;

    x_0 = [0; 0];

    [t, x] = ode45(@(~, x) dynamics(x, zeta, omega_n, g_s, delta_r), [0, T], x_0);

    plot(t, x(:, 2));
    hold on;
    grid on;

    xlabel('Time (s)');
    ylabel('\psi (deg)');

    function x_dot = dynamics(x, zeta, omega_n, g_s, delta_r)
        A = [
             -2 * zeta * omega_n, -omega_n ^ 2;
             1, 0
             ];
        B = [
             g_s * omega_n ^ 2;
             0
             ];

        x_dot = A * x + B * delta_r;
    end

end
```

This produces the following plot:

![](https://i.imgur.com/bpFMrnO.png)

And for the third plot with both variations and 2 airplanes, I produced the following MATLAB code with extra extra thick lines because the dotted lines were hard to see:

```m
plot_dynamics(0.2, 3.142, -0.9, deg2rad(2), '-');
plot_dynamics(0.2, 3.142, -0.9, deg2rad(10), ':');
plot_dynamics(0.4, 1.257, -1.2, deg2rad(2), '-');
plot_dynamics(0.4, 1.257, -1.2, deg2rad(10), ':');

legend( ...
    '\zeta = 0.2, \delta_r = 2 deg', ...
    '\zeta = 0.2, \delta_r = 10 deg', ...
    '\zeta = 0.4, \delta_r = 2 deg', ...
    '\zeta = 0.4, \delta_r = 10 deg' ...
);

function plot_dynamics(zeta, omega_n, g_s, delta_r, style)
    T = 2 * pi / omega_n;

    A = [
         -2 * zeta * omega_n, -omega_n ^ 2;
         1, 0
         ];
    B = [
         g_s * omega_n ^ 2;
         0
         ];

    x_0 = [0; 0];
    x_ss = -A \ (B * delta_r);

    [t, x] = ode45(@(~, x) dynamics(x, A, B, delta_r), [0, 4 * T], x_0);

    phi = x(:, 2);
    phi_ss = x_ss(2);

    t_normalized = t / T;
    phi_normalized = phi / phi_ss;

    plot(t_normalized, phi_normalized, style, 'LineWidth', 2);
    hold on;
    grid on;

    xlabel('Normalized time');
    ylabel('Normalized \psi');

    function x_dot = dynamics(x, A, B, delta_r)
        x_dot = A * x + B * delta_r;
    end

end
```

This gives the plot:

![](https://i.imgur.com/pQMJqrP.png)

## 2.

Before I can jump into the programming, I need to mangle the standard form:

$$
\tau = \frac{-1}{L_p}
$$

$$
g_s = -\frac{L_{\delta_a}}{L_p}
$$

And the standard form:

$$
\tau \Delta \dot{p} + p = g_s \Delta \delta_a
$$

But really, I don't care about the fact that it's a small nudge:

$$
\tau \dot{p} + p = g_s \delta_a
$$

$$
\tau \dot{p} = - p + g_s \delta_a
$$

$$
\dot{p} = \frac{-1}{\tau} p + \frac{g_s}{\tau} \delta_a
$$

This can be thrown at `ode45`, plotted for just 4 seconds:

```m
delta_a = deg2rad(5);

rho = 2.3769e-3;

M = 0.4;
a = 1116.45;
u_0 = M * a;

Q = (1/2) * rho * u_0 ^ 2;

S = 260;
b = 27.5;
I_x = 8090;

C_l_p = -0.26;
C_l_delta_a = 0.08;

L_p = (C_l_p * (b / (2 * u_0)) * Q * S * b) / I_x;
L_delta_a = (C_l_delta_a * Q * S * b) / I_x;

tau = -1 / L_p;
g_s = -L_delta_a / L_p;

T = 4;
p_0 = [0; 0];

p_dot = @(~, p) (-1 / tau) * p + (g_s / tau) * delta_a;

[t, p] = ode45(p_dot, [0, T], p_0);

plot(t, rad2deg(p))
xlabel('Time (s)')
ylabel('p (deg/s)')
grid on
```

And this gives the plot:

![](https://i.imgur.com/wTekPqa.png)

## 3.

![](https://i.imgur.com/YWWEU7H.png)

The left most root is the roll mode:

$$
s_1 = \boxed{-7 rad/s}
$$

The one with the imaginary parts is the dutch roll:

$$
s_{2,3} = \boxed{(-2 \pm 3i) rad/s}
$$

And the one close to the origin, or the one to the right is the spiral mode:

$$
s_4 = \boxed{-0.5 rad/s}
$$

Doubling time:

$$
e^{\Re(s) t} = k = 2
$$

$$
t = \frac{\ln k}{\Re(s)} = \frac{\ln 2}{\Re(s)}
$$

Halving time:

$$
t = \frac{\ln \frac{1}{2}}{\Re(s)} = -\frac{\ln 2}{\Re(s)}
$$

So, really, when I am using the doubling time and if the result is negative, I should've used the halving time. And since they all have negative real parts, I will always be using the halving timeL

$$
t_1 = -\frac{\ln 2}{-7 rad/s} = \boxed{0.09902 s}
$$

$$
t_{2,3} = -\frac{\ln 2}{-2 rad/s} = \boxed{0.3466 s}
$$

$$
t_4 = -\frac{\ln 2}{-0.5 rad/s} = \boxed{1.39 s}
$$
