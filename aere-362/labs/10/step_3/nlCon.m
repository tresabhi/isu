function [c, ceq] = nlCon(x)
    [theta, r] = propagator(x, 0);

    ceq(1) = r(end) - 2;
    c = [];
end
