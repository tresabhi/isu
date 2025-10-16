es = 1:0.5:4;
thetas = deg2rad(1:1:110);

figure(1); hold on; grid on;
title('E vs M');
xlabel('M (rad)');
ylabel('E (rad)');

figure(2); hold on; grid on;
title('θ vs M');
xlabel('M (rad)');
ylabel('\theta (deg)');

for e = es
    Es = true_to_ecc(e, thetas);
    Ms = ecc_to_mean(e, Es);

    figure(1);
    semilogy(Ms, Es, "DisplayName", sprintf("e = %.2f", e));

    figure(2);
    semilogy(rad2deg(thetas), rad2deg(Es), "DisplayName", sprintf("e = %.2f", e));
end
