clear, close

b = [1; 2; 1];
x = [0; 0; 0];

for i = 1:10
    A = [6, 2 * x(1), x(1); 2 * x(1), 5, 2; 1, x(2), 5];
    r = A * x - b;

    disp("i = " + num2str(i));
    disp(r);

    x = A \ b;
end

disp(x);
