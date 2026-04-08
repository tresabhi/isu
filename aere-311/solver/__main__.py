from solver import Solver
from registry import ur
from symbols import *
from equations import *
from units import *
from utils import *

air = {
    gamma: 7 / 5,
    R: 287.05 * ur.J / (ur.kg * ur.K),
}

solver = Solver(
    equations=[
        *ratio_equations,
        *shock_static_equations,
        *nozzle_flow_equations,
    ],
    output_units=durbin_output_units,
)

if __name__ == "__main__":
    s1 = solver.solve(
        {
            **air,
            M_sub: 0.32,
            A: 2.8 * ur.m**2,
        }
    )

    solver.solve(
        {
            **air,
            A_star: 1.311 * ur.m**2,
            A: s1[A],
        }
    )
