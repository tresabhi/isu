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
        *state_equations,
        *entropy_equations,
        *isentropic_equations,
        # *isothermal_equations,
        *calorically_perfect_equations,
        *adiabatic_equations,
        *static_equations,
        *sonic_equations,
        # *bernoulli_equations,
    ],
    base_units=si_base_units,
    output_units=durbin_output_units,
)

if __name__ == "__main__":
    solver.solve(
        {
            **air,
            #
            rho1: 0.05 * ur.kg / ur.m**3,
            u1: 600 * ur.m / ur.s,
            p1: 5000 * ur.Pa,
            u2: 294.444 * ur.m / ur.s,
        },
    )
