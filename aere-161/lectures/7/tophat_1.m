%{
  Abhigyaan Deep, AER E 161, Lecture 7 Problem 1
  Purpose: Write a MATLAB script where you will prompt the user for an integer n and print "I love MATLAB!" n times. Omit the user input error checking.
%}

clear, clc % clear

n = input('Enter an integer: '); % prompt

for i = 1 : n % loop
  disp('I love MATLAB!') % print
end % end loop