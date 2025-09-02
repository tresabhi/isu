function [errorvec, mse] = problem_6_16_findmse(yobs, ypred) % declare a function with 2 outputs and 2 inputs
errorvec = yobs - ypred; % calculate the error
mse = mean(errorvec .^ 2); % calculate the mean squared error
end % end the function