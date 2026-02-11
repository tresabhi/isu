import sympy as sp
from symbols import *

isentropic_equations = [
    # Heat capacity
    sp.Eq(c_v, R / (gamma - 1)),
    sp.Eq(c_p, (gamma * R) / (gamma - 1)),
    #
    # Ideal gas law
    sp.Eq(p, rho * R * T),
    sp.Eq(p_0, rho_0 * R * T_0),
    sp.Eq(p_inf, rho_inf * R * T_inf),
    sp.Eq(p_star, rho_star * R * T_star),
    #
    # Speed of sound (temperature form)
    sp.Eq(a, sp.sqrt(gamma * R * T)),
    sp.Eq(a_0, sp.sqrt(gamma * R * T_0)),
    sp.Eq(a_inf, sp.sqrt(gamma * R * T_inf)),
    sp.Eq(a_star, sp.sqrt(gamma * R * T_star)),
    #
    # Speed of sound (p/rho form)
    sp.Eq(a, sp.sqrt(gamma * p / rho)),
    sp.Eq(a_0, sp.sqrt(gamma * p_0 / rho_0)),
    sp.Eq(a_inf, sp.sqrt(gamma * p_inf / rho_inf)),
    sp.Eq(a_star, sp.sqrt(gamma * p_star / rho_star)),
    #
    # Mach definition
    sp.Eq(M, u / a),
    sp.Eq(M_0, u_0 / a_0),
    sp.Eq(M_inf, u_inf / a_inf),
    sp.Eq(M_star, u_star / a_star),
    #
    # Mach using temperature sound speed
    sp.Eq(M, u / sp.sqrt(gamma * R * T)),
    sp.Eq(M_0, u_0 / sp.sqrt(gamma * R * T_0)),
    sp.Eq(M_inf, u_inf / sp.sqrt(gamma * R * T_inf)),
    sp.Eq(M_star, u_star / sp.sqrt(gamma * R * T_star)),
    #
    # Velocity from stagnation temperature relation
    sp.Eq(u, M * sp.sqrt(gamma * R * T_0 / (1 + ((gamma - 1) / 2) * M**2))),
    sp.Eq(u_inf, M_inf * sp.sqrt(gamma * R * T_0 / (1 + ((gamma - 1) / 2) * M_inf**2))),
    sp.Eq(
        u_star, M_star * sp.sqrt(gamma * R * T_0 / (1 + ((gamma - 1) / 2) * M_star**2))
    ),
    #
    # Temperature ratio
    sp.Eq(T_0_T, 1 + ((gamma - 1) / 2) * M**2),
    sp.Eq(T_0_T_inf, 1 + ((gamma - 1) / 2) * M_inf**2),
    sp.Eq(T_0_T_star, 1 + ((gamma - 1) / 2) * M_star**2),
    #
    # Pressure ratio
    sp.Eq(p_0_p, (1 + (gamma - 1) / 2 * M**2) ** (gamma / (gamma - 1))),
    sp.Eq(p_0_p_inf, (1 + (gamma - 1) / 2 * M_inf**2) ** (gamma / (gamma - 1))),
    sp.Eq(p_0_p_star, (1 + (gamma - 1) / 2 * M_star**2) ** (gamma / (gamma - 1))),
    #
    # Density ratio
    sp.Eq(rho_0_rho, (1 + (gamma - 1) / 2 * M**2) ** (1 / (gamma - 1))),
    sp.Eq(rho_0_rho_inf, (1 + (gamma - 1) / 2 * M_inf**2) ** (1 / (gamma - 1))),
    sp.Eq(rho_0_rho_star, (1 + (gamma - 1) / 2 * M_star**2) ** (1 / (gamma - 1))),
    #
    # Ratio definitions
    sp.Eq(T_0_T, T_0 / T),
    sp.Eq(T_0_T_inf, T_0 / T_inf),
    sp.Eq(T_0_T_star, T_0 / T_star),
    sp.Eq(p_0_p, p_0 / p),
    sp.Eq(p_0_p_inf, p_0 / p_inf),
    sp.Eq(p_0_p_star, p_0 / p_star),
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
