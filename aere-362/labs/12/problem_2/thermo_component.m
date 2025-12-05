function T = thermo_component(theta, t, M, d)
L=[1/(t(1)+d(1)+theta(1)) 1 ; 1 1/(t(2)+d(2)+theta(2))];
s=[M;M];
T=inv(L)*s;
end