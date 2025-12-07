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
