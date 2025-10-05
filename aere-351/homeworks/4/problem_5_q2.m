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

y3 = zeros(N, 6);

for i = 1:N
    [a_i, ecc_i, argp_i, raan_i, inc_i, theta_kepl] = cart_to_kepl( ...
        y2(i, 1), y2(i, 2), y2(i, 3), y2(i, 4), y2(i, 5), y2(i, 6), mu);

    y3(i, :) = [a_i, ecc_i, argp_i, raan_i, inc_i, theta_kepl];
end

figure;

subplot(3, 2, 1);
plot(rad2deg(theta), y3(:, 1));
xlabel('True anomaly (deg)');
ylabel('a (km)');
title('Semi-major axis');

subplot(3, 2, 2);
plot(rad2deg(theta), y3(:, 2));
xlabel('True anomaly (deg)');
ylabel('Eccentricity');
title('Eccentricity');

subplot(3, 2, 3);
plot(rad2deg(theta), rad2deg(y3(:, 3)));
xlabel('True anomaly (deg)');
ylabel('Argument of perigee (deg)');
title('Argument of Perigee');

subplot(3, 2, 4);
plot(rad2deg(theta), rad2deg(y3(:, 4)));
xlabel('True anomaly (deg)');
ylabel('RAAN (deg)');
title('Right Ascension of Ascending Node');

subplot(3, 2, 5);
plot(rad2deg(theta), rad2deg(y3(:, 5)));
xlabel('True anomaly (deg)');
ylabel('Inclination (deg)');
title('Inclination');

subplot(3, 2, 6);
plot(rad2deg(theta), rad2deg(y3(:, 6)));
xlabel('True anomaly (deg)');
ylabel('True anomaly (deg)');
title('True Anomaly');
