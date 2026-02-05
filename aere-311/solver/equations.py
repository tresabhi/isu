from sympy import Eq
from symbols import *

isentropic_equations = [
    Eq(p, rho * R * T),
    Eq(p_inf, rho_inf * R * T_inf),
    Eq(p_star, rho_star * R * T_star),
    #
    Eq(a, (gamma * R * T) ** (1 / 2)),
    Eq(a_inf, (gamma * R * T_inf) ** (1 / 2)),
    Eq(a_star, (gamma * R * T_star) ** (1 / 2)),
    #
    Eq(M, u / a),
    Eq(M_inf, u_inf / a_inf),
    Eq(M_star, u_star / a_star),
    #
    Eq(T_0 / T, (1 + ((gamma - 1) / 2) * M**2)),
    Eq(T_0 / T_inf, (1 + ((gamma - 1) / 2) * M_inf**2)),
    Eq(T_0 / T_star, (1 + ((gamma - 1) / 2) * M_star**2)),
    #
    Eq(rho_0 / rho, (1 + (gamma - 1) / 2 * M**2) ** (1 / (gamma - 1))),
    Eq(rho_0 / rho_inf, (1 + (gamma - 1) / 2 * M_inf**2) ** (1 / (gamma - 1))),
    Eq(rho_0 / rho_star, (1 + (gamma - 1) / 2 * M_star**2) ** (1 / (gamma - 1))),
    #
    Eq(p_0 / p, (1 + (gamma - 1) / 2 * M**2) ** (gamma / (gamma - 1))),
    Eq(p_0 / p_inf, (1 + (gamma - 1) / 2 * M_inf**2) ** (gamma / (gamma - 1))),
    Eq(p_0 / p_star, (1 + (gamma - 1) / 2 * M_star**2) ** (gamma / (gamma - 1))),
]

equations_bernoulli = [
    Eq(p_0 + (1 / 2) * rho_0 * u_0**2, p + (1 / 2) * rho * u**2),
    Eq(rho_0, rho),
]
