from sympy import Eq
from symbols import *
from knowns import *

equations = [
    Eq(a, (gamma * R * T) ** (1 / 2)),
    Eq(M, u / a),
    #
    Eq(gamma, c_p / c_v),
    Eq(R, c_p - c_v),
    #
    Eq(T_0 / T, (1 + ((gamma - 1) / 2) * M**2)),
    Eq(rho_0 / rho, (T_0 / T) ** (c_v / R)),
    Eq(P_0 / P, (T_0 / T) ** (c_p / R)),
    #
    Eq(T_T_0, T / T_0),
    Eq(rho_rho_0, rho / rho_0),
    Eq(P_P_0, P / P_0),
]

equations = [equation.subs(knowns) for equation in equations]
