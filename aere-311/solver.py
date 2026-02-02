from sympy import symbols, Eq, solve
import pint

ur = pint.UnitRegistry()

T_0, T = symbols("T_0 T")
u, M = symbols("u M")
gamma = symbols("gamma")

equations = [
    Eq(T_0 / T, (1 + ((gamma - 1) / 2) * M**2)),
]
knowns = {
    gamma: 7 / 5,
    M: 2.6,
    T_0: (269.15 * ur.K).magnitude,
}

equations = [eq.subs(knowns) for eq in equations]
sol = solve(equations, dict=True)

print(sol)
