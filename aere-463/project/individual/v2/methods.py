import config
import math
import numpy as np


def plate_mass(v, t):
    m = 0

    for y in range(config.M):
        for x in range(config.N):
            v1 = v[x + 1, y]  # bottom right
            v2 = v[x, y + 1]  # top left

            for j in range(2):
                if j == 0:
                    # bottom left corner
                    v0 = v[x, y]
                else:
                    # top right corner
                    v0 = v[x + 1, y + 1]

                abs_n_i = config.Delta * math.sqrt(
                    (v0 - v1) ** 2 + (v0 - v2) ** 2 + config.Delta**2
                )
                A_i = abs_n_i / 2

                t_i = t[x, y, j]

                m += config.rho * A_i * t_i

    return m


def wall_segment_mass(v0, v1):
    return 0.5 * config.t_wall * config.rho * (v0 + v1) * config.Delta


def wall_mass(v):
    m = 0

    # bottom wall
    for x in range(config.N):
        m += wall_segment_mass(v[x, 0], v[x + 1, 0])

    # top wall
    for x in range(config.N):
        m += wall_segment_mass(v[x, config.M], v[x + 1, config.M])

    # left wall
    for y in range(config.M):
        m += wall_segment_mass(v[0, y], v[0, y + 1])

    # right wall
    for y in range(config.M):
        m += wall_segment_mass(v[config.N, y], v[config.N, y + 1])

    return m


def effective_thickness(v, t):
    t_prime = np.zeros((config.N, config.M, 2))

    for y in range(config.M):
        for x in range(config.N):
            v1 = v[x + 1, y]  # bottom right
            v2 = v[x, y + 1]  # top left

            for j in range(2):
                if j == 0:
                    # bottom left corner
                    v0 = v[x, y]
                else:
                    # top right corner
                    v0 = v[x + 1, y + 1]

                abs_n_i = config.Delta * math.sqrt(
                    (v0 - v1) ** 2 + (v0 - v2) ** 2 + config.Delta**2
                )

                cos_theta_i = (config.Delta**2) / abs_n_i

                t_prime[x, y, j] = t[x, y, j] / cos_theta_i

    return t_prime


def concavity(v):
    d_xx = v[2:, 1:-1] - 2 * v[1:-1, 1:-1] + v[:-2, 1:-1]
    d_yy = v[1:-1, 2:] - 2 * v[1:-1, 1:-1] + v[1:-1, :-2]

    is_convex = (d_xx >= 0) & (d_yy >= 0)
    is_concave = (d_xx <= 0) & (d_yy <= 0)

    print(is_concave)

    return -0.1


def _concavity(v):
    c = 0

    for _x in range(config.N - 1):
        x = _x + 1

        for _y in range(config.M - 1):
            y = _y + 1

            v0 = v[x, y]

            d_left = v[x - 1, y] - v0
            d_right = v[x + 1, y] - v0
            d_bottom = v[x, y - 1] - v0
            d_top = v[x, y + 1] - v0

            if d_left > 0 and d_right > 0:
                c += d_left + d_right

            if d_bottom > 0 and d_top > 0:
                c += d_bottom + d_top

    return c
