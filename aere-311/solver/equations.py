import sympy as sp
from symbols import *

continuity_equations = [
    (A1, (sp.pi / 4) * d1**2),
    (A2, (sp.pi / 4) * d2**2),
    (V_dot1, A1 * u1),
    (V_dot2, A2 * u2),
    #
    (m_dot1, rho1 * V_dot1),
    (m_dot2, rho2 * V_dot2),
    (m_dot, m_dot1),
    (m_dot, m_dot2),
    #
    (F, m_dot * (u2 - u1) + (p2 * A2 - p1 * A1)),
]

composite_equations = [
    (delta_s, s2 - incident),
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
    #
    (rho2_rho1, rho2 / rho1),
    (rho0_rho1, rho0 / rho1),
    (rho0_rho2, rho0 / rho2),
    (rho01_rho1, rho01 / rho1),
    (rho02_rho2, rho02 / rho2),
    (rho_star_rho0, rho_star / rho0),
    (rho_star_rho1, rho_star / rho1),
    (rho_star_rho2, rho_star / rho2),
    #
    (u2_u1, u2 / u1),
    #
    (M1, u1 / a1),
    (M2, u2 / a2),
    #
    (h2_h1, h2 / h1),
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

shock_static_equations = {
    (T01_T1, 1 + ((gamma - 1) / 2) * M1**2),
    (T02_T2, 1 + ((gamma - 1) / 2) * M2**2),
    #
    (p01_p1, (1 + ((gamma - 1) / 2) * M1**2) ** (gamma / (gamma - 1))),
    (p02_p2, (1 + ((gamma - 1) / 2) * M2**2) ** (gamma / (gamma - 1))),
    #
    (rho01_rho1, (1 + ((gamma - 1) / 2) * M1**2) ** (1 / (gamma - 1))),
    (rho02_rho2, (1 + ((gamma - 1) / 2) * M2**2) ** (1 / (gamma - 1))),
}

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
    (M2**2, 2 / ((gamma + 1) / M1_star**2 - (gamma - 1))),
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

oblique_shocks = [
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
