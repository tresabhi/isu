import csv
import math
import numpy as np
import matplotlib.pyplot as plt

in_to_m = 1 / 39.37

u_inf = 13
rho = 1.225
delta = 4 / 1000

xs_in = list(range(10)) + list(range(10, 65 + 5, 5))

rakes = []

for x_in in xs_in:
    path = f"data/{x_in}in.csv"
    x = x_in * in_to_m

    with open(path) as file:
        reader = csv.reader(file)

        rake_samples = []
        total_samples = []
        static_samples = []
        n = 0

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

            n += 1

        rake = np.mean(rake_samples, axis=0)

        rakes.append(rake)

        p0 = np.mean(total_samples)
        p = np.mean(static_samples)

        # u = math.sqrt((2 * (p0 - p)) / rho)

xs = [x_in * in_to_m for x_in in xs_in]
ys = [delta * i for i in range(1, 39)]

x, y = np.meshgrid(xs, ys)
z = np.array(rakes).T

plt.contourf(x, y, z)
plt.colorbar(label="Velocity")
plt.savefig("out/1.png")
