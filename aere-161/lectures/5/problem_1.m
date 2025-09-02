% Practicing matrix creation with colon notation and linspace function

clear, clc
format shortG

B1 = [
  1 : 3 : 19
  72 : -6 : 36
  0 : 0.125 : 0.75
  0.3 : 0.1 : 0.6, 1.2 : 0.2 : 1.6
  9 : -1 : 3
  ];

B2 = [
  linspace(1, 3, 7)
  linspace(72, 36, 7)
  linspace(0, 0.75, 7)
  linspace(0.3, 0.6, 4), linspace(1.2, 1.6, 3)
  linspace(9, 3, 7)
  ];

disp(B1)
disp(B2)