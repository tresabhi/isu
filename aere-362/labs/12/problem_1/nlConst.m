function [c, ceq] = nlConst(x)
    theta(1) = x(1);
    theta(2) = x(2);
    t(1) = x(3);
    t(2) = x(4);

    [gamma, d] = run_script_mda(theta, t);
    [~, L] = force(theta, gamma);

    ceq(1) = L - 1;

    sigma = stress(d);

    c(1) = sigma - 1;
end
