import pyvista as pv
import torch
import numpy as np
import math

N, d = 100, 3
N = round((1 / d) * math.floor((N * d) ** (1 / d)) ** d)
M = torch.abs(torch.randn(N * d, 1, device="cuda"))
L = round((N * d) ** (1 / d))

M_L = M.cpu().reshape([L] * d).numpy()

x = y = z = np.arange(L)
X, Y, Z = np.meshgrid(x, y, z, indexing="ij")
grid = pv.StructuredGrid(X, Y, Z)

grid["density"] = M_L.flatten(order="F")

plotter = pv.Plotter()
plotter.add_volume(grid, scalars="density", opacity="sigmoid", cmap="viridis")
plotter.show()
