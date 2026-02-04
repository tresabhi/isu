from sympy import Eq
from symbols import *
from knowns import *

equations_isentropic = [
    # Eq(gamma, c_p / c_v),
    # Eq(R, c_p - c_v),
    #
    # Eq(p_0, rho_0 * R * T_0),
    Eq(p, rho * R * T),
    #
    # Eq(a_0, (gamma * R * T_0) ** (1 / 2)),
    Eq(a, (gamma * R * T) ** (1 / 2)),
    # #
    # Eq(M_0, u_0 / a_0),
    Eq(M, u / a),
    # #
    Eq(T_0 / T, (1 + ((gamma - 1) / 2) * M**2)),
    Eq(rho_0 / rho, (1 + (gamma - 1) / 2 * M**2) ** (1 / (gamma - 1))),
    Eq(p_0 / p, (1 + (gamma - 1) / 2 * M**2) ** (gamma / (gamma - 1))),
]

equations_bernoulli = [
    Eq(p_0 + (1 / 2) * rho_0 * u_0**2, p + (1 / 2) * rho * u**2),
    Eq(rho_0, rho),
]

equations = [*equations_isentropic]
equations = [equation.subs(knowns) for equation in equations]
