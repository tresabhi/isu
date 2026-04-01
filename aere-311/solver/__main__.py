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
        *DANGEROUSLY_INCOMPLIANT_flat_plate_equations,
        # *prandtl_meyer_equations,
    ],
    output_units=durbin_output_units,
)

if __name__ == "__main__":
    solver.solve(
        {
            **air,
            alpha: 10 * ur.deg,
            M1: 7,
        }
    )
