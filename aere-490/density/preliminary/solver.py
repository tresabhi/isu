import numpy as np
import math
import random
import tabulate

G = 6.674e-11

d = 3
n = 100
mu = d * n

L = 100


def m_v(r: np.array):
    return r[0] + 1


class TrueVoxel:
    def __init__(self, r: np.array, m: float):
        self.r = r
        self.m = m

    def __str__(self):
        return f"{m}@{r}"


true_voxels: list[TrueVoxel] = []


def r_v(i: int):
    x = L * i / mu
    y = 0
    z = 0

    return np.array([x, y, z])


for i in range(mu):
    r = r_v(i)
    m = m_v(r)

    true_voxel = TrueVoxel(r, m)
    true_voxels.append(true_voxel)


def a(r: np.array):
    a = np.array([0.0, 0.0, 0.0])

    for true_voxel in true_voxels:
        dr = true_voxel.r - r
        a += (G * true_voxel.m * dr) / np.linalg.norm(dr) ** 3

    return a


A = []
R = []


for i in range(n):
    x = i + random.random() - 2
    y = random.random() - 2
    z = random.random() + 1
    a_ = a(np.array([x, y, z]))
    r = np.array([x, y, z])

    A.append([a_[0]])
    A.append([a_[1]])
    A.append([a_[2]])

    x_row = []
    y_row = []
    z_row = []

    for j in range(mu):
        r_v_ = r_v(j)
        dr = r_v_ - r
        dir = dr / (np.linalg.norm(dr) ** 3)

        x_row.append(dir[0])
        y_row.append(dir[1])
        z_row.append(dir[2])

    R.append(x_row)
    R.append(y_row)
    R.append(z_row)


A = np.matrix(A)
R = np.matrix(R)
M = (np.linalg.pinv(R) @ A) / G
M = np.asarray(M)

table = []

for i, true_voxel in enumerate(true_voxels):
    true_val = true_voxel.m
    rec_val = M[i][0]
    error = f"{round(100 * abs(true_val - rec_val) / true_val)}%"

    table.append([i, true_val, rec_val, error])

print(tabulate.tabulate(table))
