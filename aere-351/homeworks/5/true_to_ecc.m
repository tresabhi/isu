function E = true_to_ecc(e, theta)
    E = 2 * atan(sqrt((1 - e) / (1 + e)) * tan(theta / 2));
end
