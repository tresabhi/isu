function f = objFunc(x)

    global Mt
    global Rt
    global Dt

    w = zeros(9);
    b = zeros(3);

    for i = 1:9
        w(i) = x(i);
    end

    b(1) = x(10);
    b(2) = x(11);
    b(3) = x(12);

    r = 0;

    for i = 1:6
        D = nnModel(Mt(i), Rt(i), w, b);
        r = r + (D - Dt(i)) ^ 2;
    end

    f = r;
end
