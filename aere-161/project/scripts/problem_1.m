%{
  Abhigyaan Deep, AER E 161, Project 1 Problem 1
  Purpose: calculate the new center of gravity of an aircraft
%}

% clear the workspace and the command window
clear, clc

% imperial units: lbs, in, gallons
EMPTY_WEIGHT = 1471; % lbs
CENTER_OF_GRAVITY = 85.9; % inches
FRONT_SEATS_MOMENT_ARM = 85.5; % inches
FUEL_TANKS_MOMENT_ARM = 95; % inches
REAR_SEATS_MOMENT_ARM = 118.1; % inches
MAXIMUM_RAMP_WEIGHT = 2400; % lbs
MAXIMUM_FUEL = 50; % gallon

% welcome the user
disp('Welcome to the Center of Gravity Calculator.')

% declare a non-1 value for the program status
programStatus = 0;
% run till the user wants to exit
while programStatus ~= 1
  % get the user inputs
  [fuelWeight, passengerWeights] = problem_1_prompt();
  
  % sum up the all the weights to get the total
  rampWeight = EMPTY_WEIGHT + sum(passengerWeights) + fuelWeight;
  % display the results
  disp(['The ramp weight is ' num2str(rampWeight) ' lbs.'])
  
  % check if the ramp is too heavy
  if rampWeight >= MAXIMUM_RAMP_WEIGHT
    % let's hope the landing gears are not destroyed haha!
    disp('Ramp weight is above maximum. Please reduce weights.')
    % terminate this iteration and continue with the next one
    continue
  end
  
  % okay, the ramp's light enought, let's get all the moments
  emptyMoment = EMPTY_WEIGHT * CENTER_OF_GRAVITY;
  % remember the front row is the 1st and 2nd crew members
  frontSeatMoment = (passengerWeights(1) + passengerWeights(2)) * FRONT_SEATS_MOMENT_ARM;
  % same idea with the rear
  rearSeatMoment = (passengerWeights(3) + passengerWeights(4)) * REAR_SEATS_MOMENT_ARM;
  % and the fuel
  fuelMoment = fuelWeight * FUEL_TANKS_MOMENT_ARM;
  % and we just add them up
  totalMoment = emptyMoment + frontSeatMoment + rearSeatMoment + fuelMoment;
  
  % calculate the new center of gravity
  newCenterOfGravity = totalMoment / rampWeight;
  % display the results
  disp(['The new center of gravity is ' num2str(newCenterOfGravity) ' inches.'])
  % check if the new center of gravity is within acceptable range
  if newCenterOfGravity >= 86.8 && newCenterOfGravity <= 95.8
    % great!
    disp('Center of gravity is within acceptable range.')
  else
    % oh no!
    disp('Center of gravity is outside acceptable range.')
  end
  
  % check if the user wants to continue
  programStatus = input('Would you like to continue? Enter 1 to exit: ');
end

% goodbye world
disp('Thanks for using the Center of Gravity Calculator.')