x0 = [-4, 4];
d = [0.64, -0.768];
alphaL = 0;
alphaU = 10;
tol = 1e-3;
maxit = 100;

[alphaMin, fMin, I, iter] = golden(x0, d, alphaL, alphaU, tol, maxit);
plotLS(x0, d, alphaMin);
