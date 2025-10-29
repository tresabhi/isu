x0 = [5; 5; 5];
options = optimoptions("fmincon", "Display", "iter", "Algorithm", "sqp");

A = [2, 3, -1; 1, -9, 0];
b = [4; 10];

Aeq = [5, -6, 2];
beq = -7;

[xOpt, fOpt, exitFlag, output, lambda] = fmincon("objFunc", x0, A, b, Aeq, beq, [], [], "nlCon", options);

disp(xOpt);
disp(fOpt);
disp(exitFlag);
disp(output);
disp(lambda);
