from solver import Solver
from registry import ur
from symbols import *
from equations import *
from units import *

air = {
    gamma: 7 / 5,
    R: 287.05 * ur.J / (ur.kg * ur.K),
}

solver = Solver(
    equations=[*isentropic_equations, *shock_equations],
    base_units=si_base_units,
    output_units=imperial_output_units,
)

if __name__ == "__main__":
    solver.solve(
        {
            **air,
            #
            p1: 1 * ur.atm,
            p2: 10.33 * ur.atm,
            T2: 1390 * ur.rankine,
        },
    )
