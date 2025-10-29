x0 = [2; 2];
options = optimoptions("fmincon", "Display", "iter", "Algorithm", "sqp");

% linear constraint: h = 2x_1 + 3x_2 - 4 = 0 -> Aeq * x = beq
Aeq = [2, 3];
beq = 4;

[xOpt, fOpt, exitFlag, output, lambda] = fmincon("objFunc", x0, [], [], Aeq, beq, [], [], [], options);

disp(xOpt);
disp(fOpt);
disp(exitFlag);
disp(output);
disp(lambda);
