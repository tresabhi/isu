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
    equations = [
        (p2_p1, rho2_rho1**gamma),
        (p2_p1, T2_T1 ** (gamma / (gamma - 1))),
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
    ]


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
    ]


class PerfectlyExpandedSubsonicNozzle(Hopper):
    initials = {
        M: 0.5,
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


class PerfectlyExpandedSupersonicNozzle(Hopper):
    initials = {
        M: 2,
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
