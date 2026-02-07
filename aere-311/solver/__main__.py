from solver import solve
from registry import ur
from symbols import *
from equations import *

air = {
    gamma: 7 / 5,
    R: 287.05 * ur.J / (ur.kg * ur.K),
}

sonic = {
    M_star: 1,
}

if __name__ == "__main__":
    solve(
        isentropic_equations,
        {
            **air,
            **sonic,
            #
            M: 0.3786,
            T: 300 * ur.K,
            rho: 1 * ur.kg / ur.m**3,
        },
    )
