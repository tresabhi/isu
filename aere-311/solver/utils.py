from solver import Solver
from equations import *
from units import *


def flat_plate(knowns, output_units=durbin_output_units):
    expansion_wave_solver = Solver(
        equations=[
            *ratio_equations,
            *shock_static_equations,
            *state_equations,
            *specific_heat_equations,
            *expansion_wave_equations,
        ],
        output_units=output_units,
    )
    oblique_shock_solver = Solver(
        equations=[
            *ratio_equations,
            *shock_static_equations,
            *state_equations,
            *specific_heat_equations,
            *oblique_shock_equations,
        ],
        output_units=output_units,
    )
    flat_plate_solver = Solver(
        equations=[
            *dynamic_equations,
            *flat_plate_equations,
        ],
        output_units=output_units,
    )

    top_knowns = {
        **knowns,
        theta: knowns.get(alpha),
    }
    bottom_knowns = {
        **knowns,
        theta: knowns.get(alpha),
    }

    top_solutions = expansion_wave_solver.solve(top_knowns)
    bottom_solutions = oblique_shock_solver.solve(bottom_knowns)

    flat_plate_knowns = {
        **knowns,
        p2: top_solutions.get(p2),
        p3: bottom_solutions.get(p2),
        p2_p1: top_solutions.get(p2_p1),
        p3_p1: bottom_solutions.get(p2_p1),
    }

    flat_plate_solutions = flat_plate_solver.solve(flat_plate_knowns)

    return flat_plate_solutions


def diamond_wedge(knowns, output_units=durbin_output_units):
    expansion_wave_solver = Solver(
        equations=[
            *ratio_equations,
            *shock_static_equations,
            *state_equations,
            *specific_heat_equations,
            *expansion_wave_equations,
        ],
        output_units=output_units,
    )
    oblique_shock_solver = Solver(
        equations=[
            *ratio_equations,
            *shock_static_equations,
            *state_equations,
            *specific_heat_equations,
            *oblique_shock_equations,
        ],
        output_units=output_units,
    )
    diamond_wedge_solver = Solver(
        equations=[
            *diamond_wedge_equations,
        ],
        output_units=output_units,
    )

    knowns_superset = diamond_wedge_solver.solve(knowns)

    theta_top_left = -knowns_superset[alpha] + knowns_superset[epsilon]
    theta_bottom_left = knowns_superset[alpha] + knowns_superset[epsilon]
    theta_top_right = 2 * knowns_superset[epsilon]
    theta_bottom_right = 2 * knowns_superset[epsilon]

    if theta_top_left < 0:
        top_left_solutions = expansion_wave_solver.solve(
            {
                **knowns_superset,
                theta: -theta_top_left,
            }
        )
    else:
        top_left_solutions = oblique_shock_solver.solve(
            {
                **knowns_superset,
                theta: theta_top_left,
            }
        )

    if theta_bottom_left < 0:
        bottom_left_solutions = expansion_wave_solver.solve(
            {
                **knowns_superset,
                theta: -theta_bottom_left,
            }
        )
    else:
        bottom_left_solutions = oblique_shock_solver.solve(
            {
                **knowns_superset,
                theta: theta_bottom_left,
            }
        )

    top_right_solutions = expansion_wave_solver.solve(
        {
            **knowns_superset,
            theta: theta_top_right,
            M1: top_left_solutions.get(M2),
            p1: top_left_solutions.get(p2),
            T1: top_left_solutions.get(T2),
            rho1: top_left_solutions.get(rho2),
        }
    )
    bottom_right_solutions = expansion_wave_solver.solve(
        {
            **knowns_superset,
            theta: theta_bottom_right,
            M1: bottom_left_solutions.get(M2),
            p1: bottom_left_solutions.get(p2),
            T1: bottom_left_solutions.get(T2),
            rho1: bottom_left_solutions.get(rho2),
        }
    )

    diamond_wedge_solver.solve(
        {
            **knowns_superset,
            p2_p1: top_left_solutions.get(p2_p1),
            p3_p2: top_right_solutions.get(p2_p1),
            p4_p1: bottom_left_solutions.get(p2_p1),
            p5_p4: bottom_right_solutions.get(p2_p1),
        }
    )


def nozzle_shock(Ae_At, p0, gamma=1.4, R=287.05):
    step = (Ae_At - 1) / 2
    A2_A1_star = 1 + step
    A2_A1_star = 1.204

    # pe = pe_p02 * p02_p01 * p01

    _M = sp.symbols("M1")
    M1 = sp.nsolve(
        (1 / (_M**2))
        * ((2 / (gamma + 1)) * (1 + ((gamma - 1) / 2) * _M**2))
        ** ((gamma + 1) / (gamma - 1))
        - A2_A1_star**2,
        2,
    )
    M2 = math.sqrt((1 + ((gamma - 1) / 2) * M1**2) / (gamma * M1**2 - (gamma - 1) / 2))

    cp = (gamma * R) / (gamma - 1)
    delta_s = cp * math.log(
        (1 + ((2 * gamma) / (gamma + 1)) * (M1**2 - 1))
        * ((2 + (gamma - 1) * M1**2) / ((gamma + 1) * M1**2))
    ) - R * sp.ln(1 + ((2 * gamma) / (gamma + 1)) * (M1**2 - 1))
    p02_p01 = math.exp(-delta_s / R)

    At_A2 = 1 / A2_A1_star
    A2_A2_star = math.sqrt(
        (1 / (M2**2))
        * ((2 / (gamma + 1)) * (1 + ((gamma - 1) / 2) * M2**2))
        ** ((gamma + 1) / (gamma - 1))
    )
    Ae_A2_star = Ae_At * At_A2 * A2_A2_star
    Me = sp.nsolve(
        (1 / (_M**2))
        * ((2 / (gamma + 1)) * (1 + ((gamma - 1) / 2) * _M**2))
        ** ((gamma + 1) / (gamma - 1))
        - Ae_A2_star**2,
        0.001,
    )
    p02_pe = (1 + ((gamma - 1) / 2) * Me**2) ** (gamma / (gamma - 1))

    pe_p02 = 1 / p02_pe
    pe = pe_p02 * p02_p01 * p0

    print(pe)
