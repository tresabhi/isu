% x is a list of x values and same goes for y
% a and b are used in the least square line of best fit y = a + bx
function [a, b] = problem_2_lin_lsqfit(x, y)
% get the size of the list
n = length(x);

% get all the sums required
s1 = sum(x);
s2 = sum(y);
s3 = sum(x .^ 2);
s4 = sum(x .* y);

% ditch the matrices and directly implement the algebra
a = (s2 * s3 - s4 * s1) / (n * s3 - s1 * s1);
b = (s4 * n - s2 * s1) / (n * s3 - s1 * s1);
end