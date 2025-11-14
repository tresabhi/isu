A = [-2 0 0; 0 0 1; -10 -15 0];
B = [1 0; 0 0; 0 -5];
X_0 = [0; 0; 0];

t = 0:0.01:10;
q = ones(size(t));
delta = zeros(size(t));

dt = t(2) - t(1);
X = zeros(3, length(t));
X(:, 1) = X_0;

for i = 1:length(t) - 1
    u = [q(i); delta(i)];
    X(:, i + 1) = X(:, i) + dt * (A * X(:, i) + B * u);
end

plot(t, X(1, :), 'r', t, X(2, :), 'b', t, X(3, :), 'g')
xlabel('t')
ylabel('X')
legend('alpha', 'theta', 'theta dot')
grid on
