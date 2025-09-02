%{
  Abhigyaan Deep, AER E 161, Project 1 Problem 1
  Purpose: calculate the density altitude of the Ames Airport
%}

% clear the workspace and the command window
% clear, clc

FIELD_ELEVATION = 955.6; % from the Ames Airport
OPEN_WEATHER_API_KEY = '7cab1fcaf444883263bc48dd983e6018';

% generate the request body
options = weboptions('ContentType', 'json');
% concatenate the url
url = ['https://api.openweathermap.org/data/2.5/weather?q=', 'Ames', '&APPID=', OPEN_WEATHER_API_KEY];
% fetch the data
weather = webread(url, options).main;

% display the data for debugging purposes
disp('Raw weather data: ')
disp(weather)

% convert to celsius
temperatureCelsius = problem_2_kelvin_to_celsius(weather.temp);
% calculate the dew point in celsius
dewPoint = temperatureCelsius - ((100 - weather.humidity) / 5);
fprintf('Dew Point (celsius): %f\n', dewPoint)
% calculate the vapor pressure
vaporPressure = 6.11 * 10 ^ ((7.5 * dewPoint) / (237.7 + dewPoint));

% calculate the virtual temperature in kelvin
virtualTemperature = weather.temp / (1 - (vaporPressure / weather.pressure) * (1 - 0.622));
% convert it to rankine
virtualTemperatureRankine = ((9 / 5) * (virtualTemperature - 273.15) + 32) + 459.69;

% convert the pressure to inches of mercury
pressureInchesHG = weather.pressure * 0.02953;
fprintf('Pressure (inches of mercury): %f\n', pressureInchesHG)
% calculate the density altitude
densityAltitude = FIELD_ELEVATION + (145366 * (1 - ((17.326 * pressureInchesHG) / virtualTemperatureRankine) ^ 0.235));

% display the results
disp(['The density altitude of the Ames Airport is ', num2str(densityAltitude), ' ft.'])