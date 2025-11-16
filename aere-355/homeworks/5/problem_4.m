g = 32.174;
a = 1116.45;
rho = 2.3769e-3;

I_y = 126099;
W = 23904;
Mach = 0.20;
c_bar = 10.93;
S = 542.5;

C_L_0 = 0.737;
C_L_alpha = 5.0;
C_D_0 = 0.095;
C_L_u = 0;
C_D_alpha = 0.75;
C_D_u = 0;
C_m_alpha = -0.80;
C_m_alpha_dot = -3.0;
C_m_q = -8.0;

m = W / g;
u_0 = Mach * a;
Q = (1/2) * rho * u_0 ^ 2;

M_u = 0;
X_u =- (C_D_u + 2 * C_D_0) * Q * S / (m * u_0);
Z_u =- (C_L_u + 2 * C_L_0) * Q * S / (m * u_0);
X_w =- (C_D_alpha - C_L_0) * Q * S / (m * u_0);
Z_w =- (C_L_alpha + C_D_0) * Q * S / (m * u_0);

M_w = C_m_alpha * Q * S * c_bar / (u_0 * I_y);
M_w_dot = C_m_alpha_dot * (c_bar / (2 * u_0)) * Q * S * c_bar / (u_0 * I_y);
M_q = C_m_q * (c_bar / (2 * u_0)) * Q * S * c_bar / I_y;

A = [
     X_u, X_w, 0, -g;
     Z_u, Z_w, u_0, 0;
     M_u + M_w_dot * Z_u, M_w + M_w_dot * Z_w, M_w_dot * u_0 + M_q, 0;
     0, 0, 1, 0;
     ];

disp('A =')
disp(A)

lambda = eig(A);
disp('lambda =')
disp(lambda)

complex_eigenvalues = lambda(imag(lambda) ~= 0);

[~, idx_p] = min(abs(real(complex_eigenvalues)));
[~, idx_sp] = max(abs(real(complex_eigenvalues)));

lambda_p = complex_eigenvalues(idx_p);
lambda_sp = complex_eigenvalues(idx_sp);

zeta_p = -real(lambda_p) / abs(lambda_p);
zeta_sp = -real(lambda_sp) / abs(lambda_sp);

disp("zeta_p =")
disp(zeta_p)

disp("zeta_sp =")
disp(zeta_sp)
