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
        *quasi_1d_flow_equations,
    ],
    output_units=imperial_output_units,
)

if __name__ == "__main__":
    solver.solve(
        {
            **air,
            A2_A_star: 10.25,
            p02: 5 * ur.atm,
            T02: 600 * ur.rankine,
        }
    )
