import config
import math


def plate_mass(v, t):
    m = 0

    for y in range(config.M):
        for x in range(config.N):
            i_bottom_right = y * (config.N + 1) + x + 1
            i_top_left = (y + 1) * (config.N + 1) + x

            v1 = v[i_bottom_right]
            v2 = v[i_top_left]

            for j in range(2):
                if j == 0:
                    # bottom left corner
                    v0 = v[i_bottom_right - 1]
                else:
                    # top right corner
                    v0 = v[i_top_left + 1]

                i = 2 * (y * config.N + x) + j

                abs_n_i = config.Delta * math.sqrt(
                    (v0 - v1) ** 2 + (v0 - v2) ** 2 + config.Delta**2
                )
                A_i = abs_n_i / 2

                t_i = t[i]

                m_i = config.rho * A_i * t_i
                m += m_i

    return m


def wall_mass(v):
    m = 0

    # bottom walls
    for i in range(config.N):
        i_left = i
        i_right = i + 1

        v0 = v[i_left]
        v1 = v[i_right]

        m_j = 0.5 * config.t_w * config.rho * (v0 + v1) * config.Delta

        m += m_j

    # top walls
    for i in range(config.N):
        i_left = config.M * (config.N + 1) + i
        i_right = config.M * (config.N + 1) + i + 1

        v0 = v[i_left]
        v1 = v[i_right]

        m_j = 0.5 * config.t_w * config.rho * (v0 + v1) * config.Delta

        m += m_j

    return m
