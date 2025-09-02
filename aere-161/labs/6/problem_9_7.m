baseFilename = 'exfile'; % Specify the base filename
totalLines = 0; % Initialize the line count
fileNumber = 1; % Loop to find and count lines in each file
while true
  currentFilename = [baseFilename, num2str(fileNumber), '.dat']; % Construct the current filename
  
  % Try to open the file
  fileID = fopen(currentFilename, 'r');
  
  % Check if the file exists
  if fileID == -1
    % If the file does not exist, break out of the loop
    break;
  end
  
  % Count lines in the current file
  while ~feof(fileID)
    % Read a line from the file
    line = fgetl(fileID);
    
    % Check if the line is not empty
    if ischar(line)
      % Increment the line count
      totalLines = totalLines + 1;
    end
  end
  
  % Close the current file
  fclose(fileID);
  
  % Move on to the next file
  fileNumber = fileNumber + 1;
end

% Display the total number of lines
disp(['Total number of lines across all files: ', num2str(totalLines)]);