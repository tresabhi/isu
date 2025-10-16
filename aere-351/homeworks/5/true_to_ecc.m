function E = true_to_ecc(e, theta)

    if e < 1
        E = 2 * atan(sqrt((1 - e) / (1 + e)) * tan(theta / 2));
    elseif e == 1
        E = theta;
    else
        E = 2 * atanh(sqrt((e - 1) / (e + 1)) * tan(theta / 2));
    end

end
