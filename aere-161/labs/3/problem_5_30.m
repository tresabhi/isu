%{
  Abhigyaan Deep, AER E 161, Lab 3
  Purpose: Write a script that will prompt the user for a number in the
  inclusive range from 1 to 10 and error-check until the user enters a
  number in the correct range. Each time the user enters an invalid
  number, it prints whether it is too low or too high. It then prints
  out the valid number.
%}

clear, clc % clear everything

range = [1 10]; % set the range
value = -1; % set the initial value outside of the range

while value < range(1) || value > range(2) % check if value is outside the range
  value = input('Enter an integer between 1 and 10: '); % prompt user
  
  if value < range(1) % check if value is too low
    fprintf('Too low. Try again.\n') % print message
  elseif value > range(2) % check if value is too high
    fprintf('Too high. Try again.\n') % print message
  end % end the if statement
end % end the while loop

fprintf('You entered: %d\n', value) % print the value