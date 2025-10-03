function c = objFuncDeriv(x)
    c(1) = 2 * x(1) - 4 - 2 * x(2);
    c(2) = 4 * x(2) - 2 * x(1);
end
