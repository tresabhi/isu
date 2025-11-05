n = 10000;

mean_2 = 1;
mean_3 = 1;

std_2 = 0.06;
std_3 = 0.2;

x1 = 1;
x2 = std_2 .* randn(n, 1) + mean_2;
x3 = std_3 .* randn(n, 1) + mean_3;

f = x1 .^ 2 + 2 .* x2 .^ 2 + 3 .* x3 .^ 2;

histogram(f, 20);
