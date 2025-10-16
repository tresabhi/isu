function theta = ecc_to_true(E, e)
    theta = 2 * atan(sqrt((1 + e) / (1 - e)) * tan(E / 2));
end
