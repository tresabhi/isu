from symbols import *
from curries import *
from hopper import *


class State(Hopper):
    equations = [
        *state_curry(
            M,
            (p, p0, p_p0, p0_p),
            (rho, rho0, rho_rho0, rho0_rho),
            (T, T0, T_T0, T0_T),
        ),
    ]


class Isentropic(Hopper):
    initials = {
        M1: 2,
        M2: 2,
    }

    equations = [
        (p2_p1, rho2_rho1**gamma),
        (p2_p1, T2_T1 ** (gamma / (gamma - 1))),
        #
        *state_curry(
            M1,
            (p1, p0, p1_p0, p0_p1),
            (rho1, rho0, rho1_rho0, rho0_rho1),
            (T1, T0, T1_T0, T0_T1),
        ),
        *state_curry(
            M2,
            (p2, p0, p2_p0, p0_p2),
            (rho2, rho0, rho2_rho0, rho0_rho2),
            (T2, T0, T2_T0, T0_T2),
        ),
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
        (a1, sympy.sqrt((gamma * p1) / rho1)),
        (a2, sympy.sqrt((gamma * p2) / rho2)),
        (a1, sympy.sqrt(gamma * R * T1)),
        (a2, sympy.sqrt(gamma * R * T2)),
        #
        (M1, u1 / a1),
        (M2, u2 / a2),
        #
        *specific_heat_curry(),
        #
        *delta_curry(T01, T02, delta_T0),
        #
        *state_curry(
            M1,
            (p1, p01, p1_p01, p01_p1),
            (rho1, rho01, rho1_rho01, rho01_rho1),
            (T1, T01, T1_T01, T01_T1),
        ),
        *state_curry(
            M2,
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
        #
        *ratio_curry(u1, u2, u1_u2, u2_u1),
        *ratio_curry(h1, h2, h1_h2, h2_h1),
        *ratio_curry(p1, p2, p1_p2, p2_p1),
        *ratio_curry(rho1, rho2, rho1_rho2, rho2_rho1),
        *ratio_curry(T1, T2, T1_T2, T2_T1),
        *ratio_curry(p01, p02, p01_p02, p02_p01),
        #
        *state_curry(
            M1,
            (p1, p01, p1_p01, p01_p1),
            (rho1, rho01, rho1_rho01, rho01_rho1),
            (T1, T01, T1_T01, T01_T1),
        ),
        *state_curry(
            M2,
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
    ]


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
        *state_curry(
            M,
            (p, p0, p_p0, p0_p),
            (rho, rho0, rho_rho0, rho0_rho),
            (T, T0, T_T0, T0_T),
        ),
    ]


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
            M,
            (p, p0, p_p0, p0_p),
            (rho, rho0, rho_rho0, rho0_rho),
            (T, T0, T_T0, T0_T),
        ),
    ]


class SupersonicNozzle(Hopper):
    initials = {
        M: 2,
    }

    equations = SubsonicNozzle.equations


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
            M1,
            (p1, p01, p1_p01, p01_p1),
            (rho1, rho01, rho1_rho01, rho01_rho1),
            (T1, T01, T1_T01, T01_T1),
        ),
        *state_curry(
            M2,
            (p2, p02, p2_p02, p02_p2),
            (rho2, rho02, rho2_rho02, rho02_rho2),
            (T2, T02, T2_T02, T02_T2),
        ),
        #
        *specific_heat_curry(),
    ]


class ObliqueShock(Hopper):
    equations = [
        (w1, w2),
        #
        (Mn1, M1 * sympy.sin(beta_weak)),
        (Mn2**2, (1 + ((gamma - 1) / 2) * Mn1**2) / (gamma * Mn1**2 - (gamma - 1) / 2)),
        (rho2_rho1, ((gamma + 1) * Mn1**2) / (2 + (gamma - 1) * Mn1**2)),
        (p2_p1, 1 + ((2 * gamma) / (gamma + 1)) * (Mn1**2 - 1)),
        (T2_T1, p2_p1 / rho2_rho1),
        (M2, Mn2 / sympy.sin(beta_weak - theta)),
        #
        (sympy.tan(beta_weak), u1 / w1),
        (sympy.tan(beta_weak - theta), u2 / w2),
        (sympy.tan(beta_weak - theta) / sympy.tan(beta_weak), u2_u1),
        (u2_u1, 1 / rho2_rho1),
        (
            u2_u1,
            (2 + (gamma - 1) * M1**2 * sympy.sin(beta_weak) ** 2)
            / ((gamma + 1) * M1**2 * sympy.sin(beta_weak) ** 2),
        ),
        #
        (
            sympy.tan(theta),
            2
            * sympy.cot(beta_weak)
            * (
                (M1**2 * sympy.sin(beta_weak) ** 2 - 1)
                / (M1**2 * (gamma + sympy.cos(2 * beta_weak)) + 2)
            ),
        ),
        (
            sympy.tan(theta),
            2
            * sympy.cot(beta_strong)
            * (
                (M1**2 * sympy.sin(beta_strong) ** 2 - 1)
                / (M1**2 * (gamma + sympy.cos(2 * beta_strong)) + 2)
            ),
        ),
        (theta, beta_weak - sympy.atan((1 / rho2_rho1) * sympy.tan(beta_weak))),
        #
        *ratio_curry(p1, p2, p1_p2, p2_p1),
        *ratio_curry(rho1, rho2, rho1_rho2, rho2_rho1),
        *ratio_curry(T1, T2, T1_T2, T2_T1),
        #
        *state_curry(
            M1,
            (p1, p01, p1_p01, p01_p1),
            (rho1, rho01, rho1_rho01, rho01_rho1),
            (T1, T01, T1_T01, T01_T1),
        ),
        *state_curry(
            M2,
            (p2, p02, p2_p02, p02_p2),
            (rho2, rho02, rho2_rho02, rho02_rho2),
            (T2, T02, T2_T02, T02_T2),
        ),
        #
        *specific_heat_curry(),
    ]
