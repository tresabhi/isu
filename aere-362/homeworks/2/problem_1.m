d_0 = [1; -1];
d_1 = [2; -1];

alpha_0 = 1.5;
alpha_1 = 2;

x_super_0 = [-5; 3];
x_super_1 = x_super_0 + alpha_0 * d_0;
x_super_2 = x_super_1 + alpha_1 * d_1;

[x1, x2] = meshgrid(-6:0.1:6, -6:0.1:6);
f = 4 * x1 .^ 2 + 3 .* x1 .* x2 + 2 .* x2 .^ 2 - 2;

c_levels = -30:20:300;
fc = contour(x1, x2, f, c_levels, "k");
clabel(fc);

hold on;

plot(x_super_0(1), x_super_0(2), "ro");
plot(x_super_1(1), x_super_1(2), "ro");
plot(x_super_2(1), x_super_2(2), "ro");

text(x_super_0(1), x_super_0(2), "x^0", "VerticalAlignment", "bottom", "HorizontalAlignment", "left");
text(x_super_1(1), x_super_1(2), "x^1", "VerticalAlignment", "bottom", "HorizontalAlignment", "left");
text(x_super_2(1), x_super_2(2), "x^2", "VerticalAlignment", "bottom", "HorizontalAlignment", "left");

plot([x_super_0(1), x_super_1(1), x_super_2(1)], [x_super_0(2), x_super_1(2), x_super_2(2)], "r");
