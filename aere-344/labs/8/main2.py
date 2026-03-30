import matplotlib.pyplot as plt
import numpy as np
import csv

rho = 1.225
Delta_y_mm = 4
Delta_y = Delta_y_mm / 1000

xs_in = list(range(10)) + list(range(10, 65 + 5, 5))
ys = np.array(range(39)) * Delta_y

velocity_profiles = []
velocity_profiles_normalized = []
y_profiles = []
deltas = []

for x_in in xs_in:
    path = f"data/{x_in}in.csv"

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

        p_pitot = mean_sample[39 - 1]
        p_static = mean_sample[40 - 1]
        p_rake = np.array(mean_sample[0:38])

        q_rake = np.maximum(0, p_rake - p_static)
        q_rake = np.array([0] + list(q_rake))
        q_pitot = p_pitot - p_static

        u_inf = np.sqrt((2 / rho) * q_pitot)
        u_rake = np.sqrt((2 / rho) * q_rake)

        idx = np.argmax(u_rake >= 0.99 * u_inf)

        u1 = u_rake[idx - 1]
        u2 = u_rake[idx]
        y1 = ys[idx - 1]
        y2 = ys[idx]

        u99 = 0.99 * u_inf
        delta = y1 + ((u99 - u1) / (u2 - u1)) * (y2 - y1)
        y_profile = ys / delta

        velocity_profiles.append(u_rake)
        velocity_profiles_normalized.append(u_rake / u_inf)
        y_profiles.append(y_profile)
        deltas.append(delta)


U = np.array(velocity_profiles)

plt.figure()
plt.title("Velocity Field")
plt.imshow(U.T, aspect="auto", origin="lower")
plt.colorbar(label="u [m/s]")
plt.xlabel("x [in]")
plt.ylabel("y [mm]")

deltas = np.array(deltas)
deltas_mm = deltas * 1000

plt.figure()
plt.title("Delta vs Downstream Position")
plt.plot(xs_in, deltas_mm)
plt.xlabel("x [in]")
plt.ylabel("delta [mm]")

plt.show()
