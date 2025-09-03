clear; close all; clc;

%% Example of Numerical Propagation %%

%% Problem Set Up
t0 = 0; % Initial time
tf = 2; % seconds, final time
y0 = 3; % initial state condition
np = 101; % number of steps

%% Evaluate Exact Solution
time = linspace(t0, tf, np);
% (solve the ode)
% dx/dt = -2x
% 1/x dx = -2 dt
% ln x = -2t + C
% x = exp(-2t + C) = exp(-2t) exp(C) = A exp(-2t)
% IC x(0) = 3 -> A = 3

ytrue = 3 * exp(-2 * time);

figure(101);
plot(time, ytrue, 'LineWidth', 2); hold on;
ylabel('y(t)'); xlabel('time [s]'); title('Solution');
legend('Truth');

%% Runge-Kutta Order 1 - Euler's Method %%

% Set up
step_size = 0.2; % seconds, step size for the fixed time step integration
yrk1_old = y0;
yRK1history = y0;
step = t0;
trk1 = step;

% Integration
while step + step_size <= tf
    k1 = RHS(step, yrk1_old);
    yhalfway = yrk1_old + k1 * step_size;

    yRK1history = [yRK1history yhalfway];

    yrk1_old = yhalfway;
    step = step + step_size;
    trk1 = [trk1, step];
end

figure(101);
plot(trk1, yRK1history, '*-r', 'LineWidth', 2);
legend('Truth', 'RK1 - Euler');

% repeat by changing step_size to see how accuracy works

%% Runge-Kutta Order 2 - Heun's Method %%

% Set up
step_size = 0.2; % seconds, step size for the fixed time step integration
yrk2_old = y0;
yRK2history = y0;
step = t0;
trk2 = step;

% Integration
while step + step_size <= tf

    k1 = RHS(step, yrk2_old);
    yhalfway = yrk2_old + k1 * (step_size / 2);
    k2 = RHS(step + step_size / 2, yhalfway);
    yrk2_new = yrk2_old + k2 * step_size;

    yRK2history = [yRK2history, yrk2_new];

    yrk2_old = yrk2_new;
    step = step + step_size;
    trk2 = [trk2, step];

end

figure(101);
plot(trk2, yRK2history, '*-g', 'LineWidth', 2);
legend('Truth', 'RK1 - Euler', 'RK2 - Heun');

%% Runge-Kutta 4(5) %%
ode_options = odeset('RelTol', 1e-6, 'AbsTol', 1e-6);
[t, y] = ode45(@(t, x) RHS(t, x), trk2, y0, ode_options);

figure(101);
plot(t, y, '*-y', 'LineWidth', 2);
legend('Truth', 'RK1 - Euler', 'RK2 - Heun', 'RK4(5)');

%% Auxiliary Functions %%
function xdot = RHS(t, x)
    xdot = -2 * x;
end
