import numpy as np

k_1 = 20
k_2 = 20
k_3 = 20
k_4 = 20

free = [1, 2, 3]

F = np.matrix(
    [
        [0],
        [0],
        [5],
        [0],
        [0],
    ]
)

base = np.matrix(
    [
        [1, -1],
        [-1, 1],
    ]
)

K_1 = k_1 * base
K_2 = k_2 * base
K_3 = k_3 * base

K_1 = np.pad(
    K_1,
    pad_width=(
        (0, 2),
        (0, 2),
    ),
)
K_2 = np.pad(
    K_2,
    pad_width=(
        (1, 1),
        (1, 1),
    ),
)
K_3 = np.pad(
    K_3,
    pad_width=(
        (2, 0),
        (2, 0),
    ),
)

S = K_1 + K_2 + K_3
S = S[np.ix_(free, free)]

F = F[np.ix_(free)]
U = np.linalg.solve(S, F)

print(U)
