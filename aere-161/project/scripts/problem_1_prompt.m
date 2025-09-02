%{
  Abhigyaan Deep, AER E 161, Project 1 Problem 1
  Purpose: get the relevant inputs from the user
%}

function [fuelWeight, passengerWeights] = problem_1_prompt()
% set fuel to infinity to always guarantee a failing case
fuel = inf;
% check for valid fuel
while fuel > MAXIMUM_FUEL || fuel < 0
  % if it's infinity, it's the first iteration
  if fuel == inf
    % ask them the initial question
    fuel = input('How much fuel is on board (in US Gallons)? ');
    % if it's less than 0, the user needs to get it together and try again
  elseif fuel < 0
    % ask them to try again but with a different question and indentation
    fuel = input('  Value cannot be less than 0. Try again: ');
    % user still made an oopsies, make 'em go at it again
  elseif fuel > MAXIMUM_FUEL
    % once again, a different question with indentation
    fuel = input('  Value cannot be greater than 50. Try again: ');
  end
end
% convert to lbs
fuelWeight = fuel * 6;

% let's start on the weights; allocating 2 to the front and 2 to the rear
passengerWeights = zeros(1, 4);
% keep track of the index
passengerIndex = 1;
% go through all 4 seats
while passengerIndex <= length(passengerWeights)
  % default name of the passenger is the pilot
  passengerName = 'the pilot';
  % switch to assign the correct name
  if passengerIndex == 2
    passengerName = 'the co-pilot';
  elseif passengerIndex ~= 1
    passengerName = sprintf('passenger %d', passengerIndex - 2);
  end
  
  % intentional initial failing case
  passengerWeight = inf;
  % check for valid weight
  while passengerWeight == inf || passengerWeight < 0
    % if it's infinity, it's the first iteration
    if passengerWeight == inf
      % ask them the initial question
      passengerWeight = input(sprintf('What is the weight of %s (in lbs)? ', passengerName));
    elseif passengerWeight < 0
      % user entered a negative value? goodness me they need help
      passengerWeight = input('  Value cannot be less than 0. Try again: ');
    end
  end
  
  % assign the weight to the correct seat
  passengerWeights(passengerIndex) = passengerWeight;
  % onto the next person
  passengerIndex = passengerIndex + 1;
end
end