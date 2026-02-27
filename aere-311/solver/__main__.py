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
    output_units=ephemeral_units,
)

if __name__ == "__main__":
    solver.solve(
        {
            **air,
            #
            # beta: 30 * ur.deg,
            # M1: 4,
            # p1: 2.65e4 * ur.N / ur.m**2,
            # T1: 223.3 * ur.K,
            #
            beta: 30 * ur.deg,
            M1: 4,
            p1: 2.65e4 * ur.N / ur.m**2,
            T1: 223.3 * ur.K,
        },
    )
