from solver import solve
from registry import ur
from symbols import *
from equations import *

air = {
    gamma: 7 / 5,
    R: 287.05 * ur.J / (ur.kg * ur.K),
}

if __name__ == "__main__":
    solve(
        isentropic_equations,
        {
            **air,
            T_0: 519 * ur.rankine,
            u: 1360 * ur.ft / ur.s,
        },
    )
