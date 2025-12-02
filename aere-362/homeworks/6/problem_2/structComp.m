function d = structComp(theta, t, gamma)
    K = [
         5 * t(1) - theta(1), 2;
         2, 4 * t(2) - theta(2)
         ];
    f = [
         2 * gamma(1) ^ 2;
         gamma(2) ^ 2
         ];
    d = K \ f;
end
