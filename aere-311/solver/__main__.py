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
            p: 1 * ur.atm,
            T: 230 * ur.K,
            M: 2.000,
        },
    )
