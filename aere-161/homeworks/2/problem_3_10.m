%{
  Abhigyaan Deep, AER E 161, Homework 2
  Purpose: A power company charges 6.6 cents per kilowatt hour (KWH) for
  providing electricity. Write a script “power_charge” that will prompt the
  user for the number of KWH used in a given month, and will print the charge
  for the month in dollars, in the following format. (The conversion is 100
  cents in one dollar.)
%}

clear, clc % clear

kwh = input('How many KWH this month: '); % prompt user for number of KWH used
charge = kwh * 0.066; % calculate charge

fprintf('Your charge for %0.0f KWH will be $%0.2f\n', kwh, charge); % print charge