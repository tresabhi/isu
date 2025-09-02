%{
  Abhigyaan Deep, AER E 161, Homework 5
  Purpose: read and plot data safely
%}

clear, clc

% Script to read and plot data
fileID = fopen('problem_1.dat', 'r');

if fileID == -1 % check if the file was opened successfully
  error('Error opening the file.'); % error message if the file was not opened successfully
end

% Initialize variables
x = [];
y = [];

try % try to read and plot the data
  for i = 1:5 % read the first 5 lines
    line = fgetl(fileID); % read a line
    if ischar(line) % check if the line is not empty
      % Extract x and y values from the line
      data = sscanf(line, '%*d (x,y) %f %f'); % extract x and y values
      x = [x, data(1)]; % append x and y values
      y = [y, data(2)]; % append x and y values
    end
  end
  
  % Plot the data points
  scatter(x, y); % plot the data points
  xlabel('X'); % label the x and y axes
  ylabel('Y'); % label the x and y axes
  title('Scatter Plot of Data Points'); % title the plot
  
  % Close the file
  fclose(fileID); % close the file
  disp('File successfully closed.'); % display a message indicating that the file was closed successfully
catch
  % Close the file in case of an error
  fclose(fileID); % close the file
  error('An error occurred while processing the file.'); % error message if an error occurred while processing the file
end