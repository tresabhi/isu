rng default

global Mt
global Rt
global Dt

x = lhsdesign(10, 2, 'smooth', 'off');
x = round(x, 3);

Mt = x(:, 1);
Rt = x(:, 2);
Dt = (Mt - 0.3) .^ 2 + (Rt - 0.5) .^ 2 + 1;

figure(1)
plot(Mt, Rt, 'ko')

options = optimoptions('fmincon', 'Display', 'iter', 'Algorithm', 'sqp');

x0 = zeros(12, 1);

[xOpt, fOpt] = fmincon("objFunc", x0, [], [], [], [], [], [], [], options);

w = zeros(9);
b = zeros(3);

for i = 1:9
    w(i) = xOpt(i);
end

b(1) = xOpt(10);
b(2) = xOpt(11);
b(3) = xOpt(12);
