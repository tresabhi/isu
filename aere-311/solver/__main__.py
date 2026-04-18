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
        *area_mach_equations,
        *calorically_perfect_equations,
        *continuity_equations,
        *state_equations,
    ],
    output_units=imperial_output_units,
)

if __name__ == "__main__":
    s1 = solver.solve(
        {
            **air,
            A_A_star: 1.616,
            p0: 1.0 * ur.atm,
        }
    )

    solver.solve(
        {
            **air,
            p_sub: 0.914 * ur.atm,
            p_sup: 0.914 * ur.atm,
            p0: 1.0 * ur.atm,
        }
    )
