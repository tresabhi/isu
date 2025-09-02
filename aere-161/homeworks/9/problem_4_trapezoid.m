function E = problem_4_trapezoid(a, b, h)
% Purpose
T = 3500; % the temperature in kelvins
n = (b - a) / h; % the number of intervals

% the function as the integrand
f = @(x) x ^ (-5) * (exp(1.432 / (T * x)) - 1) ^ (-1);

s = 0; % the inner trapezoidal sum
for i = 1 : n - 1 % loop through the intervals
  % add to the accumulator
  s = s + f(a + i * h);
end % end loop

% perform the trapezoidal rule
Integr = 0.5 * h * (f(a) + 2 * s + f(b));
% apply the rest of the efficiency formula
E = 64.77 * T ^ (-4) * Integr;
end