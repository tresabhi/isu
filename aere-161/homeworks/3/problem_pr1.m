%{
  Abhigyaan Deep, AER E 161, Homewrork 3
  Purpose: Rewrite a for loop into a while loop.
%}

clear, clc % clear the workspace and the command window

S = 0; % initialize the sum
i = 1; % initialize the counter
while i <= 10 % while the counter is less than 10
  S = S + i; % update the sum
  i = i + 1; % update the counter
end % end the while loop

disp(S)