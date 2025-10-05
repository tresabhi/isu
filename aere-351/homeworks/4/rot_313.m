function R = rot_313(raan, inc, argp)
    Omega = raan;
    i = inc;
    omega = argp;

    R11 = cos(omega) * cos(Omega) - sin(omega) * cos(i) * sin(Omega);
    R12 = -sin(omega) * cos(Omega) - cos(omega) * cos(i) * sin(Omega);
    R13 = sin(i) * sin(Omega);

    R21 = cos(omega) * sin(Omega) + sin(omega) * cos(i) * cos(Omega);
    R22 = -sin(omega) * sin(Omega) + cos(omega) * cos(i) * cos(Omega);
    R23 = -sin(i) * cos(Omega);

    R31 = sin(omega) * sin(i);
    R32 = cos(omega) * sin(i);
    R33 = cos(i);

    R = [R11 R12 R13; R21 R22 R23; R31 R32 R33];
end
