%{
  Abhigyaan Deep, AER E 161, Homework 2
  Purpose: Write a script that would create a 5x5 matrix of random integers.
  From this, create another matrix variable which is the “middle” 3x3 part of
  the original matrix. Write this new matrix to a file.
%}

clear, clc % clear

matrix = randi([0, 255], 5, 5); % create a 5x5 matrix of random integers
middle = matrix(2 : 4, 2 : 4); % extract the middle 3x3 part

disp(matrix) % display the matrix
disp(middle) % display the middle 3x3 part

save problem_3_19.dat middle % save the middle 3x3 part