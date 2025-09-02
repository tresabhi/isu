%{
  Abhigyaan Deep, AER E 161, Homework 5
  Purpose: use Cramer's rule to check against manual solution
%}

% clear, clc

% problem 1
[p1_x1, p1_x2, p1_x3] = problem_5_cramer([3, 2, -1; 2, -3, 2; 5, 1, 7], [5,-4,8]);
fprintf('problem 1: x1 = %f, x2 = %f, x3 = %f\n', p1_x1, p1_x2, p1_x3);

% problem 2
[p2_x1, p2_x2, p2_x3] = problem_5_cramer([2, 1, -1; 1, 4, -8; -1, -0.5, 0.5], [-4, 12, 2]);
fprintf('problem 2: x1 = %f, x2 = %f, x3 = %f\n', p2_x1, p2_x2, p2_x3)