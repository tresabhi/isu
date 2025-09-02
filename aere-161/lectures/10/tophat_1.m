%{
  Abhigyaan Deep, AER E 161, Lecture 10 Tophat 1
  Purpose: Write a MATLAB function that will receive as an input arguments x
  and y coordinates of a point.  The function will create a plot of just
  this one point as a red star.
%}

function tophat_1(x, y) % function definition
title('Red Star at (x, y)'); % give it a title
plot(x, y, 'r*'); % plot the point
end % end the function
