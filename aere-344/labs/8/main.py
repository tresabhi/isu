import csv
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

in_to_m = 1 / 39.37

u_inf = 13
rho = 1.225
nu = 1.57e-5
Delta_y = 4 / 1000

is_ = list(range(1, 39))

broken_indices = [56]

xs_in = list(range(10)) + list(range(10, 65 + 5, 5))
xs = [x_in * in_to_m for x_in in xs_in]
ys = [Delta_y * i for i in is_]

xs = np.array(xs)
ys = np.array(ys)

profiles = []

for x_in in xs_in:
    path = f"data/{x_in}in.csv"
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

            sample = chunk_1 + chunk_2 + chunk_3
            rake_sample = np.array(sample[0:38])
            total_sample = np.array(sample[38])
            static_sample = np.array(sample[39])

            rake_samples.append(rake_sample)
            total_samples.append(total_sample)
            static_samples.append(static_sample)

        p0 = np.mean(rake_samples, axis=0)
        p0_inf = np.mean(total_samples)
        p_inf = np.mean(static_samples)

        u = np.sqrt((2 * np.abs(p0 - p_inf)) / rho)
        u_inf = np.sqrt((2 * (p0_inf - p_inf)) / rho)

        Re_x = u * x / nu

        profiles.append(u)

        # u = math.sqrt((2 * (p0 - p)) / rho)


ys_mm = ys * 1000

x, y = np.meshgrid(xs_in, ys_mm)
z = np.array(profiles).T

plt.figure(1)

plt.contourf(x, y, z, levels=2**8)
plt.colorbar(label="Velocity [m/s]")

plt.xlabel("x [in]")
plt.ylabel("y [mm]")

plt.title("Velocity profile vs x (linear)")
plt.savefig("out/velocity_profile_vs_x_linear.png")

plt.yscale("log")

plt.title("Velocity profile vs x (logarithmic)")
plt.savefig("out/velocity_profile_vs_x_logarithmic.png")
