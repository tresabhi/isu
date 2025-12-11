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
nu = imag(eigenvalues(1));

omega_n = sqrt(sigma ^ 2 + nu ^ 2);
zeta = -sigma / omega_n;

disp('omega_n =')
disp(omega_n)

disp('zeta =')
disp(zeta)
