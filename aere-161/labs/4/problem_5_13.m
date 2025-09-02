%{
  Abhigyaan Deep, AER E 161, Lab 4
  Purpose: Write a function that will receive a matrix as an input argument, and will calculate and
  return the overall average of all numbers in the matrix. Use loops, not built-in functions, to
  calculate the average.
%}

function [average] = problem_5_13(matrix) % declare a function with input matrix
sum = 0; % initialize sum

for i = 1:length(matrix) % loop through rows
  for j = 1:length(matrix) % loop through columns
    sum = sum + matrix(i, j); % add to sum
  end % end loop
end % end loop

average = sum / (length(matrix) * length(matrix)); % calculate average
end % end function