# AERE 261 HW 7

import math
import sys
from matplotlib import pyplot as plt
import numpy as np

# given constants
C_D_0 = 0.017
K = 0.056
C_L_max = 1.37
S_wing = 22.9  # m^2
eta_pr = 0.9
W_0 = 16481  # N
P = 18e4  # W

# https://www.digitaldutch.com/atmoscalc/graphs.htm
# It would be childish to hardcode this in a function so I am making this
# data-driven.
# (m, K)[]
T_table = [
    (0.0, 288.15),
    (11e3, 216.65),
    (20e3, 216.65),
    (32e3, 228.65),
    (47e3, 270.65),
    (51e3, 270.65),
    (72e3, 212.65),
    (85e3, 186.95),
    (86e3, 186.95),
]


# m -> K
def temperature(h: int):
    # iterate through the table...
    for index in range(len(T_table) - 1):
        # ...to find an appropriate entry
        if h >= T_table[index][0] and h < T_table[index + 1][0]:
            # interpolate
            return T_table[index][1] + (
                (T_table[index + 1][1] - T_table[index][1])
                * (h - T_table[index][0])
                / (T_table[index + 1][0] - T_table[index][0])
            )

    # if the for loop never returns, the altitude is outside of our domain
    raise ValueError(f"Invalid altitude: {h}")


# https://en.wikipedia.org/wiki/Atmospheric_pressure
p_0 = 101325  # Pa
M = 0.0289644  # kg/mol
g = 9.80665  # m/s^2
R = 8.3144598  # J/(mol*K)
L = 0.00976  # K/m
T_0 = temperature(0)


# m -> Pa
def pressure(h: int):
    # applying the barometric formula
    return p_0 * (1 - (L * h) / T_0) ** ((g * M) / (R * L))


# m -> kg/m^3
def density(h: int):
    # applying the ideal gas law
    return (pressure(h) * M) / (R * temperature(h))


# m -> m/s
def v_stall(h: int):
    # applying the v_stall formula
    return math.sqrt((2 * W_0) / (density(h) * S_wing * C_L_max))


# m -> m/s
def v_r_c_max(h: int):
    # applying the v_r_c_max formula
    return math.sqrt((2 / density(h)) * (W_0 / S_wing) * math.sqrt(K / (3 * C_D_0)))


# scuffed way to write max C_L^3/2 over C_D
C_L_3_2_C_D_max = (1 / 4) * (3 / (K * (C_D_0) ** (1 / 3))) ** (3 / 4)


# m -> W
def p_r(h: int):
    return math.sqrt(2 / (density(h) * S_wing)) * ((W_0 ** (3 / 2)) / C_L_3_2_C_D_max)


# m -> W
def p_a(h: int):
    return P * (pressure(h) / p_0)


# m -> W
def p_e(h: int):
    return p_a(h) - p_r(h)


C_L_C_D_max = math.sqrt(1 / (4 * K * C_D_0))


# m -> m/s
def r_c_max(h: int):
    return eta_pr * P / W_0 - math.sqrt(
        (2 / density(h)) * math.sqrt(K / (3 * C_D_0)) * (W_0 / S_wing)
    ) * (1.155 / C_L_C_D_max)


h_0 = 0  # m
h_1 = 25e3  # m
delta_h = 1  # m

# range of heights
x = np.arange(h_0, h_1, delta_h)

# turning this file into a mono-file CLI
if len(sys.argv) < 2:
    # gotta pass an argument or get wrecked lol
    raise ValueError(
        "No instruction provided on what to plot.\nHint: py index.py --plot=<temperature|pressure|density>"
    )

# catching all plot types
if sys.argv[1] == "--plot=temperature":
    plt.plot([temperature(h) for h in x], x)
    plt.xlabel("Temperature (K)")
    plt.title("Temperature vs. Height")
elif sys.argv[1] == "--plot=pressure":
    plt.plot([pressure(h) for h in x], x)
    plt.xlabel("Pressure (Pa)")
    plt.title("Pressure vs. Height")
elif sys.argv[1] == "--plot=density":
    plt.plot([density(h) for h in x], x)
    plt.xlabel("Density (kg/m^3)")
    plt.title("Density vs. Height")
elif sys.argv[1] == "--plot=v_stall":
    plt.plot([v_stall(h) for h in x], x)
    plt.xlabel("Velocity (m/s)")
    plt.title("Stall Velocity vs. Height")
elif sys.argv[1] == "--plot=v_r_c_max":
    plt.plot([v_r_c_max(h) for h in x], x, label="Max Rate of Climb")
    plt.plot([v_stall(h) for h in x], x, label="Stall Velocity")
    plt.legend()
    plt.xlabel("Velocity (m/s)")
    plt.title("Max Rate of Climb vs. Height")
elif sys.argv[1] == "--plot=p_r":
    plt.plot([p_r(h) / 1000 for h in x], x)
    plt.xlabel("Power Required (kW)")
    plt.title("Power Required vs. Height")
elif sys.argv[1] == "--plot=p_a":
    plt.plot([p_a(h) / 1000 for h in x], x, label="Power Available")
    plt.plot([p_r(h) / 1000 for h in x], x, label="Power Required")
    plt.legend()
    plt.xlabel("Power Available (kW)")
    plt.title("Power Available vs. Height")
elif sys.argv[1] == "--plot=p_e":
    plt.plot([p_e(h) / 1000 for h in x], x, label="Power Excess")
    plt.plot([p_a(h) / 1000 for h in x], x, label="Power Available")
    plt.plot([p_r(h) / 1000 for h in x], x, label="Power Required")
    plt.xlim(0)
    plt.legend()
    plt.xlabel("Power Excess (kW)")
    plt.title("Power Excess vs. Height")
elif sys.argv[1] == "--plot=r_c_max":
    plt.plot([r_c_max(h) for h in x], x)
    plt.xlim(0)
    plt.xlabel("Rate of Climb Max (m/s)")
    plt.title("Rate of Climb Max vs. Height")
elif sys.argv[1] == "--plot=ceilings":
    # 100ft/min = 0.508m/s

    plt.plot([r_c_max(h) for h in x], x, label="Rate of Climb Max")
    plt.plot([0.508 for _ in x], x, label="Service Ceiling")
    plt.plot([0 for _ in x], x, label="Absolute Ceiling")
    plt.xlim(-1)
    plt.legend()
    plt.xlabel("Rate of Climb Max (m/s)")
    plt.title("Rate of Climb Max vs. Height")
# catching invalid plot types
else:
    raise ValueError(
        "Illegal plot argument. Run the command without arguments to see all plots types."
    )


# time for matplotlib to shine
plt.ylabel("Height (m)")
plt.grid()
plt.show()
