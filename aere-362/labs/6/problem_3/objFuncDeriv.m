function c=objFuncGrad(x)
% df/dx1
c(1) = 2*x(1) - 4 -2*x(2);
c(2) = 4*x(2) - 2*x(1);
end