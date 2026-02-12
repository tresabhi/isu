% Group 2 Quiz 4
% Aero and Prop lab

clear, clc, clf

tbl = readtable('quiz4_data.xlsx');
avgtbl = mean(tbl(:, 2));
time = table2array(tbl(:, 1));
value = table2array(tbl(:, 2));

plot(time, value, ".", "Color", "#a0a0FF");
hold on;
xlabel('Time (s)');
ylabel('Value');
title('Evolution of Data Points in Time');
axis padded

N = length(time);
delta = N * sum(time .^ 2) - ((sum(time)) .^ 2);
m = ((N .* sum(time .* value)) - (sum(time) .* sum(value))) ./ delta;
b = ((sum(value) .* sum(time .^ 2)) - (sum(time .* value) .* sum(time))) / delta;

x = min(time):max(time);
y = m * x + b;
plot(x, y, 'Color', '#0000FF', 'LineStyle', '--')

sigma = std(value - (m .* time) - b);
sigmam = sqrt(N * (sigma ^ 2) / delta);
sigmab = sqrt((sigma ^ 2) * sum(time .^ 2) / delta);
