from solver import solve
from registry import ur
from symbols import *
from equations import *

air = {
    gamma: 7 / 5,
    R: 287.05 * ur.J / (ur.kg * ur.K),
}

sonic = {
    M_star: 1,
}

if __name__ == "__main__":
    find = [M, p_0_p, rho_0_rho, T_0_T]

    solve(isentropic_equations, {**air, M: 0.61}, find)
    solve(isentropic_equations, {**air, rho_0_rho: 9.9}, find)
    solve(isentropic_equations, {**air, p_0_p: 1.5}, find)
    solve(isentropic_equations, {**air, T_0_T: 1.01}, find)
