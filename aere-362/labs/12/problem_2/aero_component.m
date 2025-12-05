function gamma = aero_component(theta, d, M)
A=[(theta(1)+d(1))^2+3+0.1*M 1;1 (theta(2)+d(2))^2+5+0.1*M];
b=[theta(1)+d(1)-0.1*M; theta(2)+d(2)-0.1*M];
gamma = inv(A)*b;
end