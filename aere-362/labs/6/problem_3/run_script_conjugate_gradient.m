clear;
close;
clc;

x=[-4 4];
eps=1e-4;
alphaL=0;
alphaU=10;
maxit=50;

x1Hist=[x(1)];
x2Hist=[x(2)];

for k=0:100

    if k==0
        % steepest descent
        f=objFunc(x);
        c=objFuncDeriv(x);
        cNorm = norm(c);
        if cNorm < eps
            disp("Optimization converged!")
            break
        else
            d = -c;
            [alphaMin,fMin,I,iter]=golden(x,d,alphaL,alphaU,eps,maxit);
            x=x+alphaMin*d;
        end
    else
        % conjugate gradient
        f=objFunc(x);
        cPrev = c;
        c=objFuncDeriv(x);
        cNorm = norm(c);
        if cNorm < eps
            disp("Optimization converged!")
            break
        else
            dPrev = d;
            beta = (norm(c)/norm(cPrev))^2;
            % conjugate gradient formulation
            d = -c + beta * dPrev;
            [alphaMin,fMin,I,iter]=golden(x,d,alphaL,alphaU,eps,maxit);
            x=x+alphaMin*d;
        end
    end
    
    x1Hist=[x1Hist, x(1)];
    x2Hist=[x2Hist, x(2)];
    disp("Iteration: "+num2str(k) ...
        +" norm(c): "+num2str(cNorm) ...
        +" f: "+num2str(f))
end

disp(x);

figure(2)
[x1,x2] = meshgrid(-10:0.2:10,-10:0.2:10);
sizeX = size(x1);
fC=x1;
for i = 1:sizeX(1)
    for j=1:sizeX(2)
        xA = x1(i,j);
        xB = x2(i,j);
        fC(i,j)=objFunc([xA, xB]);
    end
end
fc=contour(x1,x2,fC,[0:50:500], 'k');
clabel(fc)
hold on;
plot(x1Hist,x2Hist, "-or")
%plot([x0(1),x0(1)+10*d0(1)], [x0(2),x0(2)+10*d0(2)], '--b')