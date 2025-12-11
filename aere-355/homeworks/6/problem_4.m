Y_beta = -7.8;
Y_delta_r = 5.236;
Y_r = 2.47;

N_r = -0.34;
N_delta_r = -0.616;
N_beta = 0.64;

u_0 = 154;

A = [
     Y_beta / u_0, - (1 - Y_r / u_0);
     N_beta, N_r
     ];
B = [
     Y_delta_r / u_0;
     N_delta_r
     ];

eigenvalues = eig(A);

disp('eigenvalues =')
disp(eigenvalues)

sigma = real(eigenvalues(1));
omega_d = imag(eigenvalues(1));

omega_n = sqrt(sigma ^ 2 + omega_d ^ 2);
zeta = -sigma / omega_n;

disp('omega_n =')
disp(omega_n)

disp('zeta =')
disp(zeta)

T = 2 * pi / omega_d;

disp('T =')
disp(T)

t_half = -log(2) / sigma;

disp('t_half =')
disp(t_half)

x_0 = [0.1; 0];
[t, x] = ode45(@(t, x) dutch_roll(x, A, B, 0), [0, 3 * T], x_0);

figure(1)
plot(t, x(:, 1))
hold on
plot(t, x(:, 2))
legend('\beta (rad)', 'r (rad/s)')
grid on
xlabel('Time (s)')
ylabel('x (m)')
title('Dutch Roll Input Response')

x_0 = [0; 0];
[t, x] = ode45(@(t, x) dutch_roll(x, A, B, 1), [0, 3 * T], x_0);

figure(2)
plot(t, x(:, 1))
hold on
plot(t, x(:, 2))
legend('\beta (rad)', 'r (rad/s)')
grid on
xlabel('Time (s)')
ylabel('x (m)')
title('Dutch Roll Step Response')

function x_dot = dutch_roll(x, A, B, delta_r)
    x_dot = A * x + B * delta_r;
end
