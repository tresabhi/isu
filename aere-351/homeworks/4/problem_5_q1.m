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
