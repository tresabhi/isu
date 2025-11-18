A = [-2 0 1; 0 0 1; -10 -15 0];
B = [0; 0; -5];
X_0 = [0; 0; 0];
delta_0 = 1;

f = @(t, x) A * x + B * delta_0;

[t, x] = ode45(f, [0, 10], X_0);

disp("Eigenvalues of A:")
disp(eig(A))

plot(t, x)
legend('\alpha', '\theta', 'd\theta/dt')
xlabel('t')
ylabel('X')
