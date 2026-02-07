import numpy as np

k_1 = k_2 = k_3 = 1000
K_1 = K_2 = K_3 = k_1 * np.matrix(
    [
        [1, -1],
        [-1, 1],
    ]
)

print(K_1, end="\n\n")
print(K_2, end="\n\n")
print(K_3, end="\n\n")

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

print(K_1, end="\n\n")
print(K_2, end="\n\n")
print(K_3, end="\n\n")

S = K_1 + K_2 + K_3

print(S, end="\n\n")

free = [1, 2, 3]
S = S[np.ix_(free, free)]

print(S, end="\n\n")

F = np.matrix(
    [
        [0],
        [-1000],
        [0],
        [4000],
    ]
)[np.ix_(free)]

print(F, end="\n\n")

U = np.linalg.solve(S, F)

print(U)
