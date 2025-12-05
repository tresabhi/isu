clear
clc

theta=[0.6;0.3];
t=[1;0.5];

gamma = [0;0];
d=[0;0];

for i=1:10
    gamma = aero_component(theta, d);
    d = struct_component(theta, t, gamma);
end

disp(gamma)

disp(d)

