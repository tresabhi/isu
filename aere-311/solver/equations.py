import sympy as sp
from symbols import *

isentropic_equations = [
    # Heat capacity
    sp.Eq(c_v, R / (gamma - 1)),
    sp.Eq(c_p, (gamma * R) / (gamma - 1)),
    #
    # Ideal gas law
    sp.Eq(p, rho * R * T),
    sp.Eq(p0, rho0 * R * T0),
    sp.Eq(p_inf, rho_inf * R * T_inf),
    sp.Eq(p_star, rho_star * R * T_star),
    #
    # Speed of sound (temperature form)
    sp.Eq(a, sp.sqrt(gamma * R * T)),
    sp.Eq(a0, sp.sqrt(gamma * R * T0)),
    sp.Eq(a_inf, sp.sqrt(gamma * R * T_inf)),
    sp.Eq(a_star, sp.sqrt(gamma * R * T_star)),
    #
    # Speed of sound (p/rho form)
    sp.Eq(a, sp.sqrt(gamma * p / rho)),
    sp.Eq(a0, sp.sqrt(gamma * p0 / rho0)),
    sp.Eq(a_inf, sp.sqrt(gamma * p_inf / rho_inf)),
    sp.Eq(a_star, sp.sqrt(gamma * p_star / rho_star)),
    #
    # Mach definition
    sp.Eq(M, u / a),
    sp.Eq(M0, u0 / a0),
    sp.Eq(M_inf, u_inf / a_inf),
    #
    # Mach using temperature sound speed
    sp.Eq(M, u / sp.sqrt(gamma * R * T)),
    sp.Eq(M0, u0 / sp.sqrt(gamma * R * T0)),
    sp.Eq(M_inf, u_inf / sp.sqrt(gamma * R * T_inf)),
    #
    # Velocity from stagnation temperature relation
    sp.Eq(u, M * sp.sqrt(gamma * R * T0 / (1 + ((gamma - 1) / 2) * M**2))),
    sp.Eq(u_inf, M_inf * sp.sqrt(gamma * R * T0 / (1 + ((gamma - 1) / 2) * M_inf**2))),
    #
    # Temperature ratio
    sp.Eq(T0_T, 1 + ((gamma - 1) / 2) * M**2),
    sp.Eq(T0_T_inf, 1 + ((gamma - 1) / 2) * M_inf**2),
    #
    # Pressure ratio
    sp.Eq(p0_p, (1 + (gamma - 1) / 2 * M**2) ** (gamma / (gamma - 1))),
    sp.Eq(p0_p_inf, (1 + (gamma - 1) / 2 * M_inf**2) ** (gamma / (gamma - 1))),
    #
    # Density ratio
    sp.Eq(rho0_rho, (1 + (gamma - 1) / 2 * M**2) ** (1 / (gamma - 1))),
    sp.Eq(rho0_rho_inf, (1 + (gamma - 1) / 2 * M_inf**2) ** (1 / (gamma - 1))),
    #
    # Ratio definitions
    sp.Eq(T0_T, T0 / T),
    sp.Eq(T0_T_inf, T0 / T_inf),
    sp.Eq(T0_T_star, T0 / T_star),
    sp.Eq(p0_p, p0 / p),
    sp.Eq(p0_p_inf, p0 / p_inf),
    sp.Eq(p0_p_star, p0 / p_star),
    sp.Eq(rho0_rho, rho0 / rho),
    sp.Eq(rho0_rho_inf, rho0 / rho_inf),
    sp.Eq(rho0_rho_star, rho0 / rho_star),
    #
    # Star equations
    sp.Eq(1 / T0_T_star, 2 / (gamma + 1)),
    sp.Eq(1 / p0_p_star, (2 / (gamma + 1)) ** (gamma / (gamma + 1))),
    sp.Eq(1 / rho0_rho_star, (2 / (gamma + 1)) ** (1 / (gamma + 1))),
    sp.Eq(M_star**2, ((gamma + 1) * M**2) / (2 + (gamma - 1) * M**2)),
    sp.Eq(M_star, u / a_star),
]

# with open("test.md", "w") as file:
#     for equation in isentropic_equations:
#         file.write(f"$$\n{sp.latex(equation)}\n$$\n\n")

bernoulli_equations = [
    sp.Eq(q, (1 / 2) * rho * u**2),
    sp.Eq(q0, (1 / 2) * rho0 * u0**2),
    #
    sp.Eq(p + q, p0 + q0),
    #
    sp.Eq(rho, rho0),
]
