A = [-2 0 0; 0 0 1; -10 -15 0];
B = [1 0; 0 0; 0 -5];
X_0 = [0; 0; 0];
U = [0; 1];

f = @(t, x) A * x + B * U;

[t, x] = ode45(f, [0, 10], X_0);

disp("Eigenvalues of A:")
disp(eig(A))

plot(t, x)
legend('\alpha', '\theta', 'd\theta/dt')
xlabel('t')
ylabel('X')
