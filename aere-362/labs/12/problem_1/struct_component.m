function d = struct_component(theta, t, gamma)
K=[10*t(1)-theta(1) 1; 1 10*t(2)-theta(2)];
f=[gamma(1)^2; gamma(2)^2];
d = inv(K)*f;
end