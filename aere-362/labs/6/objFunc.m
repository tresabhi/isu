function f = objFunc(x)
    global Mt;
    global Rt;
    global Dt;

    w = zeros(6);
    b = zeros(2);

    for i = 1:6
        w(i) = x(i);
    end

    b(1) = x(7);
    b(2) = x(8);

    r = 0;
    nSamples = 6;

    for i = 1:nSamples
        D = nnModel(Mt(i), Rt(i), w, b);
        r = r + (D - Dt(i)) ^ 2;
    end

    f = r;

end
