function D = nnModel(M, R, w, b)
    z1 = M * w(1) + R * w(4) + b(1);
    z2 = M * w(2) + R * w(3) + b(2);
    D = w(5) / (1 + exp(-z1)) + w(6) / (1 + exp(-z2));
end
