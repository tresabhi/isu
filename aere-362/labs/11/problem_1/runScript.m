theta = [0.6; 0.3];
t = [1; 0.5];
gamma = [1; 1];
d = [1; 1];

for i = 1:10
    gamma = aeroComp(theta, d);
    d = structComp(theta, t, gamma);
end

disp("gamma =")
disp(gamma)

disp("d =")
disp(d)
