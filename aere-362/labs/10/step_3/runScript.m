x0 = [0, 0, 2];
options = optimoptions("fmincon", "Display", "iter", "Algorithm", "sqp");

[xOpt, fOpt, exitFlag, output, lambda] = fmincon("objFunc", x0, [], [], [], [], [-1, -1, 0.1], [1, 1, 100], "nlCon", options);

propagator(xOpt, 1);
