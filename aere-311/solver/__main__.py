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
    solver.equations = [
        *oblique_shock_equations,
    ]

    s1 = solver.solve(
        {
            **air,
            theta: 20 * ur.deg,
            beta_weak: 52.80 * ur.deg,
        }
    )

    solver.equations = [
        *ratio_equations,
        *shock_static_equations,
        *area_mach_equations,
    ]

    solver.solve(
        {
            **air,
            M_sup: s1[M1],
        }
    )
