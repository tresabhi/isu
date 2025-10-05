function [a, ecc, argp, raan, inc, theta] = cart_to_kepl(x, y, z, x_dot, y_dot, z_dot, mu)
    r = [x; y; z];
    v = [x_dot; y_dot; z_dot];

    r_norm = norm(r);
    v_norm = norm(v);

    h = cross(r, v);
    h_norm = norm(h);

    inc = acos(h(3) / h_norm);

    N = cross([0; 0; 1], h);
    N_norm = norm(N);

    e_vec = (1 / mu) * ((v_norm ^ 2 - mu / r_norm) * r - dot(r, v) * v);
    ecc = norm(e_vec);

    a = 1 / (2 / r_norm - v_norm ^ 2 / mu);

    if N_norm ~= 0
        raan = acos(N(1) / N_norm);

        if N(2) < 0
            raan = 2 * pi - raan;
        end

    else
        raan = 0;
    end

    if N_norm ~= 0
        argp = acos(dot(N, e_vec) / (N_norm * ecc));

        if e_vec(3) < 0
            argp = 2 * pi - argp;
        end

    else
        argp = 0;
    end

    theta = acos(dot(e_vec, r) / (ecc * r_norm));

    if dot(r, v) < 0
        theta = 2 * pi - theta;
    end

end
