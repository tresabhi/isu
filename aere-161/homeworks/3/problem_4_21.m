%{
  Abhigyaan Deep, AER E 161, Homewrork 3
  Purpose: The Beaufort Wind Scale is used to characterize the strength of winds. The
  scale uses integer values and goes from a force of 0, which is no wind, up to 12,
  which is a hurricane. The following script first generates a random force value.
  Then, it prints a message regarding what type of wind that force represents, using a
  switch statement. You are to re-write this switch statement as one nested if-else
  statement that accomplishes exactly the same thing. You may use else and/or elseif
  clauses.
%}

% clear, clc % clear the workspace and the command window

% Beaufort Wind Scale
ranforce = randi([0, 12]); % generate a random force value
if ranforce == 0 % if the force is 0
  disp('There is no wind') % print the message
elseif ranforce == 1 || ranforce == 2 || ranforce == 3 || ranforce == 4 || ranforce == 5 || ranforce == 6 % if the force is between 1 and 6
  disp('There is a breeze') % print the message
elseif ranforce == 7 || ranforce == 8 || ranforce == 9 % if the force is between 7 and 9
  disp('This is a gale') % print the message
elseif ranforce == 10 || ranforce == 11 % if the force is between 10 and 11
  disp('It is a storm') % print the message
elseif ranforce == 12 % if the force is 12
  disp('Hello, Hurricane!') % print the message
end % end the if-else statement