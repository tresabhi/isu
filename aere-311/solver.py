from sympy import symbols, Eq, solve, Float, Mul
from tabulate import tabulate
from pint import UnitRegistry, Quantity

ur = UnitRegistry()

u, M = symbols("u M")

gamma = symbols("gamma")
c_p, c_v, R = symbols("c_p c_v R")

T_0, T = symbols("T_0 T")
rho_0, rho = symbols("rho_0 rho")
P_0, P = symbols("P_0 P")

equations = [
    Eq(gamma, c_p / c_v),
    Eq(R, c_p - c_v),
    Eq(T_0 / T, (1 + ((gamma - 1) / 2) * M**2)),
    Eq(rho_0 / rho, (T_0 / T) ** (c_v / R)),
    Eq(P_0 / P, (T_0 / T) ** (c_p / R)),
]

base_units = {
    u: ur.m / ur.s,
    M: ur.dimensionless,
}
base_units = {
    **base_units,
    gamma: ur.dimensionless,
    c_p: ur.J / (ur.kg * ur.K),
    c_v: ur.J / (ur.kg * ur.K),
    R: ur.J / (ur.kg * ur.K),
}
base_units = {
    **base_units,
    T_0: ur.K,
    T: ur.K,
    rho_0: ur.kg / ur.m**3,
    rho: ur.kg / ur.m**3,
    P_0: ur.Pa,
    P: ur.Pa,
}

output_units = {
    P_0: ur.atm,
}

knowns = {
    gamma: 7 / 5,
    R: 287.05 * ur.J / (ur.kg * ur.K),
}
knowns = {
    **knowns,
    M: 2.6,
    T_0: 269.15 * ur.K,
    P: 1 * ur.atm,
}
knowns = {
    key: (value.to(base_units[key]).magnitude if isinstance(value, Quantity) else value)
    for key, value in knowns.items()
}

equations = [equation.subs(knowns) for equation in equations]
solution_sets = solve(equations)

for index, solutions in enumerate(solution_sets):
    knowns = {}
    unknowns = {}

    for key, value in solutions.items():
        if isinstance(value, Float):
            units = output_units[key] if key in output_units else base_units[key]
            knowns[key] = (float(value) * base_units[key]).to(units)
        elif isinstance(value, Mul):
            unknowns[key] = value
        else:
            raise Exception(f"Unknown solution type: {type(value)}")

    if len(knowns) > 0:
        print(f"Set {index + 1} knowns:")
        print(tabulate(knowns.items()), end="\n\n")

    if len(unknowns) > 0:
        print(f"Set {index + 1} unknowns:")
        print(tabulate(unknowns.items()), end="\n\n")
