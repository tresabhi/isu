x = [1; 1];
b = [1; 2];

for i = 1:10
    r = norm(A(x) * x - b);

    disp("i = " + num2str(i));
    disp(r);

    x = A(x) \ b;
end

disp("Final:");
disp(x);

function A = A(x)
    A = [6 * x(1), 5; 5, 4];
end
