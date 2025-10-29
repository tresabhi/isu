x0 = [2; 2];
options = optimoptions("fmincon", "Display", "iter", "Algorithm", "sqp");

% h = 5x_1 - 6x_2 + 7 = 0
% g1 = 2x_1 + 3x_2 - 4 <= 0
% g2 = x_1 - 9x_2 - 10 <= 0
% convert these into A * x <= b

A = [2, 3; 1, -9];
b = [4; 10];

Aeq = [5, -6];
beq = -7;

[xOpt, fOpt, exitFlag, output, lambda] = fmincon("objFunc", x0, A, b, Aeq, beq, [], [], [], options);

disp(xOpt);
disp(fOpt);
disp(exitFlag);
disp(output);
disp(lambda);
