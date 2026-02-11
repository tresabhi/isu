import sympy as sp
from symbols import *

isentropic_equations = [
    sp.Eq(c_v, R / (gamma - 1)),
    sp.Eq(c_p, (gamma * R) / (gamma - 1)),
    #
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
    sp.Eq(a, (gamma * p / rho) ** (1 / 2)),
    sp.Eq(a_0, (gamma * p_0 / rho_0) ** (1 / 2)),
    sp.Eq(a_inf, (gamma * p_inf / rho_inf) ** (1 / 2)),
    sp.Eq(a_star, (gamma * p_star / rho_star) ** (1 / 2)),
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
    sp.Eq(M, u * sp.sqrt((1 + ((gamma - 1) / 2) * M**2) / (gamma * R * T_0))),
    sp.Eq(
        M_inf, u_inf * sp.sqrt((1 + ((gamma - 1) / 2) * M_inf**2) / (gamma * R * T_inf))
    ),
    sp.Eq(
        M_star,
        u_star * sp.sqrt((1 + ((gamma - 1) / 2) * M_star**2) / (gamma * R * T_star)),
    ),
    #
    sp.Eq(T_0_T, 1 + ((gamma - 1) / 2) * M**2),
    sp.Eq(T_0_T_inf, 1 + ((gamma - 1) / 2) * M_inf**2),
    sp.Eq(T_0_T_star, 1 + ((gamma - 1) / 2) * M_star**2),
    #
    sp.Eq(p_0_p, (1 + (gamma - 1) / 2 * M**2) ** (gamma / (gamma - 1))),
    sp.Eq(p_0_p_inf, (1 + (gamma - 1) / 2 * M_inf**2) ** (gamma / (gamma - 1))),
    sp.Eq(p_0_p_star, (1 + (gamma - 1) / 2 * M_star**2) ** (gamma / (gamma - 1))),
    #
    sp.Eq(rho_0_rho, (1 + (gamma - 1) / 2 * M**2) ** (1 / (gamma - 1))),
    sp.Eq(rho_0_rho_inf, (1 + (gamma - 1) / 2 * M_inf**2) ** (1 / (gamma - 1))),
    sp.Eq(rho_0_rho_star, (1 + (gamma - 1) / 2 * M_star**2) ** (1 / (gamma - 1))),
    #
    sp.Eq(T_0_T, T_0 / T),
    sp.Eq(T_0_T_inf, T_0 / T_inf),
    sp.Eq(T_0_T_star, T_0 / T_star),
    #
    sp.Eq(p_0_p, p_0 / p),
    sp.Eq(p_0_p_inf, p_0 / p_inf),
    sp.Eq(p_0_p_star, p_0 / p_star),
    #
    sp.Eq(rho_0_rho, rho_0 / rho),
    sp.Eq(rho_0_rho_inf, rho_0 / rho_inf),
    sp.Eq(rho_0_rho_star, rho_0 / rho_star),
]

# with open("test.md", "w") as file:
#     for equation in isentropic_equations:
#         file.write(f"$$\n{sp.latex(equation)}\n$$\n\n")

bernoulli_equations = [
    sp.Eq(q, (1 / 2) * rho * u**2),
    sp.Eq(q_0, (1 / 2) * rho_0 * u_0**2),
    #
    sp.Eq(p + q, p_0 + q_0),
    #
    sp.Eq(rho, rho_0),
]
