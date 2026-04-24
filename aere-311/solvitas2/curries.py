from symbols import *


def ratio_curry(a, b, a_b, b_a):
    return [
        (a_b, a / b),
        (b_a, b / a),
        (a_b, 1 / b_a),
    ]


def state_curry(M, _p, _rho, _T):
    p, p0, p_p0, p0_p = _p
    rho, rho0, rho_rho0, rho0_rho = _rho
    T, T0, T_T0, T0_T = _T

    return [
        (p0_p, (1 + ((gamma - 1) / 2) * M**2) ** (gamma / (gamma - 1))),
        (rho0_rho, (1 + ((gamma - 1) / 2) * M**2) ** (1 / (gamma - 1))),
        (T0_T, 1 + ((gamma - 1) / 2) * M**2),
        #
        *ratio_curry(*_p),
        *ratio_curry(*_rho),
        *ratio_curry(*_T),
    ]


def delta_curry(x1, x2, delta_x):
    return [
        (delta_x, x2 - x1),
    ]
