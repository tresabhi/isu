clear, clc % clear pretty much everything

load houseaffoard.dat % load data

h = barh(houseaffoard(2:3,:)', 'stacked'); % plot the data
h(1).XData = houseaffoard(1,:); % set the x data for the first bar
h(2).XData = houseaffoard(1,:); % set the x data for the second bar

xlabel('$ in thousands') % set the x label
ylabel('Year') % set the y label
title('Median income and home prices') % set the title