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
        # *continuity_equations,
        *composite_equations,
        *state_equations,
        # *entropy_equations,
        # *isentropic_equations,
        # *isothermal_equations,
        *calorically_perfect_equations,
        # *adiabatic_equations,
        *static_equations,
        # *bernoulli_equations,
        # *sub_sonic_equations,
        # *sonic_equations,
        # *super_sonic_equations,
        # *normal_shock_equations,
        *oblique_shocks,
    ],
    output_units=imperial_output_units,
)

if __name__ == "__main__":
    solver.solve(
        {
            **air,
            #
            M1: 1.5,
            d1: 567 * ur.ft,
        },
    )
