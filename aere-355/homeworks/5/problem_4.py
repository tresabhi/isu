import pint
import numpy as np

ur = pint.UnitRegistry()

g = 9.81 * ur.m / ur.s**2
a = 1116.45 * ur.ft / ur.s
rho = 2.3769e-3 * ur.slug / ur.ft**3

I_y = 126099 * ur.slug * ur.ft**2
W = 23904 * ur.lbf
Mach = 0.20
c_bar = 10.93 * ur.ft
S = 542.5 * ur.ft**2

C_L_0 = 0.737
C_L_alpha = 5.0
C_D_0 = 0.095
C_L_u = 0
C_D_alpha = 0.75
C_D_u = 0
C_m_alpha = -0.80
C_m_alpha_dot = -3.0

m = W / g
u_0 = Mach * a
Q = (1 / 2) * rho * u_0**2

M_u = 0
X_u = -(C_D_u + 2 * C_D_0) * Q * S / (m * u_0)
Z_u = -(C_L_u + 2 * C_L_0) * Q * S / (m * u_0)
X_w = -(C_D_alpha - C_L_0) * Q * S / (m * u_0)
Z_w = -(C_L_alpha + C_D_0) * Q * S / (m * u_0)

M_w = C_m_alpha * Q * S * c_bar / (u_0 * I_y)
M_w_dot = C_m_alpha_dot * (c_bar / (2 * u_0)) * Q * S * c_bar / (u_0 * I_y)
M_q = C_m_q * (c_bar / (2 * u_0)) * Q * S * c_bar / I_y

A = np.matrix(
    [
        [X_u, X_w, 0, -g],
        [Z_u, Z_w, u_0, 0],
        [M_u + M_w_dot * Z_u, M_w + M_w_dot * Z_w, M_w_dot * u_0 + M_q, 0],
        [0, 0, 1, 0],
    ]
)
B = np.matrix(
    [
        [X_delta_e, X_delta_T],
        [Z_delta_e, Z_delta_T],
        [M_delta_e + M_w_dot * Z_delta_e, M_delta_T + M_w_dot * Z_delta_T],
        [0, 0],
    ]
)
