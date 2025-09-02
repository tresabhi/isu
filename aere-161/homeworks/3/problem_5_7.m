%{
  Abhigyaan Deep, AER E 161, Homewrork 3
  Purpose: Write a script that will:
    • generate a random integer in the inclusive range from 2 to 5
    • loop that many times to
      o prompt the user for a number
      o print the sum of the numbers entered so far with one decimal place.
%}

clear, clc % clear the workspace and the command window

n = randi([2, 5]); % generate a random integer in the inclusive range from 2 to 5
S = 0; % initialize the sum
for i = 1:n % loop that many times
  num = input('Enter a number: '); % prompt the user for a number
  S = S + num; % update the sum
end % end the for loop

fprintf('The sum of the numbers entered so far is %.1f\n', S) % print the sum with one decimal place