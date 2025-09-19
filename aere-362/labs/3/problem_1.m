clear, close

syms f(x1, x2)

f(x1, x2) = x1 ^ 2 + 2 * x2 ^ 2 - 4 * x1 - 2 * x1 * x2;

df_dx1 = diff(f, x1);
df_dx2 = diff(f, x2);

[C1, T1] = coeffs(df_dx1, "All");
[C2, T2] = coeffs(df_dx2, "All");

C1 = double(C1);
C2 = double(C2);

a11 = C1(1, 2);
a12 = C1(2, 1);
a21 = C2(1, 2);
a22 = C2(2, 1);

A = [a11, a12; a21, a22];

b1 = -C1(2, 2);
b2 = -C2(2, 2);
b = [b1; b2];

x0_pt = A \ b;

h11 = diff(df_dx1, x1);
h12 = diff(df_dx1, x2);
h21 = diff(df_dx2, x1);
h22 = diff(df_dx2, x2);

H = double([h11, h12; h21, h22]);

eigenvalues = eig(H);

[x1_grid, x2_grid] = meshgrid(-10:0.1:10, -10:0.1:10);
f_grid = f(x1_grid, x2_grid);
c_levels = 0:10:100;
fc = contour(x1_grid, x2_grid, f_grid, c_levels, "k");

clabel(fc); hold on;
plot (x0_pt(1), x0_pt(2), "rx");
