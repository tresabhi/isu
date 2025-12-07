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
