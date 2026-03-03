from solver import Solver
from registry import ur
from symbols import *
from equations import *
from units import *

air = {
    gamma: 7 / 5,
    R: 287.05 * ur.J / (ur.kg * ur.K),
    # rho0: 1.225 * ur.kg / ur.m**3,
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
            beta: 36.87 * ur.deg,
            M1: 3.5,
            p1: 1 * ur.atm,
        },
    )

    s2 = solver.solve(
        {
            **air,
            #
            beta: 36.87 * ur.deg,
            M1: s1[M2],
            p1: 1 * ur.atm,
        },
    )
