from solver import solve
from registry import ur
from symbols import *
from equations import *

air = {
    gamma: 7 / 5,
    R: 287.05 * ur.J / (ur.kg * ur.K),
}

if __name__ == "__main__":
    isentropic_solution = solve(
        isentropic_equations,
        {
            **air,
            p_inf: 0.61 * ur.atm,
            rho_inf: 0.819 * ur.kg / ur.m**3,
            u_inf: 300 * ur.m / ur.s,
            p: 0.550 * ur.atm,
        },
    )

    bernoulli_solution = solve(
        bernoulli_equations,
        {
            **air,
            p_inf: 0.61 * ur.atm,
            rho_inf: 0.819 * ur.kg / ur.m**3,
            u_inf: 300 * ur.m / ur.s,
            p: 0.550 * ur.atm,
        },
    )

    percentage_change = 100 * (
        (bernoulli_solution[u] - isentropic_solution[u]) / isentropic_solution[u]
    )

    print("percentage_change", percentage_change)
