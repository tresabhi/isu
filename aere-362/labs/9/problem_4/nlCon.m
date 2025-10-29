function [c, ceq] = nlCon(x)
    c(1) = -x(1) ^ 2 - x(2) ^ 2 + 8;
    ceq = [];
end
