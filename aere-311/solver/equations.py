import sympy as sp
from symbols import *

isentropic_equations = [
    sp.Eq(p, rho * R * T),
    sp.Eq(p_0, rho_0 * R * T_0),
    sp.Eq(p_inf, rho_inf * R * T_inf),
    sp.Eq(p_star, rho_star * R * T_star),
    #
    sp.Eq(a, (gamma * R * T) ** (1 / 2)),
    sp.Eq(a_0, (gamma * R * T_0) ** (1 / 2)),
    sp.Eq(a_inf, (gamma * R * T_inf) ** (1 / 2)),
    sp.Eq(a_star, (gamma * R * T_star) ** (1 / 2)),
    #
    sp.Eq(M, u / a),
    sp.Eq(M_0, u_0 / a_0),
    sp.Eq(M_inf, u_inf / a_inf),
    sp.Eq(M_star, u_star / a_star),
    #
    sp.Eq(M, u / ((gamma * R * T) ** (1 / 2))),
    sp.Eq(M_0, u_0 / ((gamma * R * T_0) ** (1 / 2))),
    sp.Eq(M_inf, u_inf / ((gamma * R * T_inf) ** (1 / 2))),
    sp.Eq(M_star, u_star / ((gamma * R * T_star) ** (1 / 2))),
    #
    sp.Eq(T_0 / T, (1 + ((gamma - 1) / 2) * M**2)),
    sp.Eq(T_0 / T_inf, (1 + ((gamma - 1) / 2) * M_inf**2)),
    sp.Eq(T_0 / T_star, (1 + ((gamma - 1) / 2) * M_star**2)),
    #
    sp.Eq(rho_0 / rho, (1 + (gamma - 1) / 2 * M**2) ** (1 / (gamma - 1))),
    sp.Eq(rho_0 / rho_inf, (1 + (gamma - 1) / 2 * M_inf**2) ** (1 / (gamma - 1))),
    sp.Eq(rho_0 / rho_star, (1 + (gamma - 1) / 2 * M_star**2) ** (1 / (gamma - 1))),
    #
    sp.Eq(p_0 / p, (1 + (gamma - 1) / 2 * M**2) ** (gamma / (gamma - 1))),
    sp.Eq(p_0 / p_inf, (1 + (gamma - 1) / 2 * M_inf**2) ** (gamma / (gamma - 1))),
    sp.Eq(p_0 / p_star, (1 + (gamma - 1) / 2 * M_star**2) ** (gamma / (gamma - 1))),
    #
    sp.Eq(
        M, u * sp.sqrt((1 + ((gamma - 1) / 2) * M**2) / (gamma * R * T_0))
    ),  # might be wrong
    sp.Eq(
        M_inf, u_inf * sp.sqrt((1 + ((gamma - 1) / 2) * M_inf**2) / (gamma * R * T_0))
    ),  # might be wrong
    sp.Eq(
        M_star,
        u_star * sp.sqrt((1 + ((gamma - 1) / 2) * M_star**2) / (gamma * R * T_0)),
    ),  # might be wrong
]

# with open("test.md", "w") as file:
#     for equation in isentropic_equations:
#         file.write(f"$$\n{sp.latex(equation)}\n$$\n\n")

bernoulli_equations = [
    sp.Eq(q, (1 / 2) * rho * u**2),
    sp.Eq(q_0, (1 / 2) * rho_0 * u_0**2),
    sp.Eq(q_inf, (1 / 2) * rho_inf * u_inf**2),
    sp.Eq(q_star, (1 / 2) * rho_star * u_star**2),
    #
    sp.Eq(p + q, p_0 + q_0),
    sp.Eq(p + q, p_inf + q_inf),
    sp.Eq(p + q, p_star + q_star),
    #
    sp.Eq(rho, rho_0),
    sp.Eq(rho, rho_inf),
    sp.Eq(rho, rho_star),
]
