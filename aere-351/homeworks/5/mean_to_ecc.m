function E = mean_to_ecc(e, M)
    E = M;

    for i = 1:50
        E_next = E - ((E - e .* sin(E) - M) ./ (1 - e .* cos(E)));
        E = E_next;
    end

end
