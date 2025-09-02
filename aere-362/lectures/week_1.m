[D, H] = meshgrid(3.5:0.25:8, 8:0.25:18);

f = pi * D .* H + (pi / 2) .* D .^ 2;

c_levels = 0:20:1000;
fc = contour(D, H, f, c_levels, "k");
clabel(fc);

g = 400 - (pi / 4) * (D .^ 2 .* H);
infeasible_levels = 0:0.1:20;
hold on;

contour(D, H, g, infeasible_levels, "c");
contour(D, H, g, [0, 0], "k");
