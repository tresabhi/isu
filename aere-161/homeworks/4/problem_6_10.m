%{
  Abhigyaan Deep, AER E 161, Homework 4
  Purpose: Write a function that receives a matrix as an input argument, and prints a
  random column from the matrix.
%}

function problem_6_10(A) % declare a function with one input
column = A(:, randi(size(A, 2))); % select a random column
disp(column); % print the column
end % end the function