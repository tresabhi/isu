from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt


def dynamic_eqn(t, y):
    [theta, r, v_theta, v_r] = y

    dy_dt = np.zeros(4)

    dy_dt[0] = v_theta / r
    dy_dt[1] = v_r
    dy_dt[2] = -v_r * v_theta / r
    dy_dt[3] = v_theta**2 / r - 1 / r / r

    return dy_dt


theta_0 = 0
r_0 = 1
v_theta_0 = 1
v_r_0 = 0

y_0 = [theta_0, r_0, v_theta_0, v_r_0]
t_span = [0, 3]

solution = solve_ivp(dynamic_eqn, t_span, y_0, max_step=0.1)

theta = solution.y[0]
r = solution.y[1]

fig, ax = plt.subplots(subplot_kw={"projection": "polar"})

ax.plot(theta, r)
plt.plot(theta_0, r_0, "bo")

ax.set_rmax(3)

plt.show()
