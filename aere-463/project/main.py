import math
import numpy as np

w = 3  # m
h = 3  # m

Delta = 1  # m

rho = 7850  # kg/m^3

t_e = 250 / 1000  # m

N = int(w / Delta)
M = int(h / Delta)

print(f"(N, M) = ({N}, {M})\n")

n_v = (N + 1) * (M + 1)
n_t = 2 * N * M

Vs = [np.zeros((n_v, 1))]
Ts = [np.full((n_t, 1), t_e)]


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


print(f(Vs[-1], Ts[-1]))
