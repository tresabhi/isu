function [x, y, z, x_dot, y_dot, z_dot] = kepl_to_cart(a, ecc, argp, raan, inc, theta, mu)
    e = ecc;

    p = a * (1 - e ^ 2);
    r_abs = p / (1 + e * cos(theta));

    r_e = r_abs * cos(theta);
    r_p = r_abs * sin(theta);
    r_k = 0;

    v_e = -sqrt(mu / p) * sin(theta);
    v_p = sqrt(mu / p) * (e + cos(theta));
    v_k = 0;

    R = rot_313(raan, inc, argp);
    r = R * [r_e; r_p; r_k];
    v = R * [v_e; v_p; v_k];

    x = r(1);
    y = r(2);
    z = r(3);
    x_dot = v(1);
    y_dot = v(2);
    z_dot = v(3);
end
