%{
  Abhigyaan Deep, AER E 161, Homework 2
  Purpose: A data file “parttolerance.dat” stores, on one line, a part number, and the
  minimum and maximum values for the valid range that the part could weigh. Write
  a script “parttol” that will read these values from the file, prompt the user for a
  weight, and print whether or not that weight is within range. Create a sample data
  file.
%}

% clear, clc % clear

data = load('problem_4_7.dat'); % load the data
partNumber = data(:, 1); % get the part number
min = data(:, 2); % get the minimum
max = data(:, 3); % get the maximum

weight = input('Enter the weight: '); % get the weight from the user

if weight >= min && weight <= max % check if the weight is within range
  fprintf('The weight is within range (%d - %d)\n', min, max) % print the result
else % if the weight is not within range
  fprintf('The weight is not within range (%d - %d)\n', min, max) % print the result
end % end if