%{
  Abhigyaan Deep, AER E 161, Homework 5
  Purpose: compare the best options for a student's mean and median
%}

clear, clc

% Scenario 1: Grades 99, 88, and 95
grades1 = [99, 88, 95];

% Scenario 2: Grades 99, 70, and 77
grades2 = [99, 70, 77];

% Calculate mean and median for Scenario 1
mean1 = mean(grades1);
median1 = median(grades1);

% Calculate mean and median for Scenario 2
mean2 = mean(grades2);
median2 = median(grades2);

% Display results
fprintf('Scenario 1:\n');
fprintf('Mean: %.2f\n', mean1);
fprintf('Median: %.2f\n\n', median1);

fprintf('Scenario 2:\n');
fprintf('Mean: %.2f\n', mean2);
fprintf('Median: %.2f\n', median2);

% Determine which measure is better for each scenario
if abs(mean1 - median1) < abs(mean2 - median2)
  fprintf('In Scenario 1, the mean is closer to the median, so using the mean might be better.\n');
else
  fprintf('In Scenario 2, the median is closer to the mean, so using the median might be better.\n');
end