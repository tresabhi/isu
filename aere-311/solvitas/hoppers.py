from symbols import *
from curries import *
from hopper import *


class State(Hopper):
    equations = [
        *state_curry(
            (u, a, M),
            (p, p0, p_p0, p0_p),
            (rho, rho0, rho_rho0, rho0_rho),
            (T, T0, T_T0, T0_T),
        ),
    ]


class Adiabatic(Hopper):
    initials = {
        M1: 2,
        M2: 2,
    }

    equations = [
        (h0, h1 + u1**2 / 2),
        (h0, h2 + u2**2 / 2),
        #
        *ratio_curry(p1, p2, p1_p2, p2_p1),
        *ratio_curry(rho1, rho2, rho1_rho2, rho2_rho1),
        *ratio_curry(T1, T2, T1_T2, T2_T1),
        #
        *specific_heat_curry(T0, (h0, e0)),
        *specific_heat_curry(T1, (h1, e1)),
        *specific_heat_curry(T2, (h2, e2)),
        #
        *delta_curry(h1, h2, delta_h),
        *delta_curry(e1, e2, delta_e),
        *delta_curry(s1, s2, delta_s),
    ]


class Isentropic(Adiabatic):
    equations = [
        *Adiabatic.equations,
        #
        (delta_s, 0),
        #
        (p2_p1, rho2_rho1**gamma),
        (p2_p1, T2_T1 ** (gamma / (gamma - 1))),
        #
        (M1_star, u1 / a_star),
        (M2_star, u2 / a_star),
        #
        (m_dot, rho1 * u1 * A1),
        (m_dot, rho2 * u2 * A2),
        #
        *state_curry(
            (u1, a1, M1),
            (p1, p0, p1_p0, p0_p1),
            (rho1, rho0, rho1_rho0, rho0_rho1),
            (T1, T0, T1_T0, T0_T1),
        ),
        *state_curry(
            (u2, a2, M2),
            (p2, p0, p2_p0, p0_p2),
            (rho2, rho0, rho2_rho0, rho0_rho2),
            (T2, T0, T2_T0, T0_T2),
        ),
        *state_curry(
            (u_star, a_star, 1),
            (p_star, p0, p_star_p0, p0_p_star),
            (rho_star, rho0, rho_star_rho0, rho0_rho_star),
            (T_star, T0, T_star_T0, T0_T_star),
        ),
        #
        *critical_curry(
            (p0, rho0, T0),
            (p_star, rho_star, T_star),
            (p0_p_star, rho0_rho_star, T0_T_star),
            (p_star_p0, rho_star_rho0, T_star_T0),
        ),
    ]


class SubsonicRayleigh(Hopper):
    initials = {
        M2: 0.5,
    }

    equations = [
        (p2_p1, (1 + gamma * M1**2) / (1 + gamma * M2**2)),
        (T2_T1, (p2_p1 * (M2 / M1)) ** 2),
        #
        (p1_p_star, (1 + gamma) / (1 + gamma * M1**2)),
        (p2_p_star, (1 + gamma) / (1 + gamma * M2**2)),
        #
        (T1_T_star, M1**2 * (((1 + gamma) ** 2) / ((1 + gamma * M1**2) ** 2))),
        (T2_T_star, M2**2 * (((1 + gamma) ** 2) / ((1 + gamma * M2**2) ** 2))),
        #
        (rho_star_rho1, u1_u_star),
        (rho_star_rho2, u2_u_star),
        #
        (rho_star_rho1, M1**2 * ((1 + gamma) / (1 + gamma * M1**2))),
        (rho_star_rho2, M2**2 * ((1 + gamma) / (1 + gamma * M2**2))),
        #
        (
            T01_T0_star,
            M1**2
            * (((1 + gamma) ** 2) / ((1 + gamma * M1**2) ** 2))
            * ((2 + (gamma - 1) * M1**2) / (2 + (gamma - 1))),
        ),
        (
            T02_T0_star,
            M2**2
            * (((1 + gamma) ** 2) / ((1 + gamma * M2**2) ** 2))
            * ((2 + (gamma - 1) * M2**2) / (2 + (gamma - 1))),
        ),
        #
        (M1, u1 / a1),
        (M2, u2 / a2),
        #
        *specific_heat_curry(),
        #
        *delta_curry(T01, T02, delta_T0),
        #
        *state_curry(
            (u1, a1, M1),
            (p1, p01, p1_p01, p01_p1),
            (rho1, rho01, rho1_rho01, rho01_rho1),
            (T1, T01, T1_T01, T01_T1),
        ),
        *state_curry(
            (u2, a2, M2),
            (p2, p02, p2_p02, p02_p2),
            (rho2, rho02, rho2_rho02, rho02_rho2),
            (T2, T02, T2_T02, T02_T2),
        ),
        #
        *ratio_curry(p1, p2, p1_p2, p2_p1),
        *ratio_curry(rho1, rho2, rho1_rho2, rho2_rho1),
        *ratio_curry(T1, T2, T1_T2, T2_T1),
        #
        *ratio_curry(p1, p_star, p1_p_star, p_star_p1),
        *ratio_curry(p2, p_star, p2_p_star, p_star_p2),
        *ratio_curry(T1, T_star, T1_T_star, T_star_T1),
        *ratio_curry(T2, T_star, T2_T_star, T_star_T2),
        *ratio_curry(T01, T0_star, T01_T0_star, T0_star_T01),
        *ratio_curry(T02, T0_star, T02_T0_star, T0_star_T02),
        *ratio_curry(rho1, rho_star, rho1_rho_star, rho_star_rho1),
        *ratio_curry(rho2, rho_star, rho2_rho_star, rho_star_rho2),
        *ratio_curry(u1, u_star, u1_u_star, u_star_u1),
        *ratio_curry(u2, u_star, u2_u_star, u_star_u2),
    ]


class SupersonicRayleigh(Hopper):
    initials = {
        M2: 2,
    }

    equations = SubsonicRayleigh.equations


class NormalShock(Hopper):
    # initials = {
    #     M1: 0.5,
    #     M2: 0.5,
    # }

    equations = [
        (M2**2, (1 + ((gamma - 1) / 2) * M1**2) / (gamma * M1**2 - (gamma - 1) / 2)),
        #
        (rho2_rho1, u1_u2),
        (rho2_rho1, ((gamma + 1) * M1**2) / (2 + (gamma - 1) * M1**2)),
        #
        (p2_p1, 1 + ((2 * gamma) / (gamma + 1)) * (M1**2 - 1)),
        #
        (T2_T1, h2_h1),
        (
            T2_T1,
            (1 + ((2 * gamma) / (gamma + 1)) * (M1**2 - 1))
            * ((2 + (gamma - 1) * M1**2) / ((gamma + 1) * M1**2)),
        ),
        #
        (
            delta_s,
            cp
            * sympy.ln(
                (1 + ((2 * gamma) / (gamma + 1)) * (M1**2 - 1))
                * ((2 + (gamma - 1) * M1**2) / ((gamma + 1) * M1**2))
            )
            - R * sympy.ln(1 + ((2 * gamma) / (gamma + 1)) * (M1**2 - 1)),
        ),
        (p02_p01, sympy.exp(-delta_s / R)),
        (
            p02_p1,
            (((gamma + 1) ** 2 * M1**2) / (4 * gamma * M1**2 - 2 * (gamma - 1)))
            ** (gamma / (gamma - 1))
            * ((1 - gamma + 2 * gamma * M1**2) / (gamma + 1)),
        ),
        (
            p01_p2,
            ((1 + ((gamma - 1) / 2) * M1**2) ** (gamma / (gamma - 1)))
            / (1 + ((2 * gamma) / (gamma + 1)) * (M1**2 - 1)),
        ),
        (
            p01_p2,
            (
                (((gamma + 1) ** 2 * M2**2) / (4 * gamma * M2**2 - 2 * (gamma - 1)))
                ** (gamma / (gamma - 1))
            )
            * ((1 - gamma + 2 * gamma * M2**2) / (gamma + 1)),
        ),
        #
        (At2_At1, p01_p02),
        #
        *ratio_curry(u1, u2, u1_u2, u2_u1),
        *ratio_curry(h1, h2, h1_h2, h2_h1),
        *ratio_curry(p1, p2, p1_p2, p2_p1),
        *ratio_curry(rho1, rho2, rho1_rho2, rho2_rho1),
        *ratio_curry(T1, T2, T1_T2, T2_T1),
        *ratio_curry(p01, p02, p01_p02, p02_p01),
        *ratio_curry(p01, p2, p01_p2, p2_p01),
        *ratio_curry(p02, p1, p02_p1, p1_p02),
        #
        *state_curry(
            (u1, a1, M1),
            (p1, p01, p1_p01, p01_p1),
            (rho1, rho01, rho1_rho01, rho01_rho1),
            (T1, T01, T1_T01, T01_T1),
        ),
        *state_curry(
            (u2, a2, M2),
            (p2, p02, p2_p02, p02_p2),
            (rho2, rho02, rho2_rho02, rho02_rho2),
            (T2, T02, T2_T02, T02_T2),
        ),
        #
        *specific_heat_curry(T1, (h1, e1)),
        *specific_heat_curry(T01, (h01, e01)),
        *specific_heat_curry(T2, (h2, e2)),
        *specific_heat_curry(T02, (h02, e02)),
        #
        *delta_curry(h1, h2, delta_h),
        *delta_curry(e1, e2, delta_e),
        *delta_curry(s1, s2, delta_s),
        #
        *ratio_curry(At1, At2, At1_At2, At2_At1),
    ]


class WeakObliqueShock(Hopper):
    initials = {
        beta: math.pi / 4,
    }

    equations = [
        (w1, w2),
        #
        (Mn1, M1 * sympy.sin(beta)),
        (M2, Mn2 / sympy.sin(beta - theta)),
        (Mn2**2, (1 + ((gamma - 1) / 2) * Mn1**2) / (gamma * Mn1**2 - (gamma - 1) / 2)),
        #
        (p2_p1, 1 + ((2 * gamma) / (gamma + 1)) * (Mn1**2 - 1)),
        (rho2_rho1, ((gamma + 1) * Mn1**2) / (2 + (gamma - 1) * Mn1**2)),
        (T2_T1, p2_p1 * rho1_rho2),
        #
        (
            sympy.tan(theta),
            2
            * sympy.cot(beta)
            * (
                (M1**2 * sympy.sin(beta) ** 2 - 1)
                / (M1**2 * (gamma + sympy.cos(2 * beta)) + 2)
            ),
        ),
        #
        (
            delta_s,
            cp
            * sympy.ln(
                (1 + ((2 * gamma) / (gamma + 1)) * (Mn1**2 - 1))
                * ((2 + (gamma - 1) * Mn1**2) / ((gamma + 1) * Mn1**2))
            )
            - R * sympy.ln(1 + ((2 * gamma) / (gamma + 1)) * (Mn1**2 - 1)),
        ),
        (p02_p01, sympy.exp(-delta_s / R)),
        #
        *specific_heat_curry(),
        #
        *ratio_curry(p1, p2, p1_p2, p2_p1),
        *ratio_curry(rho1, rho2, rho1_rho2, rho2_rho1),
        *ratio_curry(T1, T2, T1_T2, T2_T1),
        #
        *state_curry(
            (u1, a1, M1),
            (p1, p01, p1_p01, p01_p1),
            (rho1, rho01, rho1_rho01, rho01_rho1),
            (T1, T01, T1_T01, T01_T1),
        ),
        *state_curry(
            (u2, a2, M2),
            (p2, p02, p2_p02, p02_p2),
            (rho2, rho02, rho2_rho02, rho02_rho2),
            (T2, T02, T2_T02, T02_T2),
        ),
    ]


class StrongObliqueShock(Hopper):
    initials = {
        beta: math.pi / 2,
    }

    equations = WeakObliqueShock.equations


class SubsonicNozzle(Hopper):
    initials = {
        M: 2**-8,
    }

    equations = [
        (
            A_At**2,
            (1 / (M**2))
            * ((2 / (gamma + 1)) * (1 + ((gamma - 1) / 2) * M**2))
            ** ((gamma + 1) / (gamma - 1)),
        ),
        #
        (m_dot, rho * A * u),
        (m_dot, rhot * At * ut),
        #
        *ratio_curry(A, At, A_At, At_A),
        #
        *state_curry(
            (u, a, M),
            (p, p0, p_p0, p0_p),
            (rho, rho0, rho_rho0, rho0_rho),
            (T, T0, T_T0, T0_T),
        ),
        *state_curry(
            (ut, at, 1),
            (pt, p0, pt_p0, p0_pt),
            (rhot, rho0, rhot_rho0, rho0_rhot),
            (Tt, T0, Tt_T0, T0_Tt),
        ),
    ]


class SupersonicNozzle(Hopper):
    initials = {
        M: 2,
    }

    equations = SubsonicNozzle.equations


class PostShockNozzle(Hopper):
    initials = SubsonicNozzle.initials

    equations = [
        (Ae_At2, Ae_At1 / As_At1 * As_At2),
        (
            Ae_At2**2,
            (1 / (M**2))
            * ((2 / (gamma + 1)) * (1 + ((gamma - 1) / 2) * M**2))
            ** ((gamma + 1) / (gamma - 1)),
        ),
        #
        *state_curry(
            (u, a, M),
            (p, p0, p_p0, p0_p),
            (rho, rho0, rho_rho0, rho0_rho),
            (T, T0, T_T0, T0_T),
        ),
    ]


class PrandtlGlauertRule(Hopper):
    equations = [
        (Cp, Cp0 / sympy.sqrt(1 - M_inf**2)),
        (
            p_p_inf,
            ((1 + ((gamma - 1) / 2) * M_inf**2) / (1 + ((gamma - 1) / 2) * M**2))
            ** (gamma / (gamma - 1)),
        ),
        #
        *ratio_curry(p, p_inf, p_p_inf, p_inf_p),
    ]


class PrandtlGlauertCriticalRule(Hopper):
    equations = [
        (
            Cp_cr,
            (2 / (gamma * M_cr**2))
            * (
                ((1 + ((gamma - 1) / 2) * M_cr**2) / (1 + (gamma - 1) / 2))
                ** (gamma / (gamma - 1))
                - 1
            ),
        ),
    ]


class KarmanTsienRule(Hopper):
    equations = [
        (
            Cp,
            Cp0
            / (
                sympy.sqrt(1 - M_inf**2)
                + (M_inf**2 / (1 + sympy.sqrt(1 - M_inf**2))) * (Cp0 / 2)
            ),
        ),
    ]


class LaitoneRule(Hopper):
    equations = [
        (
            Cp,
            Cp0
            / (
                sympy.sqrt(1 - M_inf**2)
                + (
                    M_inf**2
                    * (1 + ((gamma - 1) / 2) * M_inf**2)
                    / (2 * sympy.sqrt(1 - M_inf**2))
                )
                * Cp0
            ),
        ),
    ]


class LinearizedFlatPlate(Hopper):
    equations = [
        (Cp2, -Cp3),
        (Cp3, (2 * alpha) / sympy.sqrt(M_inf**2 - 1)),
        #
        (Cl, (4 * alpha) / sympy.sqrt(M_inf**2 - 1)),
        (Cd, (4 * alpha**2) / sympy.sqrt(M_inf**2 - 1)),
        #
        (Cp2, (2 / (gamma * M_inf**2)) * (p2_p_inf - 1)),
        (Cp3, (2 / (gamma * M_inf**2)) * (p3_p_inf - 1)),
        #
        *ratio_curry(p2, p_inf, p2_p_inf, p_inf_p2),
        *ratio_curry(p3, p_inf, p3_p_inf, p_inf_p3),
    ]


class DiamondWedge(Hopper):
    equations = [
        #
        # these are my derivations; use at your own risk
        (t / c, sympy.tan(epsilon)),
        #
        (
            Cl,
            (2 / (gamma * M1**2))
            * (1 / (2 * sympy.cos(epsilon)))
            * (
                (p4_p1 - p3_p1) * sympy.cos(alpha + epsilon)
                + (p5_p1 - p2_p1) * sympy.cos(alpha - epsilon)
            ),
        ),
        (
            Cd,
            (2 / (gamma * M1**2))
            * (1 / (2 * sympy.cos(epsilon)))
            * (
                (p4_p1 - p3_p1) * sympy.sin(alpha + epsilon)
                + (p5_p1 - p2_p1) * sympy.sin(alpha - epsilon)
            ),
        ),
        #
        (p3_p1, p3_p2 * p2_p1),
        (p5_p1, p5_p4 * p4_p1),
        #
        *ratio_curry(p1, p3, p1_p3, p3_p1),
        *ratio_curry(p1, p4, p1_p4, p4_p1),
        *ratio_curry(p1, p5, p1_p5, p5_p1),
        *ratio_curry(p2, p3, p2_p3, p3_p2),
        *ratio_curry(p4, p5, p4_p5, p5_p4),
    ]


class LinearDiamondWedge(Hopper):
    equations = [
        #
        # these are my derivations; use at your own risk
        (alpha2, epsilon - alpha),
        (alpha4, epsilon + alpha),
        (alpha3, -2 * epsilon),
        (alpha5, -2 * epsilon),
        #
        (Cp2, (2 * alpha2) / sympy.sqrt(M1**2 - 1)),
        (Cp4, (2 * alpha4) / sympy.sqrt(M1**2 - 1)),
        (Cp3, (2 * alpha3) / sympy.sqrt(M1**2 - 1)),
        (Cp5, (2 * alpha5) / sympy.sqrt(M1**2 - 1)),
        (Cp2, (2 / (gamma * M1**2)) * (p2_p1 - 1)),
        (Cp4, (2 / (gamma * M1**2)) * (p4_p1 - 1)),
        (Cp3, (2 / (gamma * M1**2)) * (p3_p2 - 1)),
        (Cp5, (2 / (gamma * M1**2)) * (p5_p4 - 1)),
        #
        (p3_p1, p3_p2 * p2_p1),
        (p5_p1, p5_p4 * p4_p1),
        #
        (
            Cl,
            (2 / (gamma * M1**2))
            * (1 / (2 * sympy.cos(epsilon)))
            * (
                (p4_p1 - p3_p1) * sympy.cos(alpha + epsilon)
                + (p5_p1 - p2_p1) * sympy.cos(alpha - epsilon)
            ),
        ),
        (
            Cd,
            (2 / (gamma * M1**2))
            * (1 / (2 * sympy.cos(epsilon)))
            * (
                (p4_p1 - p3_p1) * sympy.sin(alpha + epsilon)
                + (p5_p1 - p2_p1) * sympy.sin(alpha - epsilon)
            ),
        ),
        #
        *ratio_curry(p1, p3, p1_p3, p3_p1),
        *ratio_curry(p1, p4, p1_p4, p4_p1),
        *ratio_curry(p1, p5, p1_p5, p5_p1),
        *ratio_curry(p2, p3, p2_p3, p3_p2),
        *ratio_curry(p4, p5, p4_p5, p5_p4),
    ]


class ExpansionWave(Hopper):
    initials = {
        M1: 2,
        M2: 2,
    }

    equations = [
        (
            nu1,
            sympy.sqrt((gamma + 1) / (gamma - 1))
            * sympy.atan(sympy.sqrt(((gamma - 1) / (gamma + 1)) * (M1**2 - 1)))
            - sympy.atan(sympy.sqrt(M1**2 - 1)),
        ),
        (
            nu2,
            sympy.sqrt((gamma + 1) / (gamma - 1))
            * sympy.atan(sympy.sqrt(((gamma - 1) / (gamma + 1)) * (M2**2 - 1)))
            - sympy.atan(sympy.sqrt(M2**2 - 1)),
        ),
        #
        (theta, nu2 - nu1),
        #
        (sympy.tan(mu1), 1 / sympy.sqrt(M1**2 - 1)),
        (sympy.tan(mu2), 1 / sympy.sqrt(M2**2 - 1)),
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
        #
        *ratio_curry(T1, T2, T1_T2, T2_T1),
        *ratio_curry(p1, p2, p1_p2, p2_p1),
        #
        *state_curry(
            (u1, a1, M1),
            (p1, p01, p1_p01, p01_p1),
            (rho1, rho01, rho1_rho01, rho01_rho1),
            (T1, T01, T1_T01, T01_T1),
        ),
        *state_curry(
            (u2, a2, M2),
            (p2, p02, p2_p02, p02_p2),
            (rho2, rho02, rho2_rho02, rho02_rho2),
            (T2, T02, T2_T02, T02_T2),
        ),
        #
        *specific_heat_curry(),
    ]


class Bernoulli(Hopper):
    equations = [
        (p1 + q1, p2 + q2),
        (rho1, rho2),
        (q1, (1 / 2) * rho1 * u1**2),
        (q2, (1 / 2) * rho2 * u2**2),
        #
        *state_curry(
            (u1, a1, M1),
            (p1, p0, p1_p0, p0_p1),
            (rho1, rho0, rho1_rho0, rho0_rho1),
            (T1, T0, T1_T0, T0_T1),
        ),
        *state_curry(
            (u2, a2, M2),
            (p2, p0, p2_p0, p0_p2),
            (rho2, rho0, rho2_rho0, rho0_rho2),
            (T2, T0, T2_T0, T0_T2),
        ),
    ]
