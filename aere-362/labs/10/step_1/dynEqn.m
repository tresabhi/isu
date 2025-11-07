function dStateT = dynEqn(t, state)
    theta = state(1);
    r = state(2);
    vTheta = state(3);
    vr = state(4);

    dStateT = zeros(4, 1);
    dStateT(1) = vTheta / r;
    dStateT(2) = vr;
    dStateT(3) = -vr * vTheta / r;
    dStateT(4) = vTheta ^ 2 / r - 1 / r / r;
end
