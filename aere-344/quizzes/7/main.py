import re
from matplotlib import pyplot as plt

c = 24

with open("data.dat") as file:
    lines = file.readlines()
    zones = [
        lines[9:40],
        lines[41:70],
        lines[71:99],
    ]
    zone_index = 0

    for zone in zones:
        C_D = 0
        zone = [
            [float(x) for x in re.sub(r"\s+", " ", line.strip()).split(" ")]
            for line in zone
        ]
        index = 0

        xs = []
        ys = []

        for columns in zone:
            columns_prev = zone[0 if index == 0 else index - 1]

            [_, y, u, _, uu, _, _] = columns
            [_, y_prev, _, _, _, _, _] = columns_prev

            delta_y_i = y - y_prev
            C_D += u * (1 - u) * delta_y_i

            xs.append(uu)
            ys.append(y / c)

            index += 1

        C_D *= 2 / c
        zone_index += 1

        print(f"C_D_{zone_index} = {C_D:.5g}")

        plt.figure()
        plt.title(f"Zone {zone_index}")

        plt.plot(xs, ys)

        plt.savefig(f"out/zone_{zone_index}.png")
