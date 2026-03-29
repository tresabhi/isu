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

Re_tr = 5e5
x_tr = (Re_tr * nu) / u_inf
delta_tr = 5 * x_tr / np.sqrt(Re_tr)

is_ = list(range(0, 39))

# broken_indices = [2, 11, 17, 22]
broken_indices = []
broken_indices = [1, 20, 21]
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
velocity_profiles = []
pressure_profiles = []


def plt_figure_1(name):
    plt.grid()
    plt.legend()
    plt.title(f"Velocity Profile vs Downstream Position ({name})")
    plt.ylabel("y [mm]")
    plt.xlabel("u / u_inf")
    plt.xlim(left=0.75, right=1)
    plt.ylim(bottom=0, top=1.75)


for x_in in xs_in:
    path = f"data/{x_in}in.csv"
    profile_range = x_in * in_to_m
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
        p0 = np.array(mean_sample[0:38])

        q_inf = p0_pitot - p_inf
        q = np.maximum(0, p0 - p_inf)

        pressure_profiles.append([p0[0]] + list(p0))

        u_inf = np.sqrt((2 / rho) * q_inf)
        u = np.sqrt((2 / rho) * q)
        u = [0] + list(u)

        # plt.clf()
        # plt.plot(is_, list(u))
        # plt.savefig(f"out/{x_in}in.png")

        velocity_profiles.append(u)

        idx = np.argmax(u >= 0.99 * u_inf)

        u1 = u[idx - 1]
        u2 = u[idx]
        y1 = ys[idx - 1]
        y2 = ys[idx]

        Re_x = u_inf * x / nu
        delta = y1 + (0.99 * u_inf - u1) * (y2 - y1) / (u2 - u1)

        if x < x_tr:
            delta_theoretical = 5 * x / np.sqrt(Re_x)
        else:
            delta_theoretical = delta_tr + 0.37 * (
                x / (Re_x ** (1 / 5)) - x_tr / (Re_tr ** (1 / 5))
            )

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

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

profile_range, y = np.meshgrid(xs_in, ys_mm)
z = np.array(pressure_profiles).T

# 3D surface plot
surf = ax.plot_surface(profile_range, y, z, cmap="viridis")

# Colorbar
fig.colorbar(surf, ax=ax, label="p0 [Pa]")

# Labels
ax.set_xlabel("x [in]")
ax.set_ylabel("y [mm]")
ax.set_zlabel("p0 [Pa]")

ax.set_title("Pressure Profile vs Downstream Position (3D)")

plt.savefig("out/dynamic_pressure_profile_3d.png")

plt.clf()

z = np.array(velocity_profiles).T

plt.contourf(profile_range, y, z)
plt.colorbar(label="u [m/s]")
plt.xlabel("x [in]")
plt.ylabel("y [mm]")

plt.title("Velocity Profile vs Downstream Position (Linear)")
plt.savefig("out/velocity_profile_linear.png")

plt.yscale("symlog")

plt.title("Velocity Profile vs Downstream Position (Logarithmic)")
plt.savefig("out/velocity_profile_logarithmic.png")

plt.clf()

d_theta = np.diff(thetas)
d_x = np.diff(xs)
C_f = 2 * d_theta / d_x

Re_x = u_inf * xs / nu
C_f_theoretical = 0.0583 / (Re_x**0.2)

plt.plot(xs_in[:-1], C_f, label="Empirical")
plt.plot(xs_in[:-1], C_f_theoretical[:-1], label="Theoretical")
plt.title("Local Shear Stress vs Downstream Position")
plt.xlabel("x [in]")
plt.ylabel("C_f")
plt.xlim(left=0, right=xs_in[-1])
plt.ylim(bottom=0, top=0.01)
plt.legend()
plt.grid()
plt.savefig(f"out/locale_shear_stress.png")

L = 65 * in_to_m
C_D = 2 * thetas[-1] / L
C_D_theoretical = 0.075 / (Re_x[-1] ** 0.2)

print(f"C_D = {C_D}")
print(f"C_D_theoretical = {C_D_theoretical}")
