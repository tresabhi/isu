%{
  Abhigyaan Deep, AER E 161, Lecture 7 Problem 1
  Purpose: find the max value from a list
%}

clear, clc

list = [1, 2, 7, 9, 0, -3, 11, 1];
max = -Inf;

for i = 1 : length(list)
  if list(i) > max
    max = list(i);
  end
end

disp(max)