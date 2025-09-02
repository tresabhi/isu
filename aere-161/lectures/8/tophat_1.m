%{
  Abhigyaan Deep, AER E 161, Lecture 7 Problem 1
  Purpose: Rewrite the following while loop into a for loop.
%}

clear, clc % clear screen and clear variables

for k = 1 : 3 : 10 % 1, 4, 7
  x = k ^ 2; % x = 1, 16, 49
  disp(x); % display x
end % end of for loop