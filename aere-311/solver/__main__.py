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
            M_sub: 1,
            M_sup: 1,
            p0: 1 * ur.atm,
        }
    )

    solver.solve(
        {
            **air,
            A_A_star: 1.53,
            p0: 1 * ur.atm,
        }
    )

    solver.solve(
        {
            **air,
            p_sub: 0.94 * ur.atm,
            p_sup: 0.94 * ur.atm,
            p0: 1 * ur.atm,
        }
    )
