import numpy as np
import math

psi = np.deg2rad(-20)
theta = np.deg2rad(7)
phi = np.deg2rad(0)

C_psi = math.cos(psi)
C_theta = math.cos(theta)
C_phi = math.cos(phi)

S_psi = math.sin(psi)
S_theta = math.sin(theta)
S_phi = math.sin(phi)

R = np.matrix(
    [
        [
            C_theta * C_psi,
            S_phi * S_theta * C_psi - C_phi * S_psi,
            C_phi * S_theta * C_psi + S_phi * S_psi,
        ],
        [
            C_theta * S_psi,
            S_phi * S_theta * S_psi + C_phi * C_psi,
            C_phi * S_theta * S_psi - S_phi * C_psi,
        ],
        [-S_theta, S_phi * C_theta, C_phi * C_theta],
    ]
)

V = np.matrix(
    [
        [267.987],
        [40],
        [32.905],
    ]
)

W_f = np.matrix(
    [
        [-40 * math.sqrt(2)],
        [-40 * math.sqrt(2)],
        [0],
    ]
)

W_i = R**-1 * W_f

V_prime = V + W_i

V_f_prime = R * V_prime

print(V_f_prime)
