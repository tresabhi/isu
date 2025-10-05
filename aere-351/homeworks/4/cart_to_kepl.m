function [a, ecc, argp, raan, inc, theta] = cart_to_kepl(x, y, z, x_dot, y_dot, z_dot, mu)
    r = [x; y; z];
    v = [x_dot; y_dot; z_dot];

    h = cross(r, v);
    inc = acos(h / norm(h));

    e = cross(v, h) / mu - r / norm(r);
    ecc = norm(e);

    a = 1 / (2 / norm(r) - (norm(v) ^ 2) / mu);

    if v_dot > 0
        theta = acos(dot(e, r) / (norm(e) * norm(r)));
    else
        theta = 2 * pi - acos(dot(e, r) / (norm(e) * norm(r)));
    end

    if N_j > 0
        raan = acos(N_I / norm(N_I));
    else
        raan = 2 * pi - acos(N_I / norm(N_I));
    end

    if e_k > 0
        argp = acos(dot(N, e) / (norm(N) * norm(e)));
    else
        argp = 2 * pi - acos(dot(N, e) / (norm(N) * norm(e)));
    end

end
