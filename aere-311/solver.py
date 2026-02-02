from sympy import symbols, Eq, solve
from tabulate import tabulate
import pint

ur = pint.UnitRegistry(system="mks")

T_0, T = symbols("T_0 T")
rho_0, rho = symbols("rho_0 rho")
P_0, P = symbols("rho_0 rho")

u, M = symbols("u M")
gamma = symbols("gamma")
c_p, c_v, R = symbols("c_p c_v R")

equations = [
    Eq(T_0 / T, (1 + ((gamma - 1) / 2) * M**2)),
    Eq(rho_0 / rho, (T_0 / T) ** (c_v / R)),
    Eq(P_0 / P, (T_0 / T) ** (c_p / R)),
]

knowns = {
    gamma: 7 / 5,
    M: 2.6,
    T_0: 269.15 * ur.K,
}

knowns = {key: value.to_base_units().magnitude for key, value in knowns.items()}

equations = [equation.subs(knowns) for equation in equations]
solutions = solve(equations)

print(tabulate(solutions.items()))
