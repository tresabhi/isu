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
    equations=[
        *composite_equations,
        *shock_static_equations,
        *oblique_shocks,
    ],
    output_units=durbin_output_units,
)

if __name__ == "__main__":
    s1 = solver.solve(
        {
            **air,
            #
            M1: 4,
            p1: 4 * ur.atm,
            theta: 25.3 * ur.deg,
        }
    )

    s2 = solver.solve(
        {
            **air,
            #
            M1: s1[M2],
            p1: s1[p2],
            theta: 20 * ur.deg,
        }
    )

    solver.equations = [
        *composite_equations,
        *shock_static_equations,
        *normal_shock_equations,
    ]

    s3 = solver.solve(
        {
            **air,
            #
            M1: s2[M2],
            p1: s2[p2],
        }
    )

    print(s1[p01] - s3[p02])

    solver.clean_solutions_dir()
