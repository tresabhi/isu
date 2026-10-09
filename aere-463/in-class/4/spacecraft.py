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
