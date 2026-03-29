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

# broken_indices = [1, 7, 10, 16, 17, 21, 22, 33, 35]
broken_indices = [2, 11, 17, 21, 22]
broken_indices = np.array(broken_indices)
broken_indices -= 1

xs_in = list(range(10)) + list(range(10, 65 + 5, 5))
xs = [x_in * in_to_m for x_in in xs_in]
ys = [Delta_y * i for i in is_]

xs = np.array(xs)
ys = np.array(ys)

profiles = []

for x_in in xs_in:
    path = f"data/{x_in}in.csv"
    sample_range = x_in * in_to_m

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

        u = np.sqrt((2 * np.abs(p0 - p_inf)) / rho)
        u_inf = np.sqrt((2 * (p0_inf - p_inf)) / rho)

        Re_x = u * sample_range / nu

        profiles.append(u)

        # u = math.sqrt((2 * (p0 - p)) / rho)


ys_mm = ys * 1000

sample_range, y = np.meshgrid(xs_in, ys_mm)
z = np.array(profiles).T

plt.figure(1)

plt.contourf(sample_range, y, z, levels=2**8)
plt.colorbar(label="Velocity [m/s]")

plt.xlabel("x [in]")
plt.ylabel("y [mm]")

plt.title("Velocity Profile vs x (Linear)")
plt.savefig("out/velocity_profile_vs_x_linear.png")

plt.yscale("log")

plt.title("Velocity Profile vs x (Logarithmic)")
plt.savefig("out/velocity_profile_vs_x_logarithmic.png")
