clear variables;
close all;
% clc;

x = [-4, 4, 0];

x1Hist = [x(1)];
x2Hist = [x(2)];
x3Hist = [x(3)];
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
        " x2: "+num2str(x(2)) + ...
        " x3: "+num2str(x(3)));
    x1Hist = [x1Hist; x(1)];
    x2Hist = [x2Hist; x(2)];
    x3Hist = [x3Hist; x(3)];
    fHist = [fHist; f];
    nHist = [nHist; n];
end

figure(2)
plot(nHist, fHist, "-ko", "Linewidth", 2);
set(gca, 'FontSize', 20, 'FontName', 'Times New Roman');
xlabel('Iteration');
ylabel('Objective Function');
