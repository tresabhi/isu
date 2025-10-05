r_0 = [-3205.996075776849; -6362.271475420068; -1040.716500858713];
r_dot_0 = [7.430811747148; -3.172540334054; -3.496235935739];
T = 13082.26;
N = 361;

y0 = [r_0; r_dot_0];
t_space = linspace(0, T, N);

[t, y] = ode45(@orbit, t_space, y0);

plot3(y(:, 1), y(:, 2), y(:, 3));
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
