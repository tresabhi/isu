function D = nnModel(M, R, w, b)
    z1 = w(1) * M + w(4) * R + b(1);
    z2 = w(2) * M + w(5) * R + b(2);
    z3 = w(3) * M + w(6) * R + b(3);
    D = w(7) / (1 + exp(-z1)) + w(8) / (1 + exp(-z2)) + w(9) / (1 + exp(-z3));
end
