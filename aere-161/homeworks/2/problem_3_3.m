%{
  Abhigyaan Deep, AER E 161, Homework 2
  Purpose: Write a script that will prompt the user for a number and print it
  twice, once with three decimal places, and then with one decimal place.
%}

clear, clc % clear

number = input('Enter a number: '); % prompt user for number

fprintf('Number with three decimal places: %0.3f\n', number); % print number with three decimal places
fprintf('Number with one decimal place: %0.1f\n', number); % print number with one decimal place