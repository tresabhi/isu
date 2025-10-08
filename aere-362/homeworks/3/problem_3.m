x = [20, 10];
eps = 1e-4;
alphaL = 0;
alphaU = 10;
maxit = 50;

x1Hist = [x(1)];
x2Hist = [x(2)];
fHist = [objFunc(x)];
fVariationHist = [];

for k = 0:100

    if k == 0
        f = objFunc(x);
        c = objFuncDeriv(x);
        cNorm = norm(c);

        if cNorm < eps
            disp("Optimization converged!")
            break
        else
            d = -c;
            [alphaMin, fMin, I, iter] = golden(x, d, alphaL, alphaU, eps, maxit);
            x = x + alphaMin * d;
        end

    else
        f = objFunc(x);
        cPrev = c;
        c = objFuncDeriv(x);
        cNorm = norm(c);

        if cNorm < eps
            disp("Optimization converged!")
            break
        else
            dPrev = d;
            beta = (norm(c) / norm(cPrev)) ^ 2;
            d = -c + beta * dPrev;
            [alphaMin, fMin, I, iter] = golden(x, d, alphaL, alphaU, eps, maxit);
            x = x + alphaMin * d;
        end

    end

    x1Hist = [x1Hist, x(1)];
    x2Hist = [x2Hist, x(2)];
    fVariationHist = [fVariationHist, abs(f - fHist(end))];
    fHist = [fHist, f];
    disp("Iteration: "+num2str(k) ...
        + " norm(c): "+num2str(cNorm) ...
        + " f: "+num2str(f))
end

disp(x);
disp("f_min = " + num2str(x2Hist(end)));

figure(1)
[x1, x2] = meshgrid(-5:0.2:30, -5:0.2:15);
sizeX = size(x1);
fC = x1;

for i = 1:sizeX(1)

    for j = 1:sizeX(2)
        xA = x1(i, j);
        xB = x2(i, j);
        fC(i, j) = objFunc([xA, xB]);
    end

end

fc = contour(x1, x2, fC, [0:50:500], 'k');
clabel(fc)
hold on;
plot(x1Hist, x2Hist, "-or")

figure(2)
plot(fVariationHist(2:end))

function f = objFunc(x)
    f = x(1) ^ 2 + 3 * x(2) ^ 2 - x(1) * x(2) - 7 * x(1) - 7 * x(2);
end

function c = objFuncDeriv(x)
    c(1) = 2 * x(1) - x(2) - 7;
    c(2) = 6 * x(2) - x(1) - 7;
end

function [alphaMin, fMin, I, iter] = golden(x0, d0, alphaL, alphaU, eps, maxit)

    for iter = 0:maxit
        I = alphaU - alphaL;

        if I < eps
            break;
        else
            alphaA = alphaL + 0.382 * I;
            alphaB = alphaU - 0.382 * I;
            xA = x0 + alphaA * d0;
            xB = x0 + alphaB * d0;
            fA = objFunc(xA);
            fB = objFunc(xB);

            if fA < fB
                alphaU = alphaB;
            else
                alphaL = alphaA;
            end

            alphaMin = (alphaL + alphaU) / 2;
            xMin = x0 + alphaMin * d0;
            fMin = objFunc(xMin);

        end

    end

end
