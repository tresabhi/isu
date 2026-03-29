import csv
import numpy as np
import matplotlib.pyplot as plt

in_to_m = 1 / 39.37

u_inf = 13
rho = 1.225
nu = 1.57e-5
mu = nu * rho
Delta_y = 4 / 1000

is_ = list(range(0, 39))

broken_indices = [2, 11, 17, 21, 22]
broken_indices = np.array(broken_indices)

xs_in = list(range(10)) + list(range(10, 65 + 5, 5))
xs = [x_in * in_to_m for x_in in xs_in]
ys = [Delta_y * i for i in is_]

xs = np.array(xs)
ys = np.array(ys)

profiles = []

for x_in in xs_in:
    path = f"data/{x_in}in.csv"
    sample_range = x_in * in_to_m
    x = x_in * in_to_m

    with open(path) as file:
        reader = csv.reader(file)

        rake_samples = []
        total_samples = []
        static_samples = []

        for row in reader:
            row = [float(cell) for cell in row]

            chunk_1 = row[2:18]
            chunk_2 = row[36:52]
            chunk_3 = row[70:86]

            sample = [0] + chunk_1 + chunk_2 + chunk_3
            rake_sample = np.array(sample[0:39])
            total_sample = np.array(sample[39])
            static_sample = np.array(sample[40])

            valid = np.ones(len(rake_sample), dtype=bool)
            valid[broken_indices] = False
            sample_range = np.arange(len(rake_sample))
            rake_sample = np.interp(
                sample_range, sample_range[valid], rake_sample[valid]
            )

            rake_samples.append(rake_sample)
            total_samples.append(total_sample)
            static_samples.append(static_sample)

        p0 = np.mean(rake_samples, axis=0)
        p0_inf = np.mean(total_samples)
        p_inf = np.mean(static_samples)

        u = np.sqrt((2 * np.maximum(0, p0 - p_inf)) / rho)
        u_inf = np.sqrt((2 * (p0_inf - p_inf)) / rho)
        u[0] = 0

        Re_x = u * sample_range / nu

        idx99 = np.where(u > 0.99 * u_inf)[0][0]
        delta = ys[idx99]
        delta_theory = 0.37 * x * Re_x**-0.2

        integrand_disp = 1 - u / u_inf
        delta_star = np.trapezoid(integrand_disp, ys)
        delta_star_theory = 0.048 * x * Re_x**-0.2

        C_D_theory = 0.074 * Re_x**-0.2

        [du_dy_wall, _] = np.polyfit(ys[0:4], u[0:4], 1)
        tau_w = mu * du_dy_wall
        C_f_theory = 0.058 * Re_x**-0.2
        tau_w_theory = C_f_theory * 0.5 * rho * u_inf**2

        profiles.append(u)


ys_mm = ys * 1000

sample_range, y = np.meshgrid(xs_in, ys_mm)
z = np.array(profiles).T

plt.figure(1)

plt.contourf(sample_range, y, z)
plt.colorbar(label="u [m/s]")

plt.xlabel("x [in]")
plt.ylabel("y [mm]")

plt.title("Velocity Profile vs Downstream Position (Linear)")
plt.savefig("out/velocity_profile_vs_downstream_position_linear_filled_contour.png")

plt.yscale("symlog")

plt.title("Velocity Profile vs Downstream Position (Logarithmic)")
plt.savefig(
    "out/velocity_profile_vs_downstream_position_linear_logarithmic_filled_contour.png"
)
