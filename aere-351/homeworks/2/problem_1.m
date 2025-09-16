r_0 = [5000; 10000; 2100];
r_dot_0 = [-5; 2; 1.5];
w_0 = [r_0; r_dot_0];

T = 4 * 60 * 60;

% the default settings for ode45 are too lax
options = odeset('RelTol', 1e-9, 'AbsTol', 1e-10);
[t, y] = ode45(@orbit, [0, T], w_0, options);

plot3(y(:, 1), y(:, 2), y(:, 3));
xlabel('x (km)');
ylabel('y (km)');
zlabel('z (km)');
grid on;

final_state = y(end, 1:3);
disp(final_state);

function dw_dt = orbit(~, w)
    % matlab complains if I declare this above like all other constants
    mu = 3.98 * 10 ^ 5;

    r = w(1:3);
    r_dot = w(4:6);
    % I am sure there's a built in function for this but I like component-wise
    r_cubed = (r(1) ^ 2 + r(2) ^ 2 + r(3) ^ 2) ^ (3/2);
    r_ddot = (-mu .* r) ./ r_cubed;

    dw_dt = [r_dot; r_ddot];
end
