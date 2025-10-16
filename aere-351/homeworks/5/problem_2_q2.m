Ms = deg2rad(1:1:179);
es = 1:0.5:4;

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
    semilogy(Ms, Es, "DisplayName", sprintf("e = %.2f", e));

    figure(2);
    semilogy(Ms, rad2deg(thetas), "DisplayName", sprintf("e = %.2f", e));
end
