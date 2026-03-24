import numpy as np
import pint
import matplotlib.pyplot as plt

ur = pint.UnitRegistry()

u_inf = 13 * ur("m/s")
nu = 1.5e-5 * ur("m^2/s")

x0 = 0.000001 * ur("m")
x1 = 65 * ur("in")

Re_crit = 5e5

x = np.linspace(x0.to("m").magnitude, x1.to("m").magnitude, 2**8) * ur("m")
x_tr = (Re_crit * nu / u_inf).to("m")

Re_x = (u_inf * x / nu).to_base_units().magnitude
Re_tr = (u_inf * x_tr / nu).to_base_units().magnitude

delta = np.zeros_like(x.magnitude)

x_with_lm = x <= x_tr
x_with_tr = x > x_tr

delta_tr = 5 * x_tr.magnitude / np.sqrt(Re_tr)

delta[x_with_lm] = 5 * x[x_with_lm].magnitude / np.sqrt(Re_x[x_with_lm])
delta[x_with_tr] = delta_tr + 0.37 * (
    x[x_with_tr].magnitude / (Re_x[x_with_tr] ** (1 / 5))
    - x_tr.magnitude / (Re_tr ** (1 / 5))
)

plt.figure()
plt.plot(x.to("in").magnitude, delta)
plt.xlabel("x [in]")
plt.ylabel("$\\delta$ [m]")
plt.title("Boundary Layer Thickness vs x")
plt.grid()

plt.savefig(f"out.png")
