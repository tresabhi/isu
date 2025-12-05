clear
clc

theta=[0.6;0.3];
t=[1;0.5];
M=1;

gamma = [1;1];
d=[1;1];
T=[1;1];

for i=1:10
    gamma = aero_component(theta, d, M);
    d = struct_component(theta, t, gamma, T);
    T = thermo_component(theta, t, M, d);
end

disp(gamma)

disp(d)

disp(T)

