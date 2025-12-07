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
