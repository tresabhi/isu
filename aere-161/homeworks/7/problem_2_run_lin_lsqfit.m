clear, clc

% load problem_data.txt into data
data = load('problem_data.txt');
x = data(:, 1); % get the first column as x
y = data(:, 2); % get the second column as y

% call the function
[a, b] = problem_2_lin_lsqfit(x, y);

% plot all the points
plot(x, y, 'o');
hold on

% plot the line
plot(x, a + b * x);
hold off

% add labels
title(sprintf('Approximation: y = %f + %fx', a, b))
xlabel('x')
ylabel('y')

% add legend
legend('Points', 'Approximation')