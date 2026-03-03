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
    solver.solve(
        {
            **air,
            #
            theta: 22.5 * ur.deg,
            M1: 2.5,
            p1: 2 * ur.atm,
            T1: 280 * ur.K,
        },
    )
