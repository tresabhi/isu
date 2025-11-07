theta0 = 0;
r0 = 1;
vTheta0 = 1 + 0.1;
vr0 = 0;
state0 = [theta0; r0; vTheta0; vr0];

tSpan = linspace(0, 5, 100);
[tProp, stateProp] = ode45(@(t, state) dynEqn(t, state), tSpan, state0);

polarplot(0, 0, 'ro', 'MarkerSize', 20);
hold on;
polarplot(theta0, r0, 'bo');

thetaProp = stateProp(:, 1);
rProp = stateProp(:, 2);

polarplot(thetaProp, rProp, '-r');
rlim([0, 3]);
