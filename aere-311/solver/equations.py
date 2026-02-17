import sympy as sp
from symbols import *

# isentropic_equations = [
#     # Heat capacity
#     (c_p, (gamma * R) / (gamma - 1)),
#     (c_v, R / (gamma - 1)),
#     (c_p / c_v, gamma),
#     (e1, c_v * T1),
#     (e2, c_v * T2),
#     (delta_e_2_1, e2 - e1),
#     (h1, c_p * T1),
#     (h2, c_p * T2),
#     (delta_h_2_1, h2 - h1),
#     (delta_s_2_1, c_p * sp.ln(T2_T1) - R * sp.ln(p2_p1)),
#     (delta_s_2_1, c_v * sp.ln(T2_T1) + R * sp.ln(1 / rho2_rho1)),
#     (p2_p1, (rho2_rho1) ** gamma),
#     (p2_p1, (T2_T1) ** (gamma / (gamma - 1))),
#     (p2_p1, p2 / p1),
#     (delta_h_2_1, c_p * (T2 - T1)),
#     #
#     # Ideal gas law
#     (p, rho * R * T),
#     (p0, rho0 * R * T0),
#     (p1, rho1 * R * T1),
#     (p2, rho2 * R * T2),
#     # (p01, rho01 * R * T01),
#     # (p02, rho02 * R * T02),
#     (p_inf, rho_inf * R * T_inf),
#     (p_star, rho_star * R * T_star),
#     #
#     # Speed of sound (temperature form)
#     (a, sp.sqrt(gamma * R * T)),
#     (a0, sp.sqrt(gamma * R * T0)),
#     (a1, sp.sqrt(gamma * R * T1)),
#     (a2, sp.sqrt(gamma * R * T2)),
#     (a_inf, sp.sqrt(gamma * R * T_inf)),
#     (a_star, sp.sqrt(gamma * R * T_star)),
#     #
#     # Speed of sound (p/rho form)
#     (a, sp.sqrt(gamma * p / rho)),
#     (a0, sp.sqrt(gamma * p0 / rho0)),
#     (a1, sp.sqrt(gamma * p1 / rho1)),
#     (a2, sp.sqrt(gamma * p2 / rho2)),
#     (a_inf, sp.sqrt(gamma * p_inf / rho_inf)),
#     (a_star, sp.sqrt(gamma * p_star / rho_star)),
#     #
#     # Mach definition
#     (M, u / a),
#     (M0, u0 / a0),
#     (M1, u1 / a1),
#     (M2, u2 / a2),
#     (M_inf, u_inf / a_inf),
#     #
#     # Mach using temperature sound speed
#     (M, u / sp.sqrt(gamma * R * T)),
#     (M0, u0 / sp.sqrt(gamma * R * T0)),
#     (M1, u1 / sp.sqrt(gamma * R * T1)),
#     (M2, u2 / sp.sqrt(gamma * R * T2)),
#     (M_inf, u_inf / sp.sqrt(gamma * R * T_inf)),
#     #
#     # Velocity from stagnation temperature relation
#     (u, M * sp.sqrt(gamma * R * T0 / (1 + ((gamma - 1) / 2) * M**2))),
#     (u1, M1 * sp.sqrt(gamma * R * T0 / (1 + ((gamma - 1) / 2) * M1**2))),
#     (u2, M2 * sp.sqrt(gamma * R * T0 / (1 + ((gamma - 1) / 2) * M2**2))),
#     (u_inf, M_inf * sp.sqrt(gamma * R * T0 / (1 + ((gamma - 1) / 2) * M_inf**2))),
#     #
#     # Temperature ratio
#     (T0_T, 1 + ((gamma - 1) / 2) * M**2),
#     (T0_T_inf, 1 + ((gamma - 1) / 2) * M_inf**2),
#     (T01_T1, 1 + ((gamma - 1) / 2) * M1**2),
#     (T02_T2, 1 + ((gamma - 1) / 2) * M2**2),
#     #
#     # Pressure ratio
#     (p0_p, (1 + (gamma - 1) / 2 * M**2) ** (gamma / (gamma - 1))),
#     (p0_p_inf, (1 + (gamma - 1) / 2 * M_inf**2) ** (gamma / (gamma - 1))),
#     (p01_p1, (1 + (gamma - 1) / 2 * M1**2) ** (gamma / (gamma - 1))),
#     (p02_p2, (1 + (gamma - 1) / 2 * M2**2) ** (gamma / (gamma - 1))),
#     #
#     # Density ratio
#     (rho0_rho, (1 + (gamma - 1) / 2 * M**2) ** (1 / (gamma - 1))),
#     (rho0_rho_inf, (1 + (gamma - 1) / 2 * M_inf**2) ** (1 / (gamma - 1))),
#     (rho01_rho1, (1 + (gamma - 1) / 2 * M1**2) ** (1 / (gamma - 1))),
#     (rho02_rho2, (1 + (gamma - 1) / 2 * M2**2) ** (1 / (gamma - 1))),
#     #
#     # Jordan for the win
#     (rho2_rho1, p2_p1 ** (1 / gamma)),
#     #
#     # Ratio definitions
#     (T0_T, T0 / T),
#     (T01_T1, T01 / T1),
#     (T02_T2, T02 / T2),
#     (T2_T1, T2 / T1),
#     (T0_T_inf, T0 / T_inf),
#     (T0_T_star, T0 / T_star),
#     (p0_p, p0 / p),
#     (p01_p1, p01 / p1),
#     (p02_p2, p02 / p2),
#     (p0_p_inf, p0 / p_inf),
#     (p0_p_star, p0 / p_star),
#     (rho0_rho, rho0 / rho),
#     (rho01_rho1, rho01 / rho1),
#     (rho02_rho2, rho02 / rho2),
#     (rho0_rho_inf, rho0 / rho_inf),
#     (rho0_rho_star, rho0 / rho_star),
#     (rho2_rho1, rho2 / rho1),
#     #
#     # Star equations
#     (1 / T0_T_star, 2 / (gamma + 1)),
#     (1 / p0_p_star, (2 / (gamma + 1)) ** (gamma / (gamma + 1))),
#     (1 / rho0_rho_star, (2 / (gamma + 1)) ** (1 / (gamma + 1))),
#     (M_star**2, ((gamma + 1) * M**2) / (2 + (gamma - 1) * M**2)),
#     (M_star, u / a_star),
# ]

# shock_equations = [
#     # Continuity
#     (rho1 * u1, rho2 * u2),
#     #
#     # Momentum
#     (p1 + rho1 * u1**2, p2 + rho2 * u2**2),
#     #
#     # Energy
#     (h1 + u1**2 / 2, h2 + u2**2 / 2),
#     #
#     # Normal shock
#     (M2**2, (1 + ((gamma - 1) / 2) * M1**2) / (gamma * M1**2 - (gamma - 1) / 2)),
#     #
#     # Ratios
#     (rho2_rho1, 1 / u2_u1),
#     (rho2_rho1, ((gamma + 1) * M1**2) / (2 + (gamma - 1) * M1**2)),
#     (p2_p1, 1 + ((2 * gamma) / (gamma + 1)) * (M1**2 - 1)),
#     (T2_T1, h2_h1),
#     (
#         T2_T1,
#         (1 + ((2 * gamma) / (gamma + 1)) * (M1**2 - 1))
#         * ((2 + (gamma - 1) * M1**2) / ((gamma + 1) * M1**2)),
#     ),
#     (
#         delta_s_2_1,
#         c_p
#         * sp.ln(
#             (
#                 (1 + ((2 * gamma) / (gamma + 1)) * (M1**2 - 1))
#                 * ((2 + (gamma - 1) * M1**2) / ((gamma + 1) * M1**2))
#             )
#         )
#         - R * sp.ln(1 + ((2 * gamma) / (gamma + 1)) * (M1**2 - 1)),
#     ),
#     # (delta_s_2_1, -R * sp.ln(p2_p1)), # ONLY TRUE IF T1 = T2
#     (p02_p01, sp.E ** (-delta_s_2_1 / R)),
#     #
#     # Calorically perfect gas
#     (T02, T01),
#     #
#     # Subsonic and supersonic pitot sampling
#     (M1**2, (2 / (gamma - 1)) * (p01_p1 ** ((gamma - 1) / gamma) - 1)),
#     (
#         p02_p1,
#         (
#             (((gamma + 1) ** 2 * M1**2) / (4 * gamma * M1**2 - 2 * (gamma - 1)))
#             ** (gamma / (gamma - 1))
#         )
#         * ((1 - gamma + 2 * gamma * M1**2) / (gamma + 1)),
#     ),
#     #
#     # Composite expansions
#     (rho2_rho1, rho2 / rho1),
#     (u2_u1, u2 / u1),
#     (p01_p1, p01 / p1),
#     (p02_p1, p02 / p1),
#     (T2_T1, T2 / T1),
#     (h2_h1, h2 / h1),
#     (delta_s_2_1, s2 - s1),
# ]

# bernoulli_equations = [
#     (q, (1 / 2) * rho * u**2),
#     (q0, (1 / 2) * rho0 * u0**2),
#     #
#     (p + q, p0 + q0),
#     #
#     (rho, rho0),
# ]

# equation_sets = [
#     isentropic_equations,
#     bernoulli_equations,
#     shock_equations,
# ]

composite_equations = [
    (delta_s, s2 - s1),
    (delta_h, h2 - h1),
    (delta_e, e2 - e1),
    (T2_T1, T2 / T1),
    (p2_p1, p2 / p1),
    (rho2_rho1, rho2 / rho1),
]

# Chapter 7
thermodynamic_equations = [
    # Equation of state
    (p1, rho1 * R * T1),
    (p2, rho2 * R * T2),
    #
    # Calorically perfect gas
    (e1, cv * T1),
    (e2, cv * T2),
    (h1, cp * T1),
    (h2, cp * T2),
    (cp, (gamma * R) / (gamma - 1)),
    (cv, R / (gamma - 1)),
    (gamma, cp / cv),
    #
    # Entropy changes
    (delta_s, cp * sp.ln(T2_T1) - R * sp.ln(p2_p1)),
    (delta_s, cv * sp.ln(T2_T1) + R * sp.ln(1 / rho2_rho1)),
    #
    # Adiabatic
    (h1 + u1**2 / 2, h2 + u2**2 / 2),
]

# Chapter 7
isentropic_equations = [
    (p2_p1, rho2_rho1**gamma),
    (p2_p1, T2_T1 ** (gamma / (gamma - 1))),
]

# Chapter 7
isothermal_equations = [
    (T1, T2),
]

equation_sets = [
    composite_equations,
    thermodynamic_equations,
    isentropic_equations,
]

if __name__ == "__main__":
    with open("test.md", "w") as file:
        for equations in equation_sets:
            for equation in equations:
                file.write(f"$$\n{sp.latex(equation)}\n$$\n\n")
