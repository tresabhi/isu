x0 = [1; 2; 3];

% h = x(1) + 2 * x(2) = 6
% g1 = x(1) - 2 * x(2) + 2 * x(3) <= 4
% g2 = x(2) + 3 * x(3) <= 6
% g3 = x(1) ^ 3 + x(2) ^ 2 - 2 * x(1) * x(3) <= 0
% g4 = 3 * x(1) - 2 * x(2) <= 2

A = [1, -2, 2; 0, 1, 3; 3, -2, 0];
b = [4; 6; 2];

Aeq = [1, 2, 0];
beq = 6;

options = optimoptions("fmincon", "Display", "iter", "Algorithm", "sqp");
[xOpt, fOpt, exitFlag, output, lambda] = fmincon(@objFunc, x0, A, b, Aeq, beq, [], [], @nlCon, options);

disp("Optimal point x* =");
disp(xOpt);

disp("Optimal objective f* =");
disp(fOpt);

disp("Baseline objective f0 =");
disp(objFunc(x0));

function [c, ceq] = nlCon(x)
    c(1) = x(1) ^ 3 + x(2) ^ 2 - 2 * x(1) * x(3);
    ceq = [];
end

function f = objFunc(x)
    f = x(1) ^ 2 + 2 * x(2) ^ 2 + 2 * x(3) ^ 2 - 2 * x(1) * x(3) - x(1) * x(2);
end
