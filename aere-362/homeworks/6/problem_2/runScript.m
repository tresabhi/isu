theta = [1; 1];
t = [1; 1];
gamma = [1; 1];
d = [1; 1];

for i = 1:2
    gamma = aeroComp(theta, d);
    d = structComp(theta, t, gamma);

    disp('i =')
    disp(i)

    disp('gamma =')
    disp(gamma)

    disp('d =')
    disp(d)

    A_aero = [
              (theta(1) + d(1)) ^ 2 + 2, 1;
              1, (theta(2) + d(2)) ^ 2 + 1
              ];
    b_aero = [
              theta(1) + d(1);
              theta(2) + 2 * d(2)
              ];
    K_struct = [
                5 * t(1) - theta(1), 2;
                2, 4 * t(2) - theta(2)
                ];
    f_struct = [
                2 * gamma(1) ^ 2;
                gamma(2) ^ 2
                ];

    residual_aero = b_aero - A_aero * gamma;
    residual_struct = f_struct - K_struct * d;

    disp('residual_aero =')
    disp(residual_aero)

    disp('residual_struct =')
    disp(residual_struct)
end
