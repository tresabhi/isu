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
