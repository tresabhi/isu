from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import csv

in_to_m = 1 / 39.37

rho = 1.225
nu = 1.57e-5
Delta_y_mm = 4
u_inf = 13
Delta_y = Delta_y_mm / 1000

Re_tr = 5e5
x_tr = (Re_tr * nu) / u_inf
delta_tr = 5 * x_tr / np.sqrt(Re_tr)

broken_pressures = [2, 16, 21, 22, 35]
broken_deltas = 3

xs_in = list(range(10)) + list(range(10, 65 + 5, 5))
ys = np.array(range(39)) * Delta_y
ys_mm = ys * 1000


def u_model(y, a, b):
    return a * np.sqrt(y) + b


def u_fit(y):
    return a * np.sqrt(y) + b


u_profiles = []
u_profiles_normalized = []
q_profiles = []
deltas = []
deltas_theoretical = []
thetas = []


fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.set_xlabel("u / u_inf")
ax1.set_ylabel("y / delta")
ax1.set_title("Velocity Profile vs Downstream Position")
ax1.set_xlim(left=0.6, right=1)
ax1.set_ylim(bottom=0, top=1.25)

ax2.set_xlabel("u / u_inf")
ax2.set_ylabel("y / delta")
ax2.set_title("Velocity Profile vs Downstream Position")
ax2.set_xlim(left=0.6, right=1)
ax2.set_ylim(bottom=0, top=1.4)

i = 0
for x_in in xs_in:
    path = f"data/{x_in}in.csv"
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

        p_static = mean_sample[40 - 1]

        for broken in broken_pressures:
            d = 1 if broken < 20 else 2
            mean_sample[broken - 1] = (
                mean_sample[broken - 1 - d] + mean_sample[broken - 1 + d]
            ) / 2
            # mean_sample[i - 1] = p_static

        p_pitot = mean_sample[39 - 1]
        p_rake = np.array(mean_sample[0:38])

        q_rake = np.maximum(0, p_rake - p_static)
        q_rake = np.array([0] + list(q_rake))
        q_pitot = p_pitot - p_static

        u_inf = np.sqrt((2 / rho) * q_pitot)
        us = np.sqrt((2 / rho) * q_rake)

        if len(deltas) < len(xs_in) - broken_deltas:
            u99 = 0.99 * u_inf

            params, _ = curve_fit(u_model, ys, us)
            a, b = params
            delta = ((u99 - b) / a) ** 2
        else:
            delta = deltas[-1]

        x = max(0.000001, x)
        Re_x = u_inf * x / nu

        if x < x_tr:
            delta_theoretical = 5 * x / np.sqrt(Re_x)
        else:
            delta_theoretical = delta_tr + 0.37 * (
                x / (Re_x ** (1 / 5)) - x_tr / (Re_tr ** (1 / 5))
            )

        theta = np.sum((us / u_inf) * (1 - us / u_inf) * Delta_y)

        if i > 10:
            ax = ax2
        else:
            ax = ax1

        ax.plot(us / u_inf, ys / delta, label=f"x = {x_in}in")

        u_profiles.append(us)
        u_profiles_normalized.append(us / u_inf)
        q_profiles.append(q_rake)
        deltas.append(delta)
        deltas_theoretical.append(delta_theoretical)
        thetas.append(theta)

    i += 1

ax1.legend()
ax2.legend()

Q = np.array(q_profiles)

plt.figure(3)
plt.title("Dynamic Pressure Field")
plt.imshow(
    Q.T,
    aspect="auto",
    origin="lower",
    extent=[min(xs_in), max(xs_in), min(ys_mm), max(ys_mm)],
)
plt.colorbar(label="q [Pa]")
plt.xlabel("x [in]")
plt.ylabel("y [mm]")

U = np.array(u_profiles)

plt.figure(4)
plt.title("Velocity Field")
plt.imshow(
    U.T,
    aspect="auto",
    origin="lower",
    extent=[min(xs_in), max(xs_in), min(ys_mm), max(ys_mm)],
)
plt.colorbar(label="u [m/s]")
plt.xlabel("x [in]")
plt.ylabel("y [mm]")

deltas = np.array(deltas)
deltas_mm = deltas * 1000
deltas_theoretical = np.array(deltas_theoretical)
deltas_theoretical_mm = deltas_theoretical * 1000

plt.figure(5)
plt.title("Delta vs Downstream Position")
plt.plot(xs_in, deltas_mm, label="delta")
plt.plot(xs_in, deltas_theoretical_mm, label="delta_theoretical")
plt.xlabel("x [in]")
plt.ylabel("delta [mm]")
plt.legend()

plt.figure(6)
plt.title("Theta vs Downstream Position")
plt.plot(xs_in, thetas)
plt.xlabel("x [in]")
plt.ylabel("theta")

plt.show()
