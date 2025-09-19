clear, close

A = [6, 2, 1; 2, 5, 2; 1, 1, 5];
b = [1; 2; 1];

L = tril(A);
T = triu(A, 1);

x = [0; 0; 0];

for i = 1:10
    r = A * x - b;

    disp("i = " + num2str(i));
    disp(r);

    x = L \ (b - T * x);
end

disp(x);
