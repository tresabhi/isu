function plotLS(x0, d0, alphaOpt)
    % Plot the line search function
    % Inputs:
    %     x0: current design variables
    %     d0: search direction
    % Outputs:
    %     It will pop up two plots

    alpha = 0:0.1:10;
    f = [];

    for a = alpha
        x = x0 + a * d0;
        f = [f, objFunc(x)];
    end

    % x-y plot for the line search function
    figure(1)
    plot(alpha, f, '-k');
    hold on;

    f0 = objFunc(x0);
    plot(0, f0, 'bo', 'markerfacecolor', 'r');

    if nargin > 2
        fOpt = objFunc(x0 + alphaOpt * d0);
        plot(alphaOpt, fOpt, 'bo', 'markerfacecolor', 'b');
    end

    xlabel('alpha');
    ylabel('f(alpha)');
    set(gca, 'FontSize', 20, 'FontName', 'Times New Roman');
    title("Line search function")

    % line search direction with the f contour
    figure(2)
    [x1, x2] = meshgrid(-10:0.2:10, -10:0.2:10);
    sizeX = size(x1);
    fC = x1;

    for i = 1:sizeX(1)

        for j = 1:sizeX(2)
            fC(i, j) = objFunc([x1(i, j), x2(i, j)]);
        end

    end

    fc = contour(x1, x2, fC, [0:50:500], 'k');
    clabel(fc)
    hold on;
    plot(x0(1), x0(2), 'ro', 'markerfacecolor', 'r')
    plot([x0(1), x0(1) + 100 * d0(1)], [x0(2), x0(2) + 100 * d0(2)], "--k");

    if nargin > 2
        plot(x0(1) + alphaOpt * d0(1), x0(2) + alphaOpt * d0(2), 'bo', 'markerfacecolor', 'b');
    end

    xlim([-10 10]);
    ylim([-10 10]);
    xlabel('x1');
    ylabel('x2');
    set(gca, 'FontSize', 20, 'FontName', 'Times New Roman');
    title("Objective function contour")

end
