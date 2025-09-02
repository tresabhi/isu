%{
  Abhigyaan Deep, AER E 161, Lecture 4 Example 1
  Purpose: add geometric series for n terms (1 + 1/2 + 1/4 + 1/8 + ...)
%}

clc, clear % clear

n = 10; % number of terms
series = 0 : (n - 1); % array of terms
fractions = 2 .^ -series; % array of fractions with a negative exponent for reciprocal
answer = sum(fractions); % add them up

fprintf('Sum of geometric series till %d terms is %d\n', n, answer) % print