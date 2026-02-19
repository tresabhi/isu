import math

cd = 0

with open("data.csv") as file:
    lines = file.readlines()[1:]

    for line in lines:
        trimmed = line[0:-1]
        [angle, cp] = trimmed.split(",")

        angle = float(angle) * (math.pi / 180)
        cp = float(cp)

        cd += 2 * cp * math.cos(angle)

dTheta = 5 * (math.pi / 180)
cd *= dTheta / 2

print(f"cd = {cd}")
