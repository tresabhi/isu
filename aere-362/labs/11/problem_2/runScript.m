theta = [0.6; 0.3];
t = [1; 0.5];
gamma = [1; 1];
d = [1; 1];
M = 1;
T = [1; 1];

for i = 1:10
    gamma = aeroComp(theta, d, M);
    d = structComp(theta, t, gamma, T);
    T = thermoComp(theta, t, d, M);
end

disp("gamma =")
disp(gamma)

disp("d =")
disp(d)

disp("T =")
disp(T)
