function gamma = aero_component(theta, d)
A=[(theta(1)+d(1))^2+3 1;1 (theta(2)+d(2))^2+5];
b=[theta(1)+d(1); theta(2)+d(2)];
gamma = inv(A)*b;
end