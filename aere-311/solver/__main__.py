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
    ],
    output_units=durbin_output_units,
)

if __name__ == "__main__":
    solver.solve(
        {
            **air,
            p0: 1 * ur.atm,
            A_A_star: 1.53,
        }
    )

    solver.solve(
        {
            **air,
            p0: 1 * ur.atm,
            # p_sub: 0.154 * ur.atm,
            p_sup: 0.154 * ur.atm,
        }
    )
