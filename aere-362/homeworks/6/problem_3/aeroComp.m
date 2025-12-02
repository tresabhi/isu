function gamma = aeroComp(theta, d)
    A = [
         (theta(1) + d(1)) ^ 2 + 2, 1;
         1, (theta(2) + d(2)) ^ 2 + 1
         ];
    b = [
         theta(1) + d(1);
         theta(2) + 2 * d(2)
         ];
    gamma = A \ b;
end
