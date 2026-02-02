from sympy import symbols, Eq, solve
from tabulate import tabulate
from pint import UnitRegistry, Quantity

ur = UnitRegistry(system="mks")

u, M = symbols("u M")

gamma = symbols("gamma")
c_p, c_v, R = symbols("c_p c_v R")

T_0, T = symbols("T_0 T")
rho_0, rho = symbols("rho_0 rho")
P_0, P = symbols("rho_0 rho")

equations = [
    Eq(T_0 / T, (1 + ((gamma - 1) / 2) * M**2)),
    Eq(rho_0 / rho, (T_0 / T) ** (c_v / R)),
    Eq(P_0 / P, (T_0 / T) ** (c_p / R)),
]
units = {
    u: ur.m / ur.s,
    M: ur.dimensionless,
}
units = {
    **units,
    gamma: ur.dimensionless,
    c_p: ur.J / (ur.kg * ur.K),
    c_v: ur.J / (ur.kg * ur.K),
    R: ur.J / (ur.kg * ur.K),
}
units = {
    **units,
    T_0: ur.K,
    T: ur.K,
    rho_0: ur.kg / ur.m**3,
    rho: ur.kg / ur.m**3,
    P_0: ur.Pa,
    P: ur.Pa,
}

knowns = {
    gamma: 7 / 5,
    M: 2.6,
    T_0: 269.15 * ur.K,
}

knowns = {
    key: (value.to(units[key]).magnitude if isinstance(value, Quantity) else value)
    for key, value in knowns.items()
}

equations = [equation.subs(knowns) for equation in equations]
solutions = solve(equations)

for index, solution in enumerate(solutions):
    print(f"Solution set {index + 1}")
    print(tabulate(solution.items()), end="\n\n")
