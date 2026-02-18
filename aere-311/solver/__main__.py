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
        *continuity_equations,
        *composite_equations,
        *state_equations,
        # *entropy_equations,
        # *isentropic_equations,
        # *isothermal_equations,
        *calorically_perfect_equations,
        *adiabatic_equations,
        *static_equations,
        *sonic_equations,
        # *bernoulli_equations,
        # *normal_shock_equations,
    ],
    base_units=si_base_units,
    output_units=si_base_units,
)

if __name__ == "__main__":
    solver.solve(
        {
            **air,
            #
            A1: 0.6 * ur.m**2,
            A2: 1 * ur.m**2,
            rho1: 0.1 * ur.kg / ur.m**3,
            T1: 300 * ur.K,
            u1: 277.775 * ur.m / ur.s,
            u2: 131.540 * ur.m / ur.s,
        },
    )
