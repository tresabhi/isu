from symbols import *
from hoppers import *


def diamond_wedge(knowns):
    knowns_superset = DiamondWedge(knowns).solve()

    theta_top_left = -knowns_superset[alpha] + knowns_superset[epsilon]
    theta_bottom_left = knowns_superset[alpha] + knowns_superset[epsilon]
    theta_top_right = 2 * knowns_superset[epsilon]
    theta_bottom_right = 2 * knowns_superset[epsilon]

    if theta_top_left < 0:
        top_left_solutions = ExpansionWave(
            {
                **knowns_superset,
                theta: -theta_top_left,
            }
        ).solve()
    else:
        top_left_solutions = ObliqueShock(
            {
                **knowns_superset,
                theta: theta_top_left,
            }
        ).solve()

    if theta_bottom_left < 0:
        bottom_left_solutions = ExpansionWave(
            {
                **knowns_superset,
                theta: -theta_bottom_left,
            }
        ).solve()
    else:
        bottom_left_solutions = ObliqueShock(
            {
                **knowns_superset,
                theta: theta_bottom_left,
            }
        ).solve()

    top_right_solutions = ExpansionWave(
        {
            **knowns_superset,
            theta: theta_top_right,
            M1: top_left_solutions.get(M2),
            p1: top_left_solutions.get(p2),
            T1: top_left_solutions.get(T2),
            rho1: top_left_solutions.get(rho2),
        }
    ).solve()
    bottom_right_solutions = ExpansionWave(
        {
            **knowns_superset,
            theta: theta_bottom_right,
            M1: bottom_left_solutions.get(M2),
            p1: bottom_left_solutions.get(p2),
            T1: bottom_left_solutions.get(T2),
            rho1: bottom_left_solutions.get(rho2),
        }
    ).solve()

    return DiamondWedge(
        {
            **knowns_superset,
            p2_p1: top_left_solutions.get(p2_p1),
            p3_p2: top_right_solutions.get(p2_p1),
            p4_p1: bottom_left_solutions.get(p2_p1),
            p5_p4: bottom_right_solutions.get(p2_p1),
        }
    ).solve()
