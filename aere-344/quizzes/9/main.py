import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

nu = 1.5233e-5


def power_law(x, a):
    return a * np.sqrt(x)


def work(lines: list[str], u_inf: float):
    xs = []
    us = []
    deltas = []

    for line in lines:
        columns = [float(number) for number in line.strip().split(",")]
        x, u = columns

        Re_x = (u_inf * x) / nu
        delta = (0.37 * x) / (Re_x ** (1 / 5))

        xs.append(x)
        us.append(u)
        deltas.append(delta)

    xs = np.array(xs)
    us = np.array(us)
    deltas = np.array(deltas)

    params, _ = curve_fit(power_law, xs, us)
    [a] = params

    delta = ((0.99 / a) * u_inf) ** (1 / 2)

    print(f"delta for u_inf={u_inf} is {delta}m")

    plt.figure()
    plt.title(f"{u_inf}m/s: u vs x")
    plt.xlabel("u")
    plt.ylabel("x")
    plt.plot(xs, us)
    plt.savefig(f"{u_inf}_v.png")


with open("data.csv") as file:
    lines = file.readlines()

    work(lines[1:59], 12.07)
    work(lines[61:], 25.00)
