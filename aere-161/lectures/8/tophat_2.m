%{
  Abhigyaan Deep, AER E 161, Lecture 7 Problem 1
  Purpose: Write a MATLAB script where you will prompt the user for 5 numbers,
  and store them in a vector V. Make sure that you preallocate the vector.
%}

clear, clc % clear screen and clear variables

numbers = zeros(1, 5); % preallocate vector

for i = 1 : length(numbers) % iterate through vector
  numbers(i) = input('Enter a number: '); % prompt user for input
end % end of for loop

disp(numbers);