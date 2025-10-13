function M = ecc_to_mean(e, E)
    M = E - e * sin(E);
end
