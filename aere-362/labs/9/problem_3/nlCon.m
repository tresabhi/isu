function [c, ceq] = nlCon(x)
    c(1) = -x(1) ^ 2 - x(2) ^ 2 + 4;
    ceq = [];
end
