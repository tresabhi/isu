l = 3;

theta_0 = -60 * (pi / 180);
t_0 = 0;
t_1 = 15;
dt = 0.5;

[t, w] = ode45(@pendulum, [t_0, t_1], [theta_0, 0]);
[t_rk, w_rk] = rk4(@pendulum, [t_0, t_1], [theta_0, 0], dt);

plot(t, w(:, 1) * l, 'b', 'DisplayName', 'Position (m)'); hold on;
plot(t, w(:, 2) * l, 'r', 'DisplayName', 'Velocity (m/s)');

plot(t_rk, w_rk(:, 1) * l, '--b', 'DisplayName', 'RK4 Position (m)'); hold on;
plot(t_rk, w_rk(:, 2) * l, '--r', 'DisplayName', 'RK4 Velocity (m/s)');

legend('show');

xlabel('Time (s)');
ylabel('Position and Velocity (see respective units)');
grid on;

function [t, w] = rk4(f, t_span, w0, dt)
    tn = t_span(1);
    wn = w0(:)';

    % I initially did a for look until the dt's added up to t_span(2)
    % but that gave the w and t arrays mismatching sizes
    N = ceil((t_span(2) - t_span(1)) / dt);
    w = zeros(N + 1, length(wn));
    t = zeros(N + 1, 1);

    t(1) = tn;
    w(1, :) = wn;

    for i = 1:N
        % transposing every time here is really bad for performance
        % but it will suffice for a homework
        k1 = f(tn, wn).';
        k2 = f(tn + dt / 2, wn + (dt / 2) * k1).';
        k3 = f(tn + dt / 2, wn + (dt / 2) * k2).';
        k4 = f(tn + dt, wn + dt * k3).';

        wn = wn + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4);
        tn = tn + dt;

        w(i + 1, :) = wn;
        t(i + 1) = tn;
    end

end

function dw_dt = pendulum(~, w)
    l = 3;
    g = 9.81;
    c = 0.06;
    m = 0.2;

    x_1_dot = w(2);
    x_2_dot = (-g / l) * sin(w(1)) - (c / m) * w(2);

    dw_dt = [x_1_dot; x_2_dot];
end
