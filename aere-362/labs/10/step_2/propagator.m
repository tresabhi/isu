function [theta, r] = propagator(x, plot)
    dVTheta = x(1);
    dVr = x(2);
    tof = x(3);

    theta0 = 0;
    r0 = 1;
    vTheta0 = 1 + dVTheta;
    vr0 = 0 + dVr;
    state0 = [theta0; r0; vTheta0; vr0];

    tSpan = linspace(0, tof, 100);
    [tProp, stateProp] = ode45(@(t, state) dynEqn(t, state), tSpan, state0);
    theta = stateProp(:, 1);
    r = stateProp(:, 2);

    if (plot == 1)
        polarplot(0, 0, 'ro', 'MarkerSize', 20);
        hold on;
        polarplot(theta0, r0, 'bo');

        thetaProp = stateProp(:, 1);
        rProp = stateProp(:, 2);

        polarplot(thetaProp, rProp, '-r');
        rlim([0, 3]);
    end

end
