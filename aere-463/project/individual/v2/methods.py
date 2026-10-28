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
