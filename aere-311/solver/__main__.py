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
        *calorically_perfect_equations,
        *specific_heat_equations,
        *continuity_equations,
        *state_equations,
        *diffuser_equations,
        *normal_shock_equations,
    ],
    output_units=durbin_output_units,
)

if __name__ == "__main__":
    solver.solve(
        {
            **air,
            Me: 3,
            pB: 1 * ur.atm,
            eta_D: 1,
        }
    )
