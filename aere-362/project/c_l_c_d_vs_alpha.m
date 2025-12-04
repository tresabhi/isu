alpha = [1, 2, 3];
CL = [0.10339017, 0.20600859, 0.30687305];
CD = [0.01247696, 0.01308758, 0.01411271];

figure;
plot(alpha, CL, 'o-');
xlabel('\alpha (deg)');
ylabel('C_L');
title('Lift Coefficient vs Angle of Attack');
grid on;

figure;
plot(alpha, CD, 'o-');
xlabel('\alpha (deg)');
ylabel('C_D');
title('Drag Coefficient vs Angle of Attack');
grid on;
