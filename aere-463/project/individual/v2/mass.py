import config
import math


def plate_mass(v, t):
    m = 0

    for y in range(config.M):
        for x in range(config.N):
            for j in range(2):
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
    return 0
