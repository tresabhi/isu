%{
  Abhigyaan Deep, AER E 161, Homework 5
  Purpose: read and plot data safely
%}

% Data sets
prodLineA = [15.94 15.98 15.94 16.16 15.86 15.86 15.90 15.88]; % production line A
prodLineB = [15.96 15.94 16.02 16.10 15.92 16.00 15.96 16.02]; % production line B

clear, clc

% Calculate mean, median, mode, and standard deviation
meanA = mean(prodLineA); % calculate mean
medianA = median(prodLineA); % calculate median
modeA = mode(prodLineA); % calculate mode
stdDevA = std(prodLineA); % calculate standard deviation

meanB = mean(prodLineB); % calculate mean
medianB = median(prodLineB); % calculate median
modeB = mode(prodLineB); % calculate mode
stdDevB = std(prodLineB); % calculate standard deviation

% Display results
disp('Production Line A:'); % display results
disp(['Mean: ' num2str(meanA)]); % display results
disp(['Median: ' num2str(medianA)]); % display results
disp(['Mode: ' num2str(modeA)]); % display results
disp(['Standard Deviation: ' num2str(stdDevA)]); % display results
disp(' '); % display results

disp('Production Line B:'); % display results
disp(['Mean: ' num2str(meanB)]); % display results
disp(['Median: ' num2str(medianB)]); % display results
disp(['Mode: ' num2str(modeB)]); % display results
disp(['Standard Deviation: ' num2str(stdDevB)]); % display results
disp(' '); % display results

% Check which production line is better in terms of meeting the specification
targetDiameter = 16; % target diameter in feet

if abs(meanA - targetDiameter) < abs(meanB - targetDiameter) % compare mean
  disp('Production Line A is better in terms of meeting the specification.'); % display results
else
  disp('Production Line B is better in terms of meeting the specification.'); % display results
end
