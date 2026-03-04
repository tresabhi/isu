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
    output_units=imperial_output_units,
)

if __name__ == "__main__":
    incident = solver.solve(
        {
            **air,
            #
            theta: 18.2 * ur.deg,
            M1: 3.2,
            p1: 3 * ur.atm,
            T1: 570 * ur.rankine,
        }
    )

    reflected = solver.solve(
        {
            **air,
            #
            theta: 18.2 * ur.deg,
            M1: incident[M2],
            p1: incident[p2],
            T1: incident[T2],
        }
    )

    phi = reflected[beta_weak] - reflected[theta]

    print(phi)
