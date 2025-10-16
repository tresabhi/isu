function E = mean_to_ecc(e, M)
    E = M;

    if e == 1
        return
    end

    for i = 1:50

        if e < 1
            E = E - ((E - e .* sin(E) - M) ./ (1 - e .* cos(E)));
        else
            E = E - ((e .* sinh(E) - E - M) ./ (e .* cosh(E) - 1));
        end

    end

end
