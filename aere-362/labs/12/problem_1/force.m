function [D, L] = force(theta, gamma)
    L = 10 * (gamma(1) + gamma(2));
    D = gamma(1) * sin(theta(1)) + gamma(2) * sin(theta(2));
end
