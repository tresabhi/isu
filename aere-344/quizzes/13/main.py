import math


def parse(path):
    data = []

    with open(path) as file:
        lines = file.readlines()

    for line in lines:
        cells = line.strip().split("\t")
        cells = [float(cell) for cell in cells]

        data.append(cells)

    return data


def quiz(name):
    cls = parse(f"data/{name}cl.dat")
    cds = parse(f"data/{name}cd.dat")

    stall_cl = -math.inf
    stall_alpha = 0

    for i in range(len(cls)):
        alpha, cl = cls[i]

        if cl > stall_cl:
            stall_cl = cl
            stall_alpha = alpha

    print(f"{name} stall angle of attack = {stall_alpha} deg")


quiz("clean")
quiz("rime")
quiz("glaze")
