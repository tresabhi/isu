A = [
     -4, -2, 1;
     -2, -6, 0;
     1, 0, -2;
     ];
b = [5; 0; 0];
x = [1; 1; 1];

L = tril(A);
T = triu(A, 1);

for i = 1:50
    r = norm(A * x - b);

    disp("i = " + num2str(i));
    disp(r);

    x = L \ (b - T * x);
end

true_x = A \ b;

disp("Ground truth (inverse):")
disp(true_x)

disp("Gauss-Seidel:");
disp(x);
