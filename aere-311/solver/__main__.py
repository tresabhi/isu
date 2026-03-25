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
        *shock_static_equations,
        *state_equations,
        *specific_heat_equations,
        *prandtl_meyer_equations,
    ],
    output_units=durbin_output_units,
)

if __name__ == "__main__":
    deflection1 = solver.solve(
        {
            **air,
            #
            M1: 1.5,
            theta: 14.5 * ur.deg,
        }
    )

    solver.equations = [
        *composite_equations,
        *shock_static_equations,
        *state_equations,
        *specific_heat_equations,
        *oblique_shocks,
    ]

    deflection2 = solver.solve(
        {
            **air,
            #
            M1: deflection1[M2],
            theta: deflection1[theta],
            T2: 300 * ur.K
        }
    )

    print('M2', deflection1[M2])

    _p03_p3 = deflection2[p02_p2]
    _p3_p2 = deflection2[p2_p1]
    _p2_p1 = deflection1[p2_p1]
    _p01_p1 = deflection1[p01_p1]

    print('p03/p01',_p03_p3*_p3_p2*_p2_p1*(1/_p01_p1))

    solver.equations = [
        *composite_equations,
        *shock_static_equations,
        *state_equations,
        *specific_heat_equations,
        *prandtl_meyer_equations,
    ]

    deflection1 = solver.solve(
        {
            **deflection1,
            T2: deflection2[T1]
        }
    )

    print("T1", deflection1[T1])

    print("nu1", deflection1[nu1])

