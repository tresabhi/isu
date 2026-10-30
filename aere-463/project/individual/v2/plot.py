import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import cm, colors
import config


def plot_mesh(v, t, show_walls=True, z_exaggeration=1.0, v_decimals=4, t_decimals=4):
    # round for display only; v to 0.1 mm, t to 0.1 mm
    v = np.round(v, v_decimals)
    t = np.round(t, t_decimals)

    N, M, D = config.N, config.M, config.Delta

    def p(ix, iy):
        return (ix * D, iy * D, v[ix, iy])

    tris, vals = [], []
    for iy in range(M):
        for ix in range(N):
            # j = 0: bottom left, bottom right, top left
            tris.append([p(ix, iy), p(ix + 1, iy), p(ix, iy + 1)])
            vals.append(t[ix, iy, 0])
            # j = 1: top right, bottom right, top left
            tris.append([p(ix + 1, iy + 1), p(ix + 1, iy), p(ix, iy + 1)])
            vals.append(t[ix, iy, 1])

    # fixed scale: 0 thickness = green, t_effective (or more) = red
    norm = colors.Normalize(vmin=np.min(vals), vmax=config.t_effective, clip=True)
    cmap = cm.RdYlGn_r  # green -> yellow -> red

    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(111, projection="3d")

    ax.add_collection3d(
        Poly3DCollection(
            tris,
            facecolors=cmap(norm(vals)),
            edgecolors="k",
            linewidths=0.8,
            alpha=0.95,
        )
    )

    if show_walls:
        walls = []
        for ix in range(N):  # bottom (iy = 0) and top (iy = M)
            for iy in (0, M):
                a, b = p(ix, iy), p(ix + 1, iy)
                walls.append([(a[0], a[1], 0), (b[0], b[1], 0), b, a])
        for iy in range(M):  # left (ix = 0) and right (ix = N)
            for ix in (0, N):
                a, b = p(ix, iy), p(ix, iy + 1)
                walls.append([(a[0], a[1], 0), (b[0], b[1], 0), b, a])
        ax.add_collection3d(
            Poly3DCollection(
                walls, facecolors="lightgray", edgecolors="gray", alpha=0.35
            )
        )

    z_max = max(v.max(), 1e-3) * 1.1
    ax.set_xlim(0, N * D)
    ax.set_ylim(0, M * D)
    ax.set_zlim(0, z_max)
    ax.set_box_aspect((N * D, M * D, z_max * z_exaggeration))
    ax.set_xlabel("x [m]")
    ax.set_ylabel("y [m]")
    ax.set_zlabel("v [m]")
    ax.view_init(elev=25, azim=-60)

    fig.colorbar(
        cm.ScalarMappable(norm=norm, cmap=cmap),
        ax=ax,
        shrink=0.6,
        label="t [m]",
    )
    plt.show()
