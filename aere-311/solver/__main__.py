from solver import Solver
from registry import ur
from symbols import *
from equations import *
from units import *

air = {
    # gamma: 7 / 5,
    # R: 287.05 * ur.J / (ur.kg * ur.K),
    cp: 0.847 * ur.kJ / (ur.kg * ur.K),
    cv: 0.658 * ur.kJ / (ur.kg * ur.K),
}

solver = Solver(
    equations=[
        *composite_equations,
        *thermodynamic_equations,
        # *isentropic_equations,
    ],
    base_units=si_base_units,
    output_units=durbin_output_units,
)

if __name__ == "__main__":
    solver.solve(
        {
            **air,
            #
            T1: 288 * ur.K,
            p1: 1 * ur.atm,
            T2: 640 * ur.K,
            p2: 9 * ur.atm,
        },
    )
