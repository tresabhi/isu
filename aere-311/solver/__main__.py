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
        # *oblique_shocks,
        *normal_shock_equations,
    ],
    output_units=durbin_output_units,
)

if __name__ == "__main__":
    s = solver.solve(
        {
            **air,
            #
            M1: 4,
            p1: 4 * ur.atm,
        },
    )

    print(s[p2] - s[p1])
