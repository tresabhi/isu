%{
  Abhigyaan Deep, AER E 161, Lab 2
  Purpose: Load data file and plot altitudes vs temperatures
%}

clc, clear % clear

data = load('problem_3_17_alttemps.dat'); % load the data
x = data(:, 1); % altitudes from the first column
y = data(:, 2); % temperatures from the second column

plot(x, y, 'o-'); % plot orange line
title('Altitude vs Temperature'); % title
xlabel('Altitude (km)'); % x axis label
ylabel('Temperature (K)'); % y axis label