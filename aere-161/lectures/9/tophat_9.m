%{
  Abhigyaan Deep, AER E 161, Lecture 9 Tophat 9
  Purpose: Write a MATLAB function that will receive as an input argument a
  number of kilometers (K). The function will convert the kilometers to miles
  and to U.S. nautical miles, and return both results. The conversions are:
  1K = 0.621 miles and 1K = 0.54 US nautical miles.
%}

function [miles, nautical_miles] = tophat_9(km) % declare function
miles = km * 0.621; % convert km to miles
nautical_miles = km * 0.54; % convert km to nautical miles
end % end function