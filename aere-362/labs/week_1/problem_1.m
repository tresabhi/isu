[x1, x2] = meshgrid(-10:0.2:10, -10:0.2:10);

f = 2 * (x1 - 1) .^ 2 + 3 * (x2 - 2) .^ 2;

c_levels = 0:10:100;
fc = contour(x1, x2, f, c_levels, "k");
clabel(fc);

g1 = x1 - x2;
g2 = x2;
hold on;

infeasible_levels = 0:0.05:0.4;
contour(x1, x2, g1, infeasible_levels, "c");
contour(x1, x2, g2, infeasible_levels, "c");

contour(x1, x2, g1, [0, 0], "k");
contour(x1, x2, g2, [0, 0], "k");
