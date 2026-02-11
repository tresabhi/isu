import sympy as sp
from symbols import *

isentropic_equations = [
    # Heat capacity
    (c_v, R / (gamma - 1)),
    (c_p, (gamma * R) / (gamma - 1)),
    #
    # Ideal gas law
    (p, rho * R * T),
    (p0, rho0 * R * T0),
    (p_inf, rho_inf * R * T_inf),
    (p_star, rho_star * R * T_star),
    #
    # Speed of sound (temperature form)
    (a, sp.sqrt(gamma * R * T)),
    (a0, sp.sqrt(gamma * R * T0)),
    (a_inf, sp.sqrt(gamma * R * T_inf)),
    (a_star, sp.sqrt(gamma * R * T_star)),
    #
    # Speed of sound (p/rho form)
    (a, sp.sqrt(gamma * p / rho)),
    (a0, sp.sqrt(gamma * p0 / rho0)),
    (a_inf, sp.sqrt(gamma * p_inf / rho_inf)),
    (a_star, sp.sqrt(gamma * p_star / rho_star)),
    #
    # Mach definition
    (M, u / a),
    (M0, u0 / a0),
    (M_inf, u_inf / a_inf),
    #
    # Mach using temperature sound speed
    (M, u / sp.sqrt(gamma * R * T)),
    (M0, u0 / sp.sqrt(gamma * R * T0)),
    (M_inf, u_inf / sp.sqrt(gamma * R * T_inf)),
    #
    # Velocity from stagnation temperature relation
    (u, M * sp.sqrt(gamma * R * T0 / (1 + ((gamma - 1) / 2) * M**2))),
    (u_inf, M_inf * sp.sqrt(gamma * R * T0 / (1 + ((gamma - 1) / 2) * M_inf**2))),
    #
    # Temperature ratio
    (T0_T, 1 + ((gamma - 1) / 2) * M**2),
    (T0_T_inf, 1 + ((gamma - 1) / 2) * M_inf**2),
    #
    # Pressure ratio
    (p0_p, (1 + (gamma - 1) / 2 * M**2) ** (gamma / (gamma - 1))),
    (p0_p_inf, (1 + (gamma - 1) / 2 * M_inf**2) ** (gamma / (gamma - 1))),
    #
    # Density ratio
    (rho0_rho, (1 + (gamma - 1) / 2 * M**2) ** (1 / (gamma - 1))),
    (rho0_rho_inf, (1 + (gamma - 1) / 2 * M_inf**2) ** (1 / (gamma - 1))),
    #
    # Ratio definitions
    (T0_T, T0 / T),
    (T0_T_inf, T0 / T_inf),
    (T0_T_star, T0 / T_star),
    (p0_p, p0 / p),
    (p0_p_inf, p0 / p_inf),
    (p0_p_star, p0 / p_star),
    (rho0_rho, rho0 / rho),
    (rho0_rho_inf, rho0 / rho_inf),
    (rho0_rho_star, rho0 / rho_star),
    #
    # Star equations
    (1 / T0_T_star, 2 / (gamma + 1)),
    (1 / p0_p_star, (2 / (gamma + 1)) ** (gamma / (gamma + 1))),
    (1 / rho0_rho_star, (2 / (gamma + 1)) ** (1 / (gamma + 1))),
    (M_star**2, ((gamma + 1) * M**2) / (2 + (gamma - 1) * M**2)),
    (M_star, u / a_star),
]

# with open("test.md", "w") as file:
#     for equation in isentropic_equations:
#         file.write(f"$$\n{sp.latex(equation)}\n$$\n\n")

bernoulli_equations = [
    (q, (1 / 2) * rho * u**2),
    (q0, (1 / 2) * rho0 * u0**2),
    #
    (p + q, p0 + q0),
    #
    (rho, rho0),
]
