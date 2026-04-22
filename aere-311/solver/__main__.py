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
    # solver.solve(
    #     {
    #         **air,
    #     }
    # )

    nozzle_exit(
        {
            **air,
            p0: 2 * ur.atm,
            pe: 0.7 * ur.atm,
            # Me: 0.4,
            Ae_At: 4.005,
        }
    )

    print(8 / 1.5704278990627394)

    # solver.solve(
    #     {
    #         **air,
    #         M1: 2.79196540004919,
    #         M2: 0.4887410111514834,
    #     }
    # )

    solver.equations = [
        *ratio_equations,
        *shock_static_equations,
        *calorically_perfect_equations,
        *specific_heat_equations,
        *continuity_equations,
        *state_equations,
        *diffuser_equations,
        *area_mach_equations,
    ]

    solver.solve(
        {
            **air,
            A_A_star: 7 / 5.094153004270078,
        }
    )
