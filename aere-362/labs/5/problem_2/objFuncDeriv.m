function c = objFuncDeriv(x)
    c(1) = 2 * x(1) - 4 - 2 * x(2);
    c(2) = 4 * x(2) - 2 * x(1);
    c(3) = 8 * x(3);
end
