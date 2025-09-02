%{
  Abhigyaan Deep, AER E 161, Homework 5
  Purpose: calculate the mean without min and max values
%}

clear, clc

% Create a vector of 10 random integers in the range from 0 to 50
randomVector = randi([0, 50], 1, 10);

% Display the original vector
disp('Original Vector:');
disp(randomVector);

% Calculate and display the mean without min and max values
result = problem_4_mean_clipped(randomVector);
disp(['Mean without Min and Max values: ', num2str(result)]);