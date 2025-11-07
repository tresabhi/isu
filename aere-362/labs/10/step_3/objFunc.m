function f = objFunc(x)
    deltaV = sqrt(x(1) ^ 2 + x(2) ^ 2);
    tof = x(3);

    f = 0.99 * deltaV + 0.01 * tof;
end
