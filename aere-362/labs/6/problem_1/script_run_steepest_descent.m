clear variables;
close all;
clc;

x = [-4, 4];

x1Hist = [x(1)];
x2Hist = [x(2)];
fHist = [objFunc(x)];
nHist = 0;
nFuncEvals = 0;
iter = 0;

for n = 0:100
    f = objFunc(x);
    c = objFuncDeriv(x);

    if norm(c) <= 1e-4
        break;
    else
        d = -c;
        alphaL = 0;
        alphaU = 10;
        tol = 1e-4;
        maxit = 50;

        [alphaMin, fMin, I, iter] = golden(x, d, alphaL, alphaU, tol, maxit);

        x = x + alphaMin * d;
    end

    nFuncEvals = nFuncEvals + iter + 1;
    disp("optIter: "+num2str(n) + ...
        " nFuncEvals: "+num2str(nFuncEvals) + ...
        " f: "+num2str(f) + ...
        " x1: "+num2str(x(1)) + ...
        " x2: "+num2str(x(2)));
    x1Hist = [x1Hist; x(1)];
    x2Hist = [x2Hist; x(2)];
    fHist = [fHist; f];
    nHist = [nHist; n];
end

% Optimization is done!

% plot results
figure(1)
[x1, x2] = meshgrid(-10:0.2:10, -10:0.2:10);
sizeX = size(x1);
fC = x1;

for i = 1:sizeX(1)

    for j = 1:sizeX(2)
        fC(i, j) = objFunc([x1(i, j), x2(i, j)]);
    end

end

fc = contour(x1, x2, fC, 0:50:500, 'k');
clabel(fc)
hold on;
plot(x1Hist, x2Hist, "-ro", "markerfacecolor", "r")
plot(x1Hist, x2Hist)
xlim([-10 10]);
ylim([-10 10]);
set(gca, 'FontSize', 20, 'FontName', 'Times New Roman');
xlabel('x1');
ylabel('x2');

figure(2)
plot(nHist, fHist, "-ko", "Linewidth", 2);
set(gca, 'FontSize', 20, 'FontName', 'Times New Roman');
xlabel('Iteration');
ylabel('Objective Function');
