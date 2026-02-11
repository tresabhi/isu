import csv

CALIBRATION_POINTS = 5

for index in range(CALIBRATION_POINTS):
    name = index + 1
    pressures = []

    with open(f"data/calibration/{name}.csv", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            pressures.append(float(row[2]))

    pressure = sum(pressures) / len(pressures)
    print(pressure)
