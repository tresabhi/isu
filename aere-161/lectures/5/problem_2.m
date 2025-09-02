%{
  Abhigyaan Deep, AER E 161, Lecture 5 Problem 2
  Purpose:
  - Read data file
  - Graph Californian and Floridian daily temperatures since Jan 1, 2010
  - Data only available for 12 days
  - 1st row Temp (F) in Cape Canaveral Air Force Station in Florida
  - 2nd row Temp (F) Edwards Air Force Base in California
%}

clc, clear

data = load("lec5\problem_2.dat"); % load the data
florida = data(1, :); % first row which is Florida
california = data(2, :); % second row which is California
days = 1 : length(florida); % dinamically infer the days

plot(days, florida, 'b', days, california, 'r')
title('Average daily temperatures (F) since Jan 1, 2010')
legen('Florida - Cape Canaveral', 'California - Edwards')
xlabel('Days since Jan 1, 2010')
ylabel('Temperature (F)')