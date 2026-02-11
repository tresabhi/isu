import csv
from matplotlib import pyplot as plt
import numpy as np

CALIBRATION_POINTS = 5

voltages = []
pressures = []

for index in range(CALIBRATION_POINTS):
    name = index + 1

    point_voltages = []
    point_pressures = []

    with open(f"data/calibration/{name}.txt") as file:
        lines = file.readlines()[5:]

        for line in lines:
            magnitude = float(line[-12:-4])
            power = float(line[-2])
            voltage = magnitude * 10**power
            point_voltages.append(voltage)

    with open(f"data/calibration/{name}.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            pressure = float(row[2])
            point_pressures.append(pressure)

    pressure = sum(point_pressures) / len(point_pressures)
    voltage = sum(point_voltages) / len(point_voltages)

    voltages.append(voltage)
    pressures.append(pressure)

m, b = np.polyfit(voltages, pressures, 1)

# [dots] = plt.plot(voltages, pressures, "o", label="Data")
# plt.plot(
#     voltages,
#     m * np.array(voltages) + b,
#     "--",
#     label=f"Fit: y = {m:.3f}x + ({b:.3f})",
#     color=dots.get_color(),
# )

# plt.xlabel("Voltage (V)")
# plt.ylabel("Pressure (Pa)")
# plt.title("Calibration")
# plt.grid()
# plt.legend()
# plt.show()
