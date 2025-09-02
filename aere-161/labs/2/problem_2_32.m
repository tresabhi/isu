%{
  Abhigyaan Deep, AER E 161, Lab 2
  Purpose: Find max values from combinations of rows and columns
%}

clc, clear %2 clear

matrix = [
  3 7 1 2 0
  8 4 0 5 6
  0 2 7 8 6
  ]; % declare the matrix

maxColumn1 = max(matrix(:, 1)) % first column
maxColumn2 = max(matrix(:, 2)) % second column
maxColumn3 = max(matrix(:, 3)) % third column
maxColumn4 = max(matrix(:, 4)) % fourth column
maxColumn5 = max(matrix(:, 5)) % fifth column

maxRow1 = max(matrix(1, :)) % first row
maxRow2 = max(matrix(2, :)) % second row
maxRow3 = max(matrix(3, :)) % third row

maxMatrix = max(matrix(:)) % max value of the whole matrix