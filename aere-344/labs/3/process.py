import csv
from matplotlib import pyplot as plt
import numpy as np
import math

CALIBRATION_POINTS = 5
TEST_RANGE = np.arange(0, 6.5, 0.5)
DENSITY = 1.225

voltages = []
pressures = []


def read_voltage(path):
    voltages = []

    with open(path) as file:
        lines = file.readlines()[5:]

        for line in lines:
            magnitude = float(line[-12:-4])
            power = float(line[-2])
            voltage = magnitude * 10**power
            voltages.append(voltage)

    return sum(voltages) / len(voltages)


def read_pressure(path):
    pressures = []

    with open(path) as file:
        reader = csv.reader(file)
        for row in reader:
            pressure = float(row[2])
            pressures.append(pressure)

    return sum(pressures) / len(pressures)


for index in range(CALIBRATION_POINTS):
    name = index + 1
    voltage = read_voltage((f"data/calibration/{name}.txt"))
    pressure = read_pressure((f"data/calibration/{name}.csv"))

    voltages.append(voltage)
    pressures.append(pressure)

m, b = np.polyfit(voltages, pressures, 1)

plt.figure()
[dots] = plt.plot(voltages, pressures, "o", label="Data")
plt.plot(
    voltages,
    m * np.array(voltages) + b,
    "--",
    label=f"Fit: y = {m:.3f}x + ({b:.3f})",
    color=dots.get_color(),
)
plt.xlabel("Voltage (V)")
plt.ylabel("Pressure (Pa)")
plt.title("Calibration")
plt.grid()
plt.legend()


velocities = []

for depth in TEST_RANGE:
    voltage = read_voltage(f"data/test/{depth}in.txt")
    pressure = m * voltage + b
    velocity = math.sqrt(2 * pressure / DENSITY)
    velocities.append(velocity)

plt.figure()
plt.plot(TEST_RANGE, velocities, "o-", label="Velocity vs Depth")
plt.xlabel("Depth (inches)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity vs Depth")
plt.grid()
plt.legend()

plt.show()
