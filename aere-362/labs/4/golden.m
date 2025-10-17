function [alphaMin, fMin, I, iter] = golden(x0, d, alphaL, alphaU, tol, maxit)
    % golden: golden section search
    %   [alphaMin,fMin,error,iter]=gold(alphaL,alphaU,tol,maxit):
    %     uses golden section line search to find the minimum of f
    % input:
    %   x0 = Initial design variable where alpha=0
    %   d = search direction
    %   alphaL, alphaU = lower and upper bounds for alpha (initial bracket)
    %   tol = desired tolerance for I
    %   maxit = maximum allowable iterations
    % output:
    %   alphaMin = location of minimum
    %   fMin = minimum function value
    %   I = interval of uncertainty
    %   iter = number of iterations

    for iter = 0:maxit
        % Calculate the interval of uncertainty I
        I = alphaU - alphaL;
        % Check if I is less than the tolerance
        % if yes, quit the loop
        if I <= tol
            break
        else
            % *************************************************
            % Write some codes here to update alphaL and alphaU
            % *************************************************
            % Step 1:
            %     Calculate alphaA and alphaB to divide I into three segments
            % Hint:
            %     alphaA = alphaL + 0.382*I
            %     alphaB = alphaU - 0.382*I
            % Step 2:
            %     Calculate xA and xB based on alphaA and alphaB
            % Hint:
            %     Use xA = x0 + alphaA * d for xA and similarly for xB
            % Step 3:
            %     Calculate fA and fB based on xA and xB
            % Hint:
            %     Use this command fA = objFunc(xA) to compute fA
            %     Similarly for fB
            % Step 4:
            %     Check the values of fA and fB
            % Hint:
            %     If fA > fB, then we assign alphaA to alphaL (alphaU unchanged)
            %     If fA < fB, then we assign alphaB to alphaU (alphaL unchanged)

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

        % alphaL and alphaU are updated, now compute alphaMin and fMin
        % alphaMin will be the average of alphaL and alphaU
        alphaMin = (alphaL + alphaU) / 2.0;
        % calculate the new x based on x0, alphaMin, and d
        x = x0 + alphaMin * d;
        % calculat the fMin based on x
        fMin = objFunc(x);

    end

    % Print some info to the screen
    disp("lsIter: "+num2str(iter) + " alpha: "+num2str(alphaMin) + ...
        " I: "+num2str(I) + " f: "+num2str(fMin));
