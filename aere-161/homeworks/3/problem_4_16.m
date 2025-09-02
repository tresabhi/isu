%{
  Abhigyaan Deep, AER E 161, Homewrork 3
  Purpose: In chemistry, the pH of an aqueous solution is a measure of its acidity. The
  pH scale ranges from 0 to 14, inclusive. A solution with a pH of 7 is said to be
  neutral, a solution with a pH greater than 7 is basic, and a solution with a pH less
  than 7 is acidic. Write a script that will prompt the user for the pH of a solution, and
  will print whether it is neutral, basic, or acidic. If the user enters an invalid pH, an
  error message will be printed.
%}

clear, clc % clear the workspace and the command window

pH = input('Enter the pH of a solution: '); % prompt the user for the pH of a solution

if pH < 0 || pH > 14
  disp('Error: pH must be greater than or equal to 0')
else
  if pH < 7
    disp('The solution is acidic')
  elseif pH > 7
    disp('The solution is basic')
  else
    disp('The solution is neutral')
  end
end