from solver import Solver
from registry import ur
from symbols import *
from equations import *
from units import *

air = {
    gamma: 7 / 5,
    R: 287.05 * ur.J / (ur.kg * ur.K),
    # cp: 0.847 * ur.kJ / (ur.kg * ur.K),
    # cv: 0.658 * ur.kJ / (ur.kg * ur.K),
}

solver = Solver(
    equations=[*composite_equations, *thermodynamic_equations, *isothermal_equations],
    base_units=si_base_units,
    output_units=durbin_output_units,
)

if __name__ == "__main__":
    solver.solve(
        {
            **air,
            #
            p1: 6000 * ur.Pa,
            rho1: 0.21 * ur.kg / ur.m**3,
            p2: 7500 * ur.Pa,
        },
    )
