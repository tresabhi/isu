from symbols import *

state_space_bindings = {
    "generic": (
        M,
        #
        p,
        rho,
        T,
        #
        p0,
        rho0,
        T0,
        #
        p_p0,
        rho_rho0,
        T_T0,
        #
        A,
        At,
    ),
    1: (
        M1,
        #
        p1,
        rho1,
        T1,
        #
        p01,
        rho01,
        T01,
        #
        p1_p01,
        rho1_rho01,
        T1_T01,
        #
        A1,
        At1,
    ),
    2: (
        M2,
        #
        p2,
        rho2,
        T2,
        #
        p02,
        rho02,
        T02,
        #
        p2_p02,
        rho2_rho02,
        T2_T02,
        #
        A2,
        At2,
    ),
    "nozzle_post_shock": (A_At, p0, rho0, T0),
    "nozzle_post_shock_exit": (As_At2, p0, rho0, T0),
}


def to_state_space(knowns, state1, state2):
    space1 = state_space_bindings[state1]
    space2 = state_space_bindings[state2]

    transformed = {}

    for symbol, value in knowns.items():
        if symbol in space1:
            index = space1.index(symbol)
            transformed[space2[index]] = value

    return transformed
