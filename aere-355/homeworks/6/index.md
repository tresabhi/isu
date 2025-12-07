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
