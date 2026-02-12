import csv
from matplotlib import pyplot as plt
import numpy as np
import math

DENSITY = 1.225
CALIBRATION_POINTS = 5
TEST_MAX_DEPTH = 6.5
TEST_DEPTH_STEP = 0.5
TEST_DEPTHS = np.arange(0, TEST_MAX_DEPTH, TEST_DEPTH_STEP)
TEST_DEPTHS_WITHOUT_FIRST = TEST_DEPTHS[1:]


def read_voltage(path):
    with open(path) as file:
        lines = file.readlines()[5:]
        values = [float(line[-12:-4]) * 10 ** float(line[-2]) for line in lines]

    return sum(values) / len(values)


def read_pressure(path):
    with open(path) as file:
        reader = csv.reader(file)
        values = [float(row[2]) for row in reader]

    return sum(values) / len(values)


def calibrate():
    voltages, pressures = [], []

    for i in range(1, CALIBRATION_POINTS + 1):
        voltages.append(read_voltage(f"data/calibration/{i}.txt"))
        pressures.append(read_pressure(f"data/calibration/{i}.csv"))

    m, b = np.polyfit(voltages, pressures, 1)

    return m, b, voltages, pressures


def compute_velocities(depths, m, b):
    voltages, velocities = [], []

    for depth in depths:
        voltage = read_voltage(f"data/test/{depth}in.txt")
        voltages.append(voltage)
        pressures = m * voltage + b
        velocities.append(math.sqrt(2 * pressures / DENSITY))

    return depths, velocities, voltages


def plot_depth_velocity(depths, velocities, voltages, title):
    _, ax1 = plt.subplots()

    ax1.plot(depths, velocities, "o-", label="Velocity vs Depth", color="tab:blue")

    last_depth = depths[-1]
    mirrored_depths = [2 * last_depth - d for d in reversed(depths)]
    mirrored_velocities = velocities[::-1]

    ax1.plot(
        mirrored_depths,
        mirrored_velocities,
        ".--",
        label="Extrapolated",
        color="tab:blue",
    )

    ax1.set_xlabel("Depth (inches)")
    ax1.set_ylabel("Velocity (m/s)")
    ax1.grid()
    ax1.legend()

    ax2 = ax1.twinx()
    ax2.set_ylabel("Voltage (V)")
    ax2.set_ylim(min(voltages), max(voltages))

    plt.title(title)


def plot_calibration(voltages, pressures, m, b):
    plt.figure()
    plt.plot(voltages, pressures, "o", label="Data", color="tab:blue")
    plt.plot(
        voltages,
        m * np.array(voltages) + b,
        "--",
        label=f"Fit: y = {m:.3f}x + ({b:.3f})",
        color="tab:blue",
    )
    plt.xlabel("Voltage (V)")
    plt.ylabel("Pressure (Pa)")
    plt.title("Calibration")
    plt.grid()
    plt.legend()


m, b, voltages, pressures = calibrate()

plot_calibration(voltages, pressures, m, b)
plot_depth_velocity(
    *compute_velocities(TEST_DEPTHS, m, b), title="Velocity vs Depth & Voltage"
)
plot_depth_velocity(
    *compute_velocities(TEST_DEPTHS_WITHOUT_FIRST, m, b),
    title="Velocity vs Depth & Voltage (Excluding First Point)",
)

plt.show()
