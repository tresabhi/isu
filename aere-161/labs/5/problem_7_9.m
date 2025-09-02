function favoriteThing = problem_7_9(things) % declare a function iwth 1 input and 1 output

prompt = sprintf('What is your favorite %s: \n', things); % create a prompt
favoriteThing = input(prompt, 's'); % get input

while isempty(favoriteThing) % check if input is empty
  favoriteThing = input({'No, really... ', prompt}, 's'); % ask again
end % end while

end % end function