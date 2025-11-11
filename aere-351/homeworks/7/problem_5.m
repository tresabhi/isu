mu = 3.98600e5;

r_1 = [5887; -3520; -1204];
r_2 = [5572; -3457; -2376];
r_3 = [5088; -3289; -3480];

disp("v_2 =")
disp(gibbs(r_1, r_2, r_3, mu))

disp("|v_2| =")
disp(norm(gibbs(r_1, r_2, r_3, mu)))

function v_2 = gibbs(r_1, r_2, r_3, mu)
    C_12 = cross(r_1, r_2);
    C_23 = cross(r_2, r_3);
    C_31 = cross(r_3, r_1);

    % I'd say 1 * 10^-5 is close enough to zero
    if dot(r_1, C_23) < 1e-5
        error("Vectors are coplanar");
    end

    N_1 = norm(r_1) * C_23;
    N_2 = norm(r_2) * C_31;
    N_3 = norm(r_3) * C_12;

    S_1 = r_1 * (norm(r_2) - norm(r_3));
    S_2 = r_2 * (norm(r_3) - norm(r_1));
    S_3 = r_3 * (norm(r_1) - norm(r_2));

    N = N_1 + N_2 + N_3;
    D = C_12 + C_23 + C_31;
    S = S_1 + S_2 + S_3;

    disp(N)
    disp(D)
    disp(S)

    v_2 = sqrt(mu / (norm(N) * norm(D))) * (cross(D, r_2) / norm(r_2) + S);
end
