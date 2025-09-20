# AERE 310 Homework 6

## Coefficients Plot

![](https://i.imgur.com/Lmg3ndS.png)

## Slope Estimations

$$
a_0 = 6.38908 \quad~~ \text{(airfoil slope)}
$$

$$
a = 4.993 \qquad \text{(3D wing slope)}
$$

As expected, due to the 3D relieving effect, the slope of the airfoil is greater than the slope of the 3D wing since particles have 1 less degree of freedom in 2D.

## Gammas Plot

![](https://i.imgur.com/8TIVrXE.png)

## Source Code

```py
# AERE 310 Homework 6

import math
import numpy as np
import os
import matplotlib.pyplot as plt
import concurrent.futures
from scipy.interpolate import interp1d
from tabulate import tabulate

# compute constants
N = 150  # segments
epsilon = 1e-8  # threshold
beta = 10**-2.5  # damping

# environment properties
V_infinity = 65

# wing properties
S = 17
AR = 8
lambda_ = 0.7
b = math.sqrt(S * AR)
c_r = 2 * S / (b * (1 + lambda_))
c_t = lambda_ * c_r

# coefficient plot domain
coefficients_plot_alpha_0_deg = -17
coefficients_plot_alpha_1_deg = 17
coefficients_plot_d_alpha_deg = 1
coefficients_plot_alphas_deg = np.arange(
    coefficients_plot_alpha_0_deg,
    coefficients_plot_alpha_1_deg + coefficients_plot_d_alpha_deg,
    coefficients_plot_d_alpha_deg,
)

# coefficient of lift linear sampling domain
slope_alpha_0_deg = -8
slope_alpha_1_deg = 8
slope_alpha_0 = slope_alpha_0_deg * math.pi / 180
slope_alpha_1 = slope_alpha_1_deg * math.pi / 180

# gamma plot domain
gamma_plot_alpha_0_deg = -20
gamma_plot_alpha_1_deg = 20
gamma_plot_d_alpha_deg = 5
gamma_plot_alphas_deg = np.arange(
    gamma_plot_alpha_0_deg,
    gamma_plot_alpha_1_deg + gamma_plot_d_alpha_deg,
    gamma_plot_d_alpha_deg,
)

# incidence angles at root and tip
i_r = 1.5 * math.pi / 180
i_t = -1.5 * math.pi / 180

delta_z = b / N

# my working directory isn't on the same level as this script
# i.e. just place airfoil.dat adjacent to this file
airfoil_deg = np.loadtxt(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "airfoil.dat")
)
airfoil = airfoil_deg.copy()
airfoil[:, 0] = np.deg2rad(airfoil[:, 0])

# converge_Gammas() sometimes samples just outside the domain requiring decent
# extrapolation
c_l = interp1d(airfoil[:, 0], airfoil[:, 1], fill_value="extrapolate", kind="cubic")

# cute little optimization i made; see cache_Gammas() for details
Gamma_cache = {}


# cord length interpolator
def c(z):
    x = abs(z) / (b / 2)
    return c_r * (1 - x) + c_t * x


# incidence angle interpolator
def incidence(z):
    x = abs(z) / (b / 2)
    return i_r * (1 - x) + i_t * x


# z as a function of index
def z(i):
    return -b / 2 + delta_z / 2 + (i - 1) * delta_z


# would've placed this constants up above with the others but python is a
# stupid language and won't let me do hoisting
c_l_z_0 = c_l(incidence(0))  # c_l of the incidence angle at z = 0
Gamma_0 = V_infinity * c_r / 2 * c_l_z_0


# the inexplicable D function that just shows up in the theory lol
def D(x):
    return 4 / (1 - 4 * x**2)


# induced alpha at index i
def alpha_i_i(Gammas, i):
    return (
        -1
        / (4 * math.pi * V_infinity * delta_z)
        * sum(Gammas[j - 1] * D(i - j) for j in range(1, N + 1))
    )


# i just love the word ephemeral; here, it means initial
def Gamma_ephemeral(i):
    return Gamma_0 * math.sqrt(1 - (z(i) / (b / 2)) ** 2)


# made this optimization which fixes a few issues
# 1. this distributes the work across all CPU cores so i don't have to watch
# paint dry (16x faster on my machine)
# 2. it removes the duplicates between the coefficient and gamma plots so not
# work is wasted
def cache_Gammas():
    alphas_deg = list(set([*coefficients_plot_alphas_deg, *gamma_plot_alphas_deg]))
    cpu = os.cpu_count()
    length = len(alphas_deg)

    print(f"🔵 Spawning {cpu} asynchronous compute threads for {length} Gammas...")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        Gammas_array = executor.map(converge_Gammas, alphas_deg)

    for alpha_deg, Gammas in zip(alphas_deg, Gammas_array):
        Gamma_cache[alpha_deg] = Gammas


# the main iterator, runs so god damn slow
def iterate(Gammas, alpha):
    Gammas_new = []

    for i in range(1, N + 1):
        z_i = -b / 2 + (i - 0.5) * delta_z
        alpha_eff_i = alpha + incidence(z_i) + alpha_i_i(Gammas, i)

        c_i = c(z_i)
        C_l_i = c_l(alpha_eff_i)

        Gamma_new_i = (V_infinity * c_i / 2) * C_l_i
        Gamma_old_i = Gammas[i - 1]
        Gamma = Gamma_old_i + beta * (Gamma_new_i - Gamma_old_i)

        Gammas_new.append(Gamma)

    return Gammas_new


# the main loop
def converge_Gammas(alpha_deg):
    print(f"🟡 Received request for alpha = {alpha_deg}°")

    alpha = alpha_deg * math.pi / 180
    Gammas = [Gamma_ephemeral(i) for i in range(1, N + 1)]
    converged = False
    I = 0

    while not converged:
        Gammas_new = iterate(Gammas, alpha)
        epsilon_i = (
            1
            / N
            * sum(
                ((Gammas_new[i - 1] - Gammas[i - 1]) / Gammas[i - 1]) ** 2
                for i in range(1, N + 1)
            )
        )

        converged = epsilon_i < epsilon
        Gammas = Gammas_new
        I += 1

    print(f"🟢 Converged alpha = {round(alpha * 180 / math.pi)}° in {I} iterations")

    return Gammas


# renders C_L, c_l, and C_D_i and also logs the slopes because i couldn't be
# bothered to abstract away the slope as its own function
def render_coefficients():
    C_Ls = []
    C_D_is = []

    for alpha_deg in coefficients_plot_alphas_deg:
        Gammas = Gamma_cache[alpha_deg]
        C_L = (
            2 * delta_z / (V_infinity * S) * sum(Gammas[i - 1] for i in range(1, N + 1))
        )
        C_D_i = (
            -2
            * delta_z
            / (V_infinity * S)
            * sum(
                Gammas[i - 1] * math.sin(alpha_i_i(Gammas, i)) for i in range(1, N + 1)
            )
        )
        C_Ls.append(C_L)
        C_D_is.append(C_D_i)

    c_l_0 = c_l(slope_alpha_0)
    c_l_1 = c_l(slope_alpha_1)
    C_L_0 = C_Ls[np.where(slope_alpha_0_deg == coefficients_plot_alphas_deg)[0][0]]
    C_L_1 = C_Ls[np.where(slope_alpha_1_deg == coefficients_plot_alphas_deg)[0][0]]

    a_0 = (c_l_1 - c_l_0) / (slope_alpha_1 - slope_alpha_0)
    a = (C_L_1 - C_L_0) / (slope_alpha_1 - slope_alpha_0)

    print(
        tabulate(
            [["a_0 (airfoil slope)", a_0], ["a (3D wing slope)", a]],
        )
    )

    _, ax1 = plt.subplots()

    ax1.plot(
        airfoil_deg[:, 0],
        airfoil_deg[:, 1],
        color="tab:cyan",
        label=r"$C_l$",
    )
    ax1.legend(loc="upper left")

    ax2 = ax1.twinx()
    ax2.plot(coefficients_plot_alphas_deg, C_D_is, color="tab:red", label=r"$C_{D_i}$")
    ax2.set_ylabel(r"$C_{D_i}$", color="tab:red")
    ax2.tick_params(axis="y", labelcolor="tab:red")
    ax2.legend(loc="lower right")

    ax1.plot(coefficients_plot_alphas_deg, C_Ls, color="tab:blue", label=r"$C_L$")
    ax1.set_xlabel(r"$\alpha$ (degrees)")
    ax1.set_ylabel(r"$C_L$", color="tab:blue")
    ax1.tick_params(axis="y", labelcolor="tab:blue")
    ax1.legend(loc="upper left")

    ax1.grid()
    plt.title(r"$C_L$ and $C_{D_i}$ vs $\alpha$")
    plt.show(block=False)


# renders the Gammas
def render_Gammas():
    zs = [z(i) for i in range(1, N + 1)]

    _, ax = plt.subplots()

    for alpha_deg in gamma_plot_alphas_deg:
        Gammas = Gamma_cache[alpha_deg] / Gamma_0
        ax.plot(zs, Gammas, label=f"{alpha_deg}°")

    plt.grid()
    plt.title(r"$\Gamma$ vs z")
    plt.xlabel("z (m)")
    plt.ylabel(r"$\Gamma / \Gamma_0$")
    plt.show()


# implicit
def main():
    cache_Gammas()
    render_coefficients()
    render_Gammas()


# worker thread weeps if i don't differentiate between them and main
if __name__ == "__main__":
    main()
```

## Output

```
🔵 Spawning 16 asynchronous compute threads for 37 Gammas...
🟡 Received request for alpha = 0°
🟡 Received request for alpha = 1°
🟡 Received request for alpha = 2°
🟡 Received request for alpha = 3°
🟡 Received request for alpha = 4°
🟡 Received request for alpha = 5°
🟡 Received request for alpha = 6°
🟡 Received request for alpha = 7°
🟡 Received request for alpha = 8°
🟡 Received request for alpha = 9°
🟡 Received request for alpha = 10°
🟡 Received request for alpha = 11°
🟡 Received request for alpha = 12°
🟡 Received request for alpha = 13°
🟡 Received request for alpha = 14°
🟡 Received request for alpha = 15°
🟢 Converged alpha = 2° in 316 iterations
🟡 Received request for alpha = 16°
🟢 Converged alpha = 3° in 583 iterations
🟡 Received request for alpha = 17°
🟢 Converged alpha = 1° in 706 iterations
🟡 Received request for alpha = 20°
🟢 Converged alpha = 4° in 675 iterations
🟡 Received request for alpha = -20°
🟢 Converged alpha = 5° in 757 iterations
🟡 Received request for alpha = -17°
🟢 Converged alpha = 6° in 807 iterations
🟡 Received request for alpha = -16°
🟢 Converged alpha = 7° in 813 iterations
🟡 Received request for alpha = -15°
🟢 Converged alpha = 9° in 848 iterations
🟡 Received request for alpha = -14°
🟢 Converged alpha = 10° in 859 iterations
🟡 Received request for alpha = -13°
🟢 Converged alpha = 8° in 824 iterations
🟡 Received request for alpha = -12°
🟢 Converged alpha = 11° in 867 iterations
🟡 Received request for alpha = -11°
🟢 Converged alpha = 13° in 884 iterations
🟡 Received request for alpha = -10°
🟢 Converged alpha = 14° in 896 iterations
🟡 Received request for alpha = -9°
🟢 Converged alpha = 12° in 878 iterations
🟡 Received request for alpha = -8°
🟢 Converged alpha = 15° in 911 iterations
🟡 Received request for alpha = -7°
🟢 Converged alpha = 0° in 1069 iterations
🟡 Received request for alpha = -6°
🟢 Converged alpha = 16° in 923 iterations
🟡 Received request for alpha = -5°
🟢 Converged alpha = 17° in 951 iterations
🟡 Received request for alpha = -4°
🟢 Converged alpha = 20° in 1026 iterations
🟡 Received request for alpha = -3°
🟢 Converged alpha = -20° in 1064 iterations
🟡 Received request for alpha = -2°
🟢 Converged alpha = -17° in 1084 iterations
🟡 Received request for alpha = -1°
🟢 Converged alpha = -16° in 1026 iterations
🟢 Converged alpha = -15° in 1022 iterations
🟢 Converged alpha = -11° in 1007 iterations
🟢 Converged alpha = -13° in 1028 iterations
🟢 Converged alpha = -12° in 1008 iterations
🟢 Converged alpha = -14° in 1039 iterations
🟢 Converged alpha = -10° in 1029 iterations
🟢 Converged alpha = -9° in 1059 iterations
🟢 Converged alpha = -8° in 1065 iterations
🟢 Converged alpha = -7° in 1049 iterations
🟢 Converged alpha = -6° in 1068 iterations
🟢 Converged alpha = -5° in 1136 iterations
🟢 Converged alpha = -4° in 1183 iterations
🟢 Converged alpha = -3° in 1221 iterations
🟢 Converged alpha = -1° in 1795 iterations
🟢 Converged alpha = -2° in 1990 iterations
-------------------  -------
a_0 (airfoil slope)  6.38908
a (3D wing slope)    4.993
-------------------  -------
```
