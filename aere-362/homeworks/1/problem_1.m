[b, d] = meshgrid(0.1:1:40, 0.1:1:40);

% I find working with base units much better than the suggested cm and N

% cm to m
b = b / 100;
d = d / 100;

f = b .* d;

c_levels = 0:100:1000;

% cm^2 to m^2
c_levels = c_levels / (100 ^ 2);

fc = contour(b, d, f, c_levels, "k");
clabel(fc);
hold on;

% stress constraint
M = 120 * 10 ^ 3;
sigma_a = 210 * 10 ^ 6;
g_sigma = (5 * M) ./ (b .* d .^ 2) - sigma_a;
infeasible_levels = 0:(10 ^ 6):(3 * 10 ^ 7);

contour(b, d, g_sigma, infeasible_levels, "c");
g_sigma_c = contour(b, d, g_sigma, [0, 0], "k");
clabel(g_sigma_c);

% shear constraint
V = 400 * 10 ^ 3;
tau_a = 60 * 10 ^ 6;
g_tau = V ./ (b .* d) - tau_a;
infeasible_levels = 0:(10 ^ 6):(2 * 10 ^ 7);

contour(b, d, g_tau, infeasible_levels, "c");
g_tau_c = contour(b, d, g_tau, [0, 0], "k");
clabel(g_tau_c);

% ratio constraint
g_ratio = d - 2 .* b;
infeasible_levels = 0:0.001:0.01;

contour(b, d, g_ratio, infeasible_levels, "c");
g_ratio_c = contour(b, d, g_ratio, [0, 0], "k");
clabel(g_ratio_c);

text(0.25, 0.25, "Feasible Area", "VerticalAlignment", "top");
text(0.15, 0.3, "Ratio Constraint", "VerticalAlignment", "top");
text(0.2, 0.12, "Stress Constraint", "VerticalAlignment", "top");
text(0.1, 0.06, "Shear Constraint", "VerticalAlignment", "top");

xlabel("b (in meters)");
ylabel("d (in meters)");
