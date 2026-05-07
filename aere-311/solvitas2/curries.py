from symbols import *


def ratio_curry(a, b, a_b, b_a):
    return [
        (a_b, a / b),
        (b_a, b / a),
        (a_b, 1 / b_a),
    ]


def state_curry(_u, _p, _rho, _T):
    u, a, M = _u
    p, p0, p_p0, p0_p = _p
    rho, rho0, rho_rho0, rho0_rho = _rho
    T, T0, T_T0, T0_T = _T

    return [
        (p0_p, (1 + ((gamma - 1) / 2) * M**2) ** (gamma / (gamma - 1))),
        (rho0_rho, (1 + ((gamma - 1) / 2) * M**2) ** (1 / (gamma - 1))),
        (T0_T, 1 + ((gamma - 1) / 2) * M**2),
        (p, rho * R * T),
        (p0, rho0 * R * T0),
        #
        (a, sympy.sqrt((gamma * p) / rho)),
        (a, sympy.sqrt(gamma * R * T)),
        #
        (u, M * a),
        #
        *ratio_curry(*_p),
        *ratio_curry(*_rho),
        *ratio_curry(*_T),
    ]


def delta_curry(x1, x2, delta_x):
    return [
        (delta_x, x2 - x1),
    ]


def specific_heat_curry(T=T, _e=(h, e)):
    h, e = _e

    return [
        (cp, (gamma * R) / (gamma - 1)),
        (cv, R / (gamma - 1)),
        (gamma, cp / cv),
        #
        (h, cp * T),
        (e, cv * T),
        #
        # (delta_T0, Q / cp),
    ]


def critical_curry(_0, _star, _r1, _r2):
    p0, rho0, T0 = _0
    p_star, rho_star, T_star = _star
    p0_p_star, rho0_rho_star, T0_T_star = _r1
    p_star_p0, rho_star_rho0, T_star_T0 = _r2

    return [
        (T_star_T0, 2 / (gamma + 1)),
        (p_star_p0, (2 / (gamma + 1)) ** (gamma / (gamma - 1))),
        (rho_star_rho0, (2 / (gamma + 1)) ** (1 / (gamma - 1))),
        #
        *ratio_curry(p0, p_star, p0_p_star, p_star_p0),
        *ratio_curry(rho0, rho_star, rho0_rho_star, rho_star_rho0),
        *ratio_curry(T0, T_star, T0_T_star, T_star_T0),
    ]
