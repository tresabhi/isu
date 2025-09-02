function result = problem_4_mean_clipped(vector)
if length(vector) < 3 % At least 3 elements are required
  error('Vector should have at least three elements.');
end

minVal = min(vector); % Find min and max values
maxVal = max(vector); % Find min and max values

% Exclude min and max values from the vector
vectorWithoutMinMax = vector(vector ~= minVal & vector ~= maxVal);

% Calculate the mean of the remaining values
result = mean(vectorWithoutMinMax);
end