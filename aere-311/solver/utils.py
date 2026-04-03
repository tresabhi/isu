from solver import Solver
from equations import *
from units import *


def flat_plate(knowns, output_units=durbin_output_units):
    expansion_wave_solver = Solver(
        equations=[
            *composite_equations,
            *shock_static_equations,
            *state_equations,
            *specific_heat_equations,
            *expansion_wave_equations,
        ],
        output_units=output_units,
    )
    oblique_shock_solver = Solver(
        equations=[
            *composite_equations,
            *shock_static_equations,
            *state_equations,
            *specific_heat_equations,
            *oblique_shock_equations,
        ],
        output_units=output_units,
    )
    flat_plate_solver = Solver(
        equations=[
            *flat_plate_equations,
        ],
        output_units=output_units,
    )

    top_knowns = {
        **knowns,
        theta: knowns[alpha],
    }
    bottom_knowns = {
        **knowns,
        theta: knowns[alpha],
    }

    top_solutions = expansion_wave_solver.solve(top_knowns)
    bottom_solutions = oblique_shock_solver.solve(bottom_knowns)

    flat_plate_knowns = {
        **knowns,
        p2_p1: top_solutions[p2_p1],
        p3_p1: bottom_solutions[p2_p1],
    }

    flat_plate_solutions = flat_plate_solver.solve(flat_plate_knowns)

    return flat_plate_solutions
