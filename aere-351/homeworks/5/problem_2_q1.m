Ms = deg2rad(0:1:359);
es = 0:0.05:0.95;

figure(1); hold on; grid on;
title('E vs M');
xlabel('M (rad)');
ylabel('E (rad)');

figure(2); hold on; grid on;
title('θ vs M');
xlabel('M (rad)');
ylabel('\theta (deg)');

for e = es
    Es = mean_to_ecc(e, Ms);
    thetas = ecc_to_true(Es, e);

    figure(1);
    plot(Ms, Es, "DisplayName", sprintf("e = %.2f", e));

    figure(2);
    plot(Ms, rad2deg(thetas), "DisplayName", sprintf("e = %.2f", e));
end
