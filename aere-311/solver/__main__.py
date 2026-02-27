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
        # *normal_shock_equations,
        # *sub_sonic_equations,
        # *sonic_equations,
        # *super_sonic_equations,
    ],
    output_units=durbin_output_units,
)

if __name__ == "__main__":
    solver.solve(
        {
            **air,
            #
            M1: 1.93,
            p0: 0.751 * ur.atm,
            p2: 0.5 * ur.atm,
            T2: 300 * ur.K,
        },
    )
