rng default

x = lhsdesign(10, 2, 'smooth', 'off');
Mt = x(:, 1);
Rt = x(:, 2);
Dt = (Mt - 0.3) .^ 2 + (Rt - 0.5) .^ 2 + 1;

samples = table(Mt, Rt, Dt);

disp('Samples:')
disp(samples)

X = [Mt Rt];
Y = Dt;

net_1 = fitrnet(X, Y, "LayerSizes", 3, "Activations", "sigmoid");
predictions_1 = predict(net_1, X);
mean_1 = mean((predictions_1 - Y) .^ 2);

disp('Mean (1 layer, 3 neurons):')
disp(mean_1)

net_2 = fitrnet(X, Y, "LayerSizes", [5 8], "Activations", "sigmoid");
predictions_2 = predict(net_2, X);
mean_2 = mean((predictions_2 - Y) .^ 2);

disp('Mean (2 layers, 5 + 8 neurons):')
disp(mean_2)

fprintf('\nMSE (1 layer, 3 neurons): %f\n', mean_1);
fprintf('MSE (2 layers, 5+8 neurons): %f\n', mean_2);

if mean_2 < mean_1
    disp('Net 2 (deeper) rocks!')
else
    disp('Net 1 (shallow) rocks!')
end

[Ms, Rs] = meshgrid(linspace(0, 1, 50), linspace(0, 1, 50));

grid_x = [Ms(:) Rs(:)];
grid_y = predict(net_2, grid_x);
grid_y = reshape(grid_y, size(Ms));

figure(1)

contourf(Ms, Rs, grid_y, 20); hold on;
plot(Mt, Rt, 'ko', 'MarkerFaceColor', 'k')

xlabel('M')
ylabel('R')
title('Predicted Dt Contours with LHS Sample Points')

grid on
