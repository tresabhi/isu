import sympy as sp
from symbols import *

continuity_equations = [
    (A1, (sp.pi / 4) * d1**2),
    (A2, (sp.pi / 4) * d2**2),
    (V_dot1, A1 * u1),
    (V_dot2, A2 * u2),
    (V_dot_sub, A_sub * u_sub),
    (V_dot_sup, A_sup * u_sup),
    #
    (m_dot1, rho1 * V_dot1),
    (m_dot2, rho2 * V_dot2),
    (m_dot, m_dot1),
    (m_dot, m_dot2),
    (m_dot_sub, rho_sub * V_dot_sub),
    (m_dot_sup, rho_sup * V_dot_sup),
    #
    (F, m_dot * (u2 - u1) + (p2 * A2 - p1 * A1)),
]

ratio_equations = [
    (delta_s, s2 - s1),
    (delta_h, h2 - h1),
    (delta_e, e2 - e1),
    #
    (T2_T1, T2 / T1),
    (T0_T1, T0 / T1),
    (T0_T2, T0 / T2),
    (T01_T1, T01 / T1),
    (T02_T2, T02 / T2),
    (T02_T01, T02 / T01),
    (T_star_T0, T_star / T0),
    (T_star_T1, T_star / T1),
    (T_star_T2, T_star / T2),
    (T0_T_sub, T0 / T_sub),
    (T0_T_sup, T0 / T_sup),
    #
    (p2_p1, p2 / p1),
    (p0_p1, p0 / p1),
    (p0_p2, p0 / p2),
    (p02_p01, p02 / p01),
    (p01_p1, p01 / p1),
    (p01_p2, p01 / p2),
    (p02_p1, p02 / p1),
    (p02_p2, p02 / p2),
    (p_star_p0, p_star / p0),
    (p_star_p1, p_star / p1),
    (p_star_p2, p_star / p2),
    (p0_p_sub, p0 / p_sub),
    (p0_p_sup, p0 / p_sup),
    (p_sub_p0, 1 / p0_p_sub),
    (p_sup_p0, 1 / p0_p_sup),
    (p01_p02, p01 / p02),
    (p01_p02, 1 / p02_p01),
    (pB_p0, pB / p0),
    #
    (rho2_rho1, rho2 / rho1),
    (rho0_rho1, rho0 / rho1),
    (rho0_rho2, rho0 / rho2),
    (rho01_rho1, rho01 / rho1),
    (rho02_rho2, rho02 / rho2),
    (rho_star_rho0, rho_star / rho0),
    (rho_star_rho1, rho_star / rho1),
    (rho_star_rho2, rho_star / rho2),
    (rho_star_rho01, rho_star / rho01),
    (rho_star_rho02, rho_star / rho02),
    (rho_star_rho_sub, rho_star / rho_sub),
    (rho_star_rho_sup, rho_star / rho_sup),
    (rho0_rho_sub, rho0 / rho_sub),
    (rho0_rho_sup, rho0 / rho_sup),
    #
    (u2_u1, u2 / u1),
    (a_star_u1, a_star / u1),
    (a_star_u2, a_star / u2),
    (a_star_u_sub, a_star / u_sub),
    (a_star_u_sup, a_star / u_sup),
    (u1_a_star, u1 / a_star),
    (u2_a_star, u2 / a_star),
    (u_sub_a_star, u_sub / a_star),
    (u_sup_a_star, u_sup / a_star),
    #
    (M_sub, u_sub / a_sub),
    (M_sup, u_sup / a_sup),
    #
    (M1, u1 / a1),
    (M2, u2 / a2),
    #
    (h2_h1, h2 / h1),
    #
    (A1_A_star, A1 / A_star),
    (A2_A_star, A2 / A_star),
    (A_A_star, A_sub / A_star),
    (A_A_star, A_sup / A_star),
    (At2_At1, At2 / At1),
]

state_equations = [
    #
    # Chapter 7
    (p0, rho0 * R * T0),
    (p1, rho1 * R * T1),
    (p2, rho2 * R * T2),
    (p01, rho01 * R * T01),
    # (p02, rho02 * R * T02),
    (p_star, rho_star * R * T_star),
    #
    (p_sub, rho_sub * R * T_sub),
    (p_sup, rho_sup * R * T_sup),
]

entropy_equations = [
    #
    # Chapter 7
    (delta_s, cp * sp.ln(T2_T1) - R * sp.ln(p2_p1)),
    (delta_s, cv * sp.ln(T2_T1) + R * sp.ln(1 / rho2_rho1)),
]

isentropic_equations = [
    #
    # Chapter 7
    (delta_s, 0),
    (p2_p1, rho2_rho1**gamma),
    (p2_p1, T2_T1 ** (gamma / (gamma - 1))),
]

isothermal_equations = [
    #
    # Chapter 7
    (T1, T2),
]

specific_heat_equations = [
    (cp, (gamma * R) / (gamma - 1)),
    (cv, R / (gamma - 1)),
    (gamma, cp / cv),
]

calorically_perfect_equations = [  #
    # Chapter 7
    (e1, cv * T1),
    (e2, cv * T2),
    (h1, cp * T1),
    (h2, cp * T2),
    #
    # Chapter 8
    (a1, sp.sqrt((gamma * p1) / rho1)),
    (a2, sp.sqrt((gamma * p2) / rho2)),
    (a1, sp.sqrt(gamma * R * T1)),
    (a2, sp.sqrt(gamma * R * T2)),
    (a_star, sp.sqrt(gamma * R * T_star)),
    #
    (a_sub, sp.sqrt(gamma * R * T_sub)),
    (a_sup, sp.sqrt(gamma * R * T_sup)),
]

adiabatic_equations = [
    #
    # Chapter 8
    (h1 + u1**2 / 2, h2 + u2**2 / 2),
    (cp * T1 + u1**2 / 2, cp * T2 + u2**2 / 2),
    (a1**2 / (gamma - 1) + u1**2 / 2, a2**2 / (gamma - 1) + u2**2 / 2),
]

static_equations = [
    #
    # Chapter 8
    (a1**2 / (gamma - 1) + u1**2 / 2, a0**2 / (gamma - 1)),
    (a2**2 / (gamma - 1) + u2**2 / 2, a0**2 / (gamma - 1)),
    #
    (cp * T1 + u1**2 / 2, cp * T0),
    (cp * T2 + u2**2 / 2, cp * T0),
    #
    (T0_T1, 1 + ((gamma - 1) / 2) * M1**2),
    (T0_T2, 1 + ((gamma - 1) / 2) * M2**2),
    #
    (p0_p1, (1 + ((gamma - 1) / 2) * M1**2) ** (gamma / (gamma - 1))),
    (p0_p2, (1 + ((gamma - 1) / 2) * M2**2) ** (gamma / (gamma - 1))),
    #
    (rho0_rho1, (1 + ((gamma - 1) / 2) * M1**2) ** (1 / (gamma - 1))),
    (rho0_rho2, (1 + ((gamma - 1) / 2) * M2**2) ** (1 / (gamma - 1))),
]

shock_static_equations = [
    (T01_T1, 1 + ((gamma - 1) / 2) * M1**2),
    (T02_T2, 1 + ((gamma - 1) / 2) * M2**2),
    (T0_T_sub, 1 + ((gamma - 1) / 2) * M_sub**2),
    (T0_T_sup, 1 + ((gamma - 1) / 2) * M_sup**2),
    #
    (p01_p1, (1 + ((gamma - 1) / 2) * M1**2) ** (gamma / (gamma - 1))),
    (p02_p2, (1 + ((gamma - 1) / 2) * M2**2) ** (gamma / (gamma - 1))),
    (p0_p_sub, (1 + ((gamma - 1) / 2) * M_sub**2) ** (gamma / (gamma - 1))),
    (p0_p_sup, (1 + ((gamma - 1) / 2) * M_sup**2) ** (gamma / (gamma - 1))),
    #
    (rho01_rho1, (1 + ((gamma - 1) / 2) * M1**2) ** (1 / (gamma - 1))),
    (rho02_rho2, (1 + ((gamma - 1) / 2) * M2**2) ** (1 / (gamma - 1))),
    (rho0_rho_sub, (1 + ((gamma - 1) / 2) * M_sub**2) ** (1 / (gamma - 1))),
    (rho0_rho_sup, (1 + ((gamma - 1) / 2) * M_sup**2) ** (1 / (gamma - 1))),
]

bernoulli_equations = [
    (p0, p1 + (1 / 2) * rho1 * u1**2),
    (p0, p2 + (1 / 2) * rho2 * u2**2),
    (rho0, rho1),
    (rho0, rho2),
]

normal_shock_equations = [
    #
    # Chapter 8
    (rho1 * u1, rho2 * u2),
    (p1 + rho1 * u1**2, p2 + rho2 * u2**2),
    (h1 + u1**2 / 2, h2 + u2**2 / 2),
    #
    (M2**2, (1 + ((gamma - 1) / 2) * M1**2) / (gamma * M1**2 - (gamma - 1) / 2)),
    (rho2_rho1, 1 / u2_u1),
    (rho2_rho1, ((gamma + 1) * M1**2) / (2 + (gamma - 1) * M1**2)),
    (p2_p1, 1 + ((2 * gamma) / (gamma + 1)) * (M1**2 - 1)),
    (T2_T1, h2_h1),
    (
        T2_T1,
        (1 + ((2 * gamma) / (gamma + 1)) * (M1**2 - 1))
        * ((2 + (gamma - 1) * M1**2) / ((gamma + 1) * M1**2)),
    ),
    (
        delta_s,
        cp
        * sp.ln(
            (1 + ((2 * gamma) / (gamma + 1)) * (M1**2 - 1))
            * ((2 + (gamma - 1) * M1**2) / ((gamma + 1) * M1**2))
        )
        - R * sp.ln(1 + ((2 * gamma) / (gamma + 1)) * (M1**2 - 1)),
    ),
    (p02_p01, sp.exp(-delta_s / R)),
    #
    # source: my butt
    (rho01_rho1, (1 + ((gamma - 1) / 2) * M1**2) ** (1 / (gamma - 1))),
    (rho02_rho2, (1 + ((gamma - 1) / 2) * M2**2) ** (1 / (gamma - 1))),
]

sub_sonic_equations = [
    (M1**2, (2 / (gamma - 1)) * (p01_p1 ** ((gamma - 1) / gamma) - 1)),
    (M2**2, (2 / (gamma - 1)) * (p02_p2 ** ((gamma - 1) / gamma) - 1)),
]

sonic_equations = [
    #
    # Chapter 8
    (a1**2 / (gamma - 1) + u1**2 / 2, ((gamma + 1) / (2 * (gamma - 1))) * a_star**2),
    (a2**2 / (gamma - 1) + u2**2 / 2, ((gamma + 1) / (2 * (gamma - 1))) * a_star**2),
    #
    (a1**2, ((gamma + 1) / 2) * a_star**2 - ((gamma - 1) / 2) * u1**2),
    (a2**2, ((gamma + 1) / 2) * a_star**2 - ((gamma - 1) / 2) * u2**2),
    #
    (T_star_T0, 2 / (gamma + 1)),
    (p_star_p0, (2 / (gamma + 1)) ** (gamma / (gamma - 1))),
    (rho_star_rho0, (2 / (gamma + 1)) ** (1 / (gamma - 1))),
    # 1
    (M1**2, 2 / ((gamma + 1) / M1_star**2 - (gamma - 1))),
    (M2**2, 2 / ((gamma + 1) / M2_star**2 - (gamma - 1))),
    #
    (M1_star**2, ((gamma + 1) * M1**2) / (2 + (gamma - 1) * M1**2)),
    (M2_star**2, ((gamma + 1) * M2**2) / (2 + (gamma - 1) * M2**2)),
]

super_sonic_equations = [
    (
        p02_p1,
        (((gamma + 1) ** 2 * M1**2) / (4 * gamma * M1**2 - 2 * (gamma - 1)))
        ** (gamma / (gamma - 1))
        * ((1 - gamma + 2 * gamma * M1**2) / (gamma + 1)),
    ),
    (
        p01_p2,
        (((gamma + 1) ** 2 * M2**2) / (4 * gamma * M2**2 - 2 * (gamma - 1)))
        ** (gamma / (gamma - 1))
        * ((1 - gamma + 2 * gamma * M2**2) / (gamma + 1)),
    ),
]

oblique_shock_equations = [
    #
    # Chapter 9
    (w1, w2),
    #
    (Mn1, M1 * sp.sin(beta_weak)),
    (Mn2**2, (1 + ((gamma - 1) / 2) * Mn1**2) / (gamma * Mn1**2 - (gamma - 1) / 2)),
    (rho2_rho1, ((gamma + 1) * Mn1**2) / (2 + (gamma - 1) * Mn1**2)),
    (p2_p1, 1 + ((2 * gamma) / (gamma + 1)) * (Mn1**2 - 1)),
    (T2_T1, p2_p1 / rho2_rho1),
    (M2, Mn2 / sp.sin(beta_weak - theta)),
    #
    (sp.tan(beta_weak), u1 / w1),
    (sp.tan(beta_weak - theta), u2 / w2),
    (sp.tan(beta_weak - theta) / sp.tan(beta_weak), u2_u1),
    (u2_u1, 1 / rho2_rho1),
    (
        u2_u1,
        (2 + (gamma - 1) * M1**2 * sp.sin(beta_weak) ** 2)
        / ((gamma + 1) * M1**2 * sp.sin(beta_weak) ** 2),
    ),
    #
    (
        sp.tan(theta),
        2
        * sp.cot(beta_weak)
        * (
            (M1**2 * sp.sin(beta_weak) ** 2 - 1)
            / (M1**2 * (gamma + sp.cos(2 * beta_weak)) + 2)
        ),
    ),
    (
        sp.tan(theta),
        2
        * sp.cot(beta_strong)
        * (
            (M1**2 * sp.sin(beta_strong) ** 2 - 1)
            / (M1**2 * (gamma + sp.cos(2 * beta_strong)) + 2)
        ),
    ),
    (theta, beta_weak - sp.atan((1 / rho2_rho1) * sp.tan(beta_weak))),
]

expansion_wave_equations = [
    #
    # Chapter 9
    (
        nu1,
        sp.sqrt((gamma + 1) / (gamma - 1))
        * sp.atan(sp.sqrt(((gamma - 1) / (gamma + 1)) * (M1**2 - 1)))
        - sp.atan(sp.sqrt(M1**2 - 1)),
    ),
    (
        nu2,
        sp.sqrt((gamma + 1) / (gamma - 1))
        * sp.atan(sp.sqrt(((gamma - 1) / (gamma + 1)) * (M2**2 - 1)))
        - sp.atan(sp.sqrt(M2**2 - 1)),
    ),
    #
    (theta, nu2 - nu1),
    #
    (sp.tan(mu1), 1 / sp.sqrt(M1**2 - 1)),
    (sp.tan(mu2), 1 / sp.sqrt(M2**2 - 1)),
    #
    (T02, T01),
    (p02, p01),
    (T2_T1, T2_T02 / T1_T01),
    (p2_p1, p2_p02 / p1_p01),
    (T2_T1, (1 + ((gamma - 1) / 2) * M1**2) / (1 + ((gamma - 1) / 2) * M2**2)),
    (
        p2_p1,
        ((1 + ((gamma - 1) / 2) * M1**2) / (1 + ((gamma - 1) / 2) * M2**2))
        ** (gamma / (gamma - 1)),
    ),
]

dynamic_equations = [
    #
    # Chapter 9.7
    (q1, (gamma / 2) * p1 * M1**2),
    (q2, (gamma / 2) * p2 * M2**2),
]

flat_plate_equations = [
    #
    # Chapter 9.7
    (R_prime, (p3 - p2) * c),
    (L_prime, (p3 - p2) * c * sp.cos(alpha)),
    (D_prime, (p3 - p2) * c * sp.sin(alpha)),
    #
    (cl, L_prime / (q1 * S)),
    (cl, L_prime / ((gamma / 2) * p1 * M1**2 * c)),
    (cl, (2 / (gamma * M1**2)) * (p3_p1 - p2_p1) * sp.cos(alpha)),
    #
    (cd, D_prime / (q1 * S)),
    (cd, D_prime / ((gamma / 2) * p1 * M1**2 * c)),
    (cd, (2 / (gamma * M1**2)) * (p3_p1 - p2_p1) * sp.sin(alpha)),
    #
    (cd / cl, sp.tan(alpha)),
]

linearized_flat_plate_equations = [
    (cl, (4 * alpha) / sp.sqrt(M1**2 - 1)),
    (cd, (4 * alpha**2) / sp.sqrt(M1**2 - 1)),
]

diamond_wedge_equations = [
    #
    # these are my derivations; use at your own risk
    (t / c, sp.tan(epsilon)),
    #
    (
        cl,
        (2 / (gamma * M1**2))
        * (1 / (2 * sp.cos(epsilon)))
        * (
            (p4_p1 - p3_p1) * sp.cos(alpha + epsilon)
            + (p5_p1 - p2_p1) * sp.cos(alpha - epsilon)
        ),
    ),
    (
        cd,
        (2 / (gamma * M1**2))
        * (1 / (2 * sp.cos(epsilon)))
        * (
            (p4_p1 - p3_p1) * sp.sin(alpha + epsilon)
            + (p5_p1 - p2_p1) * sp.sin(alpha - epsilon)
        ),
    ),
    #
    (p3_p1, p3_p2 * p2_p1),
    (p5_p1, p5_p4 * p4_p1),
]

# subsonic_nozzle_flow_equations = [
#     ,
#     (p0_p, (1 + ((gamma - 1) / 2) * M**2) ** (1 / (gamma - 1))),
# ]

area_mach_equations = [
    # (
    #     A_A_star**2,
    #     (1 / (M_sub**2))
    #     * ((2 / (gamma + 1)) * (1 + ((gamma - 1) / 2) * M_sub**2))
    #     ** ((gamma + 1) / (gamma - 1)),
    # ),
    (
        A_A_star**2,
        (1 / (M_sup**2))
        * ((2 / (gamma + 1)) * (1 + ((gamma - 1) / 2) * M_sup**2))
        ** ((gamma + 1) / (gamma - 1)),
    ),
]

diffuser_equations = [
    (M1, Me),
    (At1, At),
    (At2_At1, p01_p02),
    #
    (eta_D, pB_p0 / p02_p01),
]
