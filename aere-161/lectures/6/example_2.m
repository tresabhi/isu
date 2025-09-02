%{
  Abhigyaan Deep, AER E 161, Lecture 6 Problem 2
  Purpose: display corresponding days in month name with inputted month number
%}

clear, clc

number = input('Enter a number between 1 and 12: ');

switch number
  case {1, 3, 5, 7, 8, 10, 12}
    disp(31);
  case {4, 6, 9, 11}
    disp(30);
  case 2
    disp(28);
  otherwise
    disp('Invalid input');
end