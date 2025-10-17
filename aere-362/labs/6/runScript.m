rng default;

x = lhsdesign(6, 2, 'smooth', 'off');
x = round(x, 2);

global Mt;
global Rt;
global Dt;

Mt = x(:, 1);
Rt = x(:, 2);
Dt = (Mt - 0.5) .^ 2 + (Rt - 0.6) .^ 2 + 1;

figure(1);
plot(Mt, Rt, 'ko');

options = optimoptions("fmincon", "Display", "iter", "Algorithm", "sqp");

x0 = zeros(8, 1);

[xOpt, fOpt] = fmincon("objFunc", x0, [], [], [], [], [], [], [], options);

disp(xOpt);
