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
        *state_equations,
        *calorically_perfect_equations,
        *nozzle_flow_equations,
    ],
    output_units=imperial_output_units,
)

if __name__ == "__main__":
    solver.solve(
        {
            **air,
            p0: 5 * ur.atm,
            T0: 520 * ur.rankine,
            A_star: 4.100 * ur.inch**2,
            A_sup_A_star: 2.193,
        }
    )
