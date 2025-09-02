%{
  Abhigyaan Deep, AER E 161, Lab 3
  Purpose: Write a script that will generate random integers in the range from
  0 to 50, and print them, until one is finally generated that is greater than
  25. The script should print how many attempts it took.
%}

clear, clc % clear everything

attempt = 0; % initialize attempt index
value = -1; % initialize value index intentionally outside of domain

while value <= 25 % while value is less than or equal to 25
  attempt = attempt + 1; % increment attempt
  value = randi(50); % generate random integer
  fprintf('Attempt %d: %d\n', attempt, value); % print value
end

fprintf('Attempts required: %d\n', attempt); % print attempt