%{
  Abhigyaan Deep, AER E 161, Homework 5
  Purpose: read and plot data safely
%}

clear, clc

% Read data from the file
data = dlmread('problem_2.dat'); % read data from the file

% Extract individual columns
blade_diameter = data(:, 1); % blade diameter in feet
wind_velocity = data(:, 2); % wind velocity in mph
electricity_generated = data(:, 3); % electricity generated in kWh/year

% Create a 3D scatter plot
figure;
scatter3(blade_diameter, wind_velocity, electricity_generated, 'filled'); % plot the data
xlabel('Blade Diameter (feet)'); % label the x and y axes
ylabel('Wind Velocity (mph)'); % label the x and y axes
zlabel('Electricity Generated (kWh/year)'); % label the x and y axes
title('Wind Turbine Electricity Generation'); % title the plot

% Add grid and customize plot if needed
grid on; % add grid
