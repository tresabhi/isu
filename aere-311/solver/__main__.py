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
        *state_equations,
        *entropy_equations,
        *isentropic_equations,
        # *isothermal_equations,
        *calorically_perfect_equations,
        *adiabatic_equations,
        *static_equations,
        # *sonic_equations,
        *bernoulli_equations,
    ],
    base_units=si_base_units,
    output_units=durbin_output_units,
)

if __name__ == "__main__":
    solver.solve(
        {
            **air,
            #
            p0: 1550 * ur.atm,
            T0: 1800 * ur.K,
            u1: 1.85 * ur.km / ur.s,
        },
    )
