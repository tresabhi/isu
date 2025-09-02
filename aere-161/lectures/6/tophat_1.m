%{
  Abhigyaan Deep, AER E 161, Lecture 6 Problem 2
  Purpose: rewrite given code with if statements
%}

clear,clc

grade = input('Enter the integer quiz grade 1-10  ');
fprintf('You have entered %d  ',grade)

if grade == 10
  disp(' grade is A+')
elseif grade == 9
  disp(' grade is A')
elseif grade == 6 || grade == 7 || grade == 8
  disp(' grade is B')
elseif grade == 4 || grade == 5
  disp(' grade is C')
elseif grade == 3
  disp(' grade is D')
elseif grade == 1 || grade == 2
  disp(' grade is F')
else
  disp(' wrong entry')
end