import numpy as np
import pyvista as pv
import torch
import math
import random


N = 100_000  # sample count
d = 3  # dimension of the universe
l = math.floor((N * d) ** (1 / d))  # max side length of a perfect cube
N = round(
    (1 / d) * l**d
)  # sample count adjusted to fit a perfect cube in the dimensioned universe


r_asteroid = 30  # radius of the random asteroid
M_true = torch.zeros(*[l] * d, device="cuda")  # empty asteroid density tensor

for i in range(l):
    x = i - (l - 1) / 2

    for j in range(l):
        y = j - (l - 1) / 2

        for k in range(l):
            z = k - (l - 1) / 2
            r = math.sqrt(x**2 + y**2 + z**2)

            if r < r_asteroid:
                # a good test bench distribution
                M_true[i][j][k] = (1 - r / r_asteroid) * random.uniform(0.5, 1.5)

x = y = z = np.arange(l)
X, Y, Z = np.meshgrid(x, y, z, indexing="ij")
grid = pv.StructuredGrid(X, Y, Z)

grid["density"] = M_true.cpu().flatten()
clipped = grid.clip(normal="x", origin=grid.center)

plotter = pv.Plotter()
plotter.add_volume(clipped, opacity="foreground", cmap="copper_r")
plotter.show()
