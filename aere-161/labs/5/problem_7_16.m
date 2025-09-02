%{
  AER E 161, Lab 5
  Purpose: Write a function that will prompt the user separately for a filename and extension and will
  create and return a string with the form ‘filename.ext’.
%}

function problem_7_16() % declare a function
name = input("What is your file's name? ", 's'); % get input
extention = input("What is your file's extention? ", 's'); % get input

fprintf("%s.%s\n", name, extention); % print
end % end function

