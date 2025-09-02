%{
  Abhigyaan Deep, AER E 161, Homework 4
  Purpose: Some Machine Learning algorithms are trained on data sets that have known
  outcomes.
%}

clear, clc % clear the workspace

x1 = input('Enter x1: '); % ask for x coordinate of point 1
y1 = input('Enter y1: '); % ask for y coordinate of point 1
x2 = input('Enter x2: '); % ask for x coordinate of point 2
y2 = input('Enter y2: '); % ask for y coordinate of point 2
x3 = input('Enter x3: '); % ask for x coordinate of point 3
y3 = input('Enter y3: '); % ask for y coordinate of point 3

area = problem_6_18_area(x1, y1, x2, y2, x3, y3); % calculate area
disp(area) % display area
