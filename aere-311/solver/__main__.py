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
        # *state_equations,
        # *entropy_equations,
        # *isentropic_equations,
        # *isothermal_equations,
        *specific_heat_equations,
        # *calorically_perfect_equations,
        # *adiabatic_equations,
        # *static_equations,
        # *bernoulli_equations,
        # *sub_sonic_equations,
        # *sonic_equations,
        # *super_sonic_equations,
        # *shock_equations,
        # *normal_shock_equations,
        *oblique_shocks,
    ],
    output_units=ephemeral_units,
)

if __name__ == "__main__":
    solver.solve(
        {
            **air,
            #
            # beta: 30 * ur.deg,
            # M1: 4,
            # p1: 2.65e4 * ur.N / ur.m**2,
            # T1: 223.3 * ur.K,
            #
            M1: 2,
            p1: 1 * ur.atm,
            T1: 288 * ur.K,
            theta: 20 * ur.deg,
        },
    )
