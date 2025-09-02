%{
  Abhigyaan Deep, AER E 161, Homework 2
  Purpose: A part is being turned on a lathe. The diameter of the part is
  supposed to be 20,000 mm. The diameter is measured every 10 minutes and the
  results are stored in a file called partdiam.dat. Create a data file to
  simulate this. The file will store the time in minutes and the diameter at
  each time. Write a script to plot the data.
%}

clear, clc % clear

data = load('problem_3_20.dat'); % load the data
x = data(:, 1); % time
y = data(:, 2); % diameter

plot(x, y) % plot the data
title('Part Diameter') % title
xlabel('Time (minutes)') % x-axis label
ylabel('Diameter (mm)') % y-axis label