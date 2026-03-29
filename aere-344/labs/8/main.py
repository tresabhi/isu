import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

in_to_m = 1 / 39.37

u_inf = 13
rho = 1.225
nu = 1.57e-5
mu = nu * rho
Delta_y = 4 / 1000

is_ = list(range(0, 39))

# broken_indices = [2, 11, 17, 22]
broken_indices = [1, 15, 20, 21, 33, 34]
broken_indices = np.array(broken_indices)

xs_in = list(range(10)) + list(range(10, 65 + 5, 5))
xs = [x_in * in_to_m for x_in in xs_in]
ys = [Delta_y * i for i in is_]

xs = np.array(xs)
ys = np.array(ys)

ys_mm = ys * 1000


def boundary_model(y, d):
    return 1 - np.exp(-y / d)


deltas = []
deltas_theoretical = []
thetas = []


def plt_figure_1(name):
    plt.grid()
    plt.legend()
    plt.title(f"Velocity Profile vs Downstream Position ({name})")
    plt.ylabel("y [mm]")
    plt.xlabel("u / u_inf")
    plt.xlim(left=0.75, right=1)
    plt.ylim(bottom=0, top=1)


for x_in in xs_in:
    path = f"data/{x_in}in.csv"
    sample_range = x_in * in_to_m
    x = x_in * in_to_m

    with open(path) as file:
        reader = csv.reader(file)

        samples = []

        for row in reader:
            row = [float(cell) for cell in row]

            chunk_1 = row[2:18]
            chunk_2 = row[36:52]
            chunk_3 = row[70:86]

            sample = chunk_1 + chunk_2 + chunk_3

            samples.append(sample)

        mean_sample = np.mean(samples, axis=0)

        for broken in broken_indices:
            distance = 1 if broken < 18 else 2

            mean_sample[broken] = (
                mean_sample[broken - distance] + mean_sample[broken + distance]
            ) / 2

        p0_pitot = mean_sample[39 - 1]
        p_inf = mean_sample[40 - 1]
        p0 = np.array(mean_sample[0:39])

        q_inf = p0_pitot - p_inf
        q = np.maximum(0, p0 - p_inf)

        u_inf = np.sqrt((2 / rho) * q_inf)
        u = np.sqrt((2 / rho) * q)

        idx = np.argmax(u >= 0.99 * u_inf)

        u1 = u[idx - 1]
        u2 = u[idx]
        y1 = ys[idx - 1]
        y2 = ys[idx]

        Re_x = u_inf * x / nu
        delta = y1 + (0.99 * u_inf - u1) * (y2 - y1) / (u2 - u1)
        delta_theoretical = 0.37 * x * Re_x ** (-0.2)

        deltas.append(delta)
        deltas_theoretical.append(delta_theoretical)

        plt.plot(u / u_inf, ys / delta, label=f"x = {x_in}in")

        theta = np.sum((u / u_inf) * (1 - u / u_inf) * Delta_y)
        thetas.append(theta)

        if x_in == 10:
            plt_figure_1("Front")

            plt.savefig(f"out/velocity_profiles_front.png")
            plt.clf()


plt_figure_1("Back")
plt.savefig(f"out/velocity_profiles_back.png")

plt.clf()

deltas_mm = np.array(deltas) * 1000
deltas_theoretical_mm = np.array(deltas_theoretical) * 1000

plt.plot(xs_in, deltas_mm, label="Empirical")
plt.plot(xs_in, deltas_theoretical_mm, label="Theoretical")
plt.legend()
plt.title("Boundary Thickness vs Downstream Position")
plt.xlabel("x [in]")
plt.ylabel("delta [mm]")
plt.ylim(bottom=0)
plt.xlim(left=0, right=xs_in[-1])
plt.grid()
plt.savefig(f"out/boundary_thickness.png")

plt.clf()

plt.plot(xs_in, thetas)
plt.title("Momentum Thickness vs Downstream Position")
plt.xlabel("x [in]")
plt.ylabel("theta")
plt.ylim(bottom=0)
plt.xlim(left=0, right=xs_in[-1])
plt.grid()
plt.savefig(f"out/momentum_thickness.png")

# rake_sample = np.array(sample[0:38] + [0])
# total_sample = np.array(sample[38])
# static_sample = np.array(sample[39])

# valid = np.ones(len(rake_sample), dtype=bool)
# valid[broken_indices] = False
# sample_range = np.arange(len(rake_sample))
# rake_sample = np.interp(
#     sample_range, sample_range[valid], rake_sample[valid]
# )

# rake_sample = np.flip(rake_sample)
# rake_samples.append(rake_sample)
# total_samples.append(total_sample)
# static_samples.append(static_sample)

# p0 = np.mean(rake_samples, axis=0)
# p0_inf = np.mean(total_samples)
# p_inf = np.mean(static_samples)

# # print(p0)

# u = np.sqrt((2 * np.maximum(0, p0 - p_inf)) / rho)
# u_inf = np.sqrt((2 * (p0_inf - p_inf)) / rho)
# u[0] = 0

# Re_x = u_inf * x / nu

# popt, _ = curve_fit(boundary_model, ys, u / u_inf)
# d_fit = popt[0]
# delta = -d_fit * np.log(0.01)
# delta_theory = 0.37 * x * Re_x**-0.2

# idx99 = np.where(u > 0.99 * u_inf)[0][0]
# delta_last = ys[idx99]

# print(delta, delta_last, delta_theory)

# integrand_disp = 1 - u / u_inf
# delta_star = np.trapezoid(integrand_disp, ys)
# delta_star_theory = 0.048 * x * Re_x**-0.2

# C_D_theory = 0.074 * Re_x**-0.2

# [du_dy_wall, _] = np.polyfit(ys[0:4], u[0:4], 1)
# tau_w = mu * du_dy_wall
# C_f_theory = 0.058 * Re_x**-0.2
# tau_w_theory = C_f_theory * 0.5 * rho * u_inf**2

# theta = sum((u / u_inf) * (1 - u / u_inf) * Delta_y)

# profiles.append(u)
# deltas.append(delta)
# thetas.append(theta)

# ys_mm = ys * 1000

# sample_range, y = np.meshgrid(xs_in, ys_mm)
# z = np.array(profiles).T

# plt.figure(1)

# plt.contourf(sample_range, y, z)
# plt.colorbar(label="u [m/s]")

# plt.xlabel("x [in]")
# plt.ylabel("y [mm]")

# plt.title("Velocity Profile vs Downstream Position (Linear)")
# plt.savefig("out/velocity_profile_vs_downstream_position_linear_filled_contour.png")

# plt.yscale("symlog")

# plt.title("Velocity Profile vs Downstream Position (Logarithmic)")
# plt.savefig(
#     "out/velocity_profile_vs_downstream_position_linear_logarithmic_filled_contour.png"
# )

# plt.figure(2)

# plt.plot(xs_in, deltas)
# plt.savefig("out/boundary_thickness_vs_downstream_position.png")
