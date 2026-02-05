from solver import solve
from registry import ur
from symbols import *
from equations import *

air = {
    gamma: 7 / 5,
    R: 287.05 * ur.J / (ur.kg * ur.K),
}

if __name__ == "__main__":
    s1 = solve(
        isentropic_equations_inf,
        {
            **air,
            p_inf: 0.61 * ur.atm,
            rho_inf: 0.819 * ur.kg / ur.m**3,
            u_inf: 300 * ur.m / ur.s,
        },
    )

    print(s1)

    solve(
        isentropic_equations,
        {
            gamma: 1.4,
            p_0: 1.0579259314780214 * ur.atm,
            p: 0.550 * ur.atm,
        },
    )
