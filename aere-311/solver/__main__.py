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
        *prandtl_meyer_equations,
    ],
    output_units=imperial_output_units,
)

if __name__ == "__main__":
    solver.solve(
        {
            **air,
            #
            M1: 2,
            p1: 0.7 * ur.atm,
            theta: 23.38 * ur.degree,
            T1: 550 * ur.rankine,
        }
    )
