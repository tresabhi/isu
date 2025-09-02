%{
  Abhigyaan Deep, AER E 161, Lecture 4 Problem 3
  Purpose: answer the following question:

  The general equation for the distance that a free falling body has traveled
  (neglecting air friction) is D = 0.5gt2. Assume that g=9.8 m/s2. Write a
  script to generate a plot of time versus distance traveled, for the time
  from 0 to 100 sec. Include plot title and label your axes.
%}

clc, clear

gravity = 9.8; % declare gravity
time = 0 : 100; % declare time
distance = 0.5 * gravity .* time .^ 2; % calculate distances

plot(time, distance) % plot the time vs. distance
title('Time vs. Distance') % give it a title
xlabel('Time (sec)') % give it a human readable label
ylabel('Distance (m)') % give it a human readable label again