import numpy as np
import math
import matplotlib.pyplot as plt


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

    alpha_cl, cl_vals = np.array(cls).T
    alpha_cd, cd_vals = np.array(cds).T

    cl_sort_idx = np.argsort(alpha_cl)
    cd_sort_idx = np.argsort(alpha_cd)

    alpha_cl = alpha_cl[cl_sort_idx]
    cl_vals = cl_vals[cl_sort_idx]

    alpha_cd = alpha_cd[cd_sort_idx]
    cd_vals = cd_vals[cd_sort_idx]

    alpha_min = max(alpha_cl.min(), alpha_cd.min())
    alpha_max = min(alpha_cl.max(), alpha_cd.max())

    if alpha_min >= alpha_max:
        raise ValueError("No overlapping alpha range")

    mask = (alpha_cl >= alpha_min) & (alpha_cl <= alpha_max)
    alpha_common = alpha_cl[mask]
    cl_common = cl_vals[mask]

    cd_interpolated = np.interp(alpha_common, alpha_cd, cd_vals)

    valid = cd_interpolated > 1e-8
    alpha_common = alpha_common[valid]
    cl_common = cl_common[valid]
    cd_interpolated = cd_interpolated[valid]

    ld_ratio = cl_common / cd_interpolated

    stall_idx = np.argmax(cl_vals)
    stall_alpha = alpha_cl[stall_idx]

    print(f"{name} stall angle of attack = {stall_alpha} deg")

    best_idx = np.argmax(ld_ratio)
    best_alpha = alpha_common[best_idx]
    best_ld = ld_ratio[best_idx]

    print(f"{name} max L/D = {best_ld:.2f} at {best_alpha} deg")

    plt.plot(alpha_common, ld_ratio, label="L/D")
    plt.scatter(best_alpha, best_ld, label="max L/D")
    plt.xlabel("Alpha (deg)")
    plt.ylabel("L/D")
    # plt.title(name)
    plt.legend()
    plt.grid()


quiz("clean")
quiz("rime")
quiz("glaze")

plt.show()
