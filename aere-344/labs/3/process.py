import csv

CALIBRATION_POINTS = 5

for index in range(CALIBRATION_POINTS):
    name = index + 1

    voltages = []
    pressures = []

    with open(f"data/calibration/{name}.txt") as file:
        lines = file.readlines()[5:]

        for line in lines:
            magnitude = float(line[-12:-4])
            power = float(line[-2])
            voltage = magnitude * 10**power

            voltages.append(voltage)

    with open(f"data/calibration/{name}.csv") as file:
        reader = csv.reader(file)

        for row in reader:
            pressure = float(row[2])
            pressures.append(pressure)

    pressure = sum(pressures) / len(pressures)
    voltage = sum(voltages) / len(voltages)

    print(voltage, pressure)
