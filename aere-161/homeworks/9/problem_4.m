% declare lower and upper bounds
a = 4 * 10 ^ -5;
b = 7 * 10 ^ -5;

% use trapezoid rule function with decreasing step sizes
E1 = problem_4_trapezoid(a, b, 0.6 * 10 ^ -5);
E2 = problem_4_trapezoid(a, b, 0.3 * 10 ^ -5);
E3 = problem_4_trapezoid(a, b, 0.15 * 10 ^ -5);

% print results
fprintf('Approximation 1: E = %f\n', E1);
fprintf('Approximation 2: E = %f\n', E2);
fprintf('Approximation 3: E = %f\n', E3);