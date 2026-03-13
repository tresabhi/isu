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
        *state_equations,
        *specific_heat_equations,
        *oblique_shocks,
    ],
    output_units=durbin_output_units,
)

if __name__ == "__main__":
    deflection1 = solver.solve(
        {
            **air,
            #
            M1: 3,
            T1: 280 * ur.K,
            p1: 3 * ur.atm,
            theta: 30.6 * ur.deg,
        }
    )

    solver.equations = [
        *composite_equations,
        *shock_static_equations,
        *state_equations,
        *specific_heat_equations,
        *prandtl_meyer_equations,
    ]

    deflection2 = solver.solve(
        {
            **air,
            #
            M1: deflection1[M2],
            T1: deflection1[T2],
            p1: deflection1[p2],
            theta: 30.6 * ur.deg,
        }
    )
