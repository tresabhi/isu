function theta = ecc_to_true(E, e)

    if e < 1
        theta = 2 * atan(sqrt((1 + e) / (1 - e)) * tan(E / 2));
    elseif e == 1
        theta = E;
    else
        theta = 2 * atan(sqrt((e + 1) / (e - 1)) * tanh(E / 2));
    end

end
