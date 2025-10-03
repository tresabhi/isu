function [alphaMin, fMin, I, iter] = golden(x0, d, alphaL, alphaU, tol, maxit)

    for iter = 0:maxit
        I = alphaU - alphaL;

        if I <= tol
            break
        else
            alphaA = alphaL + 0.382 * I;
            alphaB = alphaU - 0.382 * I;

            xA = x0 + alphaA * d;
            xB = x0 + alphaB * d;

            fA = objFunc(xA);
            fB = objFunc(xB);

            if fA > fB
                alphaL = alphaA;
            else
                alphaU = alphaB;
            end

        end

        alphaMin = (alphaL + alphaU) / 2.0;
        x = x0 + alphaMin * d;
        fMin = objFunc(x);
    end

    disp("lsIter: "+num2str(iter) + " alpha: "+num2str(alphaMin) + ...
        " I: "+num2str(I) + " f: "+num2str(fMin));
