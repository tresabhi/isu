function T = thermoComp(theta, t, d, M)
    L = [
         1 / (t(1) + d(1) + theta(1)), 1;
         1, 1 / (t(2) + d(2) + theta(2))
         ];
    S = [M; M];
    T = L \ S;
end
