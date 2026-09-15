import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import math
import numpy as np
import time

w = 3  # m
h = 3  # m

Delta = 0.1  # m

rho = 7850  # kg/m^3

t_e = 250 / 1000  # m

N = int(w / Delta)
M = int(h / Delta)

print(f"(N, M) = ({N}, {M})\n")

n_v = (N + 1) * (M + 1)
n_t = 2 * N * M

Vs = [np.zeros((n_v, 1))]
Ts = [np.random.uniform(t_e, 2 * t_e, size=(n_t, 1))]


def f(X, T):
    m = 0

    # i_tri is the index of the triangle
    for i_tri in range(n_t):
        is_bottom_left = i_tri % 2 == 0

        # i_quad is the index of the quad formed by 2 triangles
        i_quad = i_tri // 2
        # i_bottom_left_vertex is the index of the bottom left vertex of the
        # quad or the bottom left vertex of the bottom left triangle
        i_bottom_left_vertex = i_quad % N + (i_quad // N) * (N + 1)

        if is_bottom_left:
            # i0 is the 90deg corner and everything the other vertices are
            # picked in a counter-clockwise fashion
            i0 = i_bottom_left_vertex
            i1 = i0 + 1
            i2 = i0 + N + 1
        else:
            # the same applies here
            i0 = i_bottom_left_vertex + N + 2
            i1 = i0 - 1
            i2 = i_bottom_left_vertex + 1

        [v0] = X[i0]
        [v1] = X[i1]
        [v2] = X[i2]
        [t] = T[i_tri]

        n_i_abs = Delta * math.sqrt((v0 - v1) ** 2 + (v0 - v2) ** 2 + Delta**2)
        A_i = n_i_abs / 2

        V_i = A_i * t
        m_i = rho * V_i

        m += m_i

    return m


def visualize(V, T):
    t0 = time.time()

    x = np.linspace(0, w, N + 1)
    y = np.linspace(0, h, M + 1)
    grid_x, grid_y = np.meshgrid(x, y)

    z = V.flatten()

    vertices_3d = np.column_stack((grid_x.ravel(), z, grid_y.ravel()))

    triangles_3d = []
    for i_tri in range(n_t):
        is_bottom_left = i_tri % 2 == 0
        i_quad = i_tri // 2
        i_bottom_left_vertex = i_quad % N + (i_quad // N) * (N + 1)

        if is_bottom_left:
            i0 = i_bottom_left_vertex
            i1 = i0 + 1
            i2 = i0 + N + 1
        else:
            i0 = i_bottom_left_vertex + N + 2
            i1 = i0 - 1
            i2 = i_bottom_left_vertex + 1

        triangles_3d.append(vertices_3d[[i0, i1, i2]])

    thicknesses = T.flatten()

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")

    collection = Poly3DCollection(
        triangles_3d, cmap="RdYlGn_r", edgecolors="none", alpha=1.0, shade=False
    )
    collection.set_array(thicknesses)

    ax.add_collection3d(collection)
    ax.set_xlim(0, w)

    z_min, z_max = np.min(z), np.max(z)
    if z_min == z_max:
        ax.set_ylim(z_min - 0.1, z_max + 0.1)
    else:
        ax.set_ylim(z_min, z_max)

    ax.set_zlim(0, h)

    ax.set_xlabel("x [m]")
    ax.set_ylabel("v [mm]")
    ax.set_zlabel("y [m]")
    ax.set_title("3D Armor Surface & Thickness Distribution")

    cbar = fig.colorbar(collection, ax=ax, pad=0.1)
    cbar.set_label("Armor Thickness (mm)")

    # Adjust view angle to bring Z-offset out toward viewer
    ax.view_init(elev=20, azim=-60)

    plt.tight_layout()

    print(time.time() - t0)

    plt.show()


visualize(Vs[-1], Ts[-1])

def add(a, b):
    return a + b