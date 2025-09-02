function [x_1, x_2, x_3] = problem_5_cramer(A, b)
% clone A for each variable
A_x = A;
A_y = A;
A_z = A;

% replace corresponding columns
A_x(:, 1) = b;
A_y(:, 2) = b;
A_z(:, 3) = b;

% get the determinants
D = det(A);
D_x = det(A_x);
D_y = det(A_y);
D_z = det(A_z);

% apply the formula
x_1 = D_x / D;
x_2 = D_y / D;
x_3 = D_z / D;

if D == 0
  disp('The system has no solution');
end
end
