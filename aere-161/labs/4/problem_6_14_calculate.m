%{
  Abhigyaan Deep, AER E 161, Lab 4
  Purpose: Write a script that will:
  • Call a function to prompt the user for an angle in degrees
  • Call a function to calculate and return the angle in radians. (Note: p radians = 180°)
  • Call a function to print the result
  Write all of the functions, also. Put the script and all functions in separate code files.
%}

function [angleInRadians] = problem_6_14_calculate(angleInDegrees) % declare a function
angleInRadians = angleInDegrees * pi / 180; % convert to radians
end % end function