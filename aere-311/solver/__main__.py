from solver import Solver
from registry import ur
from symbols import *
from equations import *

air = {
    gamma: 7 / 5,
    R: 287.05 * ur.J / (ur.kg * ur.K),
}

solver = Solver(equations=isentropic_equations)

if __name__ == "__main__":
    solver.solve(
        {
            **air,
            p: 1.2 * ur.atm,
            T: 300 * ur.K,
            u: 300 * ur.m / ur.s,
        },
    )
