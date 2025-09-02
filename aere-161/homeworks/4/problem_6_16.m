%{
  Abhigyaan Deep, AER E 161, Homework 4
  Purpose: Some Machine Learning algorithms are trained on data sets that have known
  outcomes.
%}

clear, clc % clear the workspace

[yobs, ypred] = problem_6_16_getvecs(); % get the vectors
[errorvec, mse] = problem_6_16_findmse(yobs, ypred); % find the mse and error
problem_6_16_printmse(mse) % print the mse