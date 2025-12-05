x0 = [0.1; 0.1; 1; 1];
options = optimoptions("fmincon", "Display", "iter", "Algorithm", "sqp");

fmincon("objFunc", x0, [], [], [], [], [], [], "nlConst", options);
