%{
  Abhigyaan Deep, AER E 161, Lecture 4 Tophat 3
  Purpose: add geometric series for n terms (1 + 1/2 + 1/3 + 1/4 + ...)
%}

clc, clear % clear

n = 10; % number of terms
series = 1 : n; % array of terms
fractions = series .^ -1; % array of fractions with a negative exponent for reciprocal
answer = sum(fractions); % add them up

fprintf('Sum of geometric series till %d terms is %d\n', n, answer) % print