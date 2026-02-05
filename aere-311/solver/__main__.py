from solver import solve
from registry import ur
from symbols import *
from equations import isentropic_equations

if __name__ == "__main__":
    solve(
        isentropic_equations,
        {
            gamma: 7 / 5,
            R: 287.05 * ur.J / (ur.kg * ur.K),
            #
            p_inf: 0.61 * ur.atm,
            rho_inf: 0.819 * ur.kg / ur.m**3,
            u_inf: 300 * ur.m / ur.s,
            p: 0.550 * ur.atm,
        },
        [T_inf, a_inf, M_inf, p_0],
    )
