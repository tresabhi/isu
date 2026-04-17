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
        *area_mach_equations,
        *calorically_perfect_equations,
        *continuity_equations,
    ],
    output_units=imperial_output_units,
)

if __name__ == "__main__":
    s1 = solver.solve(
        {
            **air,
            M_sup: 3.100,
            T_sup: 518.670 * ur.rankine,
            p_sup: 2.1162e3 * ur.lbf / (ur.ft**2),
            rho_sup: 2.3769e-3 * ur.slug / (ur.ft**3),
            m_dot_sup: 1 * ur.slug / ur.s,
        }
    )

    # solver.equations = [
    # *ratio_equations,
    # *shock_static_equations,
    # *area_mach_equations,
    # ]

    # solver.solve(
    #     {
    #         **air,
    #         M_sup: s1[M1],
    #     }
    # )
