from symbols import *
from registry import *

si_base_units = {
    u: ur.m / ur.s,
    u0: ur.m / ur.s,
    u1: ur.m / ur.s,
    u2: ur.m / ur.s,
    u_inf: ur.m / ur.s,
    u_star: ur.m / ur.s,
    u2_u1: ur.dimensionless,
    #
    a: ur.m / ur.s,
    a0: ur.m / ur.s,
    a1: ur.m / ur.s,
    a2: ur.m / ur.s,
    a_inf: ur.m / ur.s,
    a_star: ur.m / ur.s,
    #
    M: ur.dimensionless,
    M0: ur.dimensionless,
    M1: ur.dimensionless,
    M2: ur.dimensionless,
    M_inf: ur.dimensionless,
    M_star: ur.dimensionless,
    #
    p: ur.Pa,
    p0: ur.Pa,
    p1: ur.Pa,
    p2: ur.Pa,
    p_inf: ur.Pa,
    p_star: ur.Pa,
    #
    q: ur.Pa,
    q0: ur.Pa,
    q1: ur.Pa,
    q2: ur.Pa,
    q_inf: ur.Pa,
    q_star: ur.Pa,
    #
    rho: ur.kg / ur.m**3,
    rho0: ur.kg / ur.m**3,
    rho1: ur.kg / ur.m**3,
    rho2: ur.kg / ur.m**3,
    rho_inf: ur.kg / ur.m**3,
    rho_star: ur.kg / ur.m**3,
    #
    T: ur.K,
    T0: ur.K,
    T1: ur.K,
    T2: ur.K,
    T_inf: ur.K,
    T_star: ur.K,
    T2_T1: ur.dimensionless,
    #
    gamma: ur.dimensionless,
    c_p: ur.J / (ur.kg * ur.K),
    c_v: ur.J / (ur.kg * ur.K),
    R: ur.J / (ur.kg * ur.K),
    h0: ur.J / ur.kg,
    h1: ur.J / ur.kg,
    h2: ur.J / ur.kg,
    #
    T0_T: ur.dimensionless,
    T0_T_inf: ur.dimensionless,
    T0_T_star: ur.dimensionless,
    #
    p0_p: ur.dimensionless,
    p0_p_inf: ur.dimensionless,
    p0_p_star: ur.dimensionless,
    p2_p1: ur.dimensionless,
    #
    rho0_rho: ur.dimensionless,
    rho0_rho_inf: ur.dimensionless,
    rho0_rho_star: ur.dimensionless,
    rho2_rho1: ur.dimensionless,
}

durbin_output_units = {
    p: ur.atm,
    p0: ur.atm,
    p1: ur.atm,
    p2: ur.atm,
    p_inf: ur.atm,
    p_star: ur.atm,
    #
    q: ur.atm,
    q0: ur.atm,
    q1: ur.atm,
    q2: ur.atm,
    q_inf: ur.atm,
    q_star: ur.atm,
}
