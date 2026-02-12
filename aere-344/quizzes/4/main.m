% Group 2 Quiz 4
% Aero and Prop lab

clear, clc, clf

tbl = readtable('quiz4_data.xlsx');
avgtbl = mean(tbl(:, 2));
time = table2array(tbl(:, 1));
value = table2array(tbl(:, 2));

plot(time, value)
xlabel('Time (s)');
ylabel('Value');
title('Evolution of Data Points in Time');
axis padded

N = length(time);
delta = N * sum(time .^ 2) - ((sum(time)) .^ 2);
m = ((N .* sum(time .* value)) - (sum(time) .* sum(value))) ./ delta;
b = ((sum(value) .* sum(time .^ 2)) - (sum(time .* value) .* sum(time))) / delta;

sigma = std(value - (m .* time) - b);
sigmam = sqrt(N * (sigma ^ 2) / delta);
sigmab = sqrt((sigma ^ 2) * sum(time .^ 2) / delta);
