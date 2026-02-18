from symbols import *
from registry import *

si_base_units = {
    d1: ur.m,
    d2: ur.m,
    A1: ur.m**2,
    A2: ur.m**2,
    V_dot1: ur.m**3 / ur.s,
    V_dot2: ur.m**3 / ur.s,
    m_dot: ur.kg / ur.s,
    m_dot1: ur.kg / ur.s,
    m_dot2: ur.kg / ur.s,
    F: ur.N,
    #
    R: ur.J / (ur.kg * ur.K),
    cp: ur.J / (ur.kg * ur.K),
    cv: ur.J / (ur.kg * ur.K),
    gamma: ur.dimensionless,
    #
    e1: ur.J / (ur.kg * ur.K),
    e2: ur.J / (ur.kg * ur.K),
    delta_e: ur.J / (ur.kg * ur.K),
    #
    h1: ur.J / ur.kg,
    h2: ur.J / ur.kg,
    delta_h: ur.J / ur.kg,
    h2_h1: ur.dimensionless,
    #
    s1: ur.J / (ur.kg * ur.K),
    s2: ur.J / (ur.kg * ur.K),
    delta_s: ur.J / (ur.kg * ur.K),
    #
    u1: ur.m / ur.s,
    u2: ur.m / ur.s,
    u2_u1: ur.dimensionless,
    #
    a0: ur.m / ur.s,
    a1: ur.m / ur.s,
    a2: ur.m / ur.s,
    a_star: ur.m / ur.s,
    #
    M1: ur.dimensionless,
    M2: ur.dimensionless,
    M1_star: ur.dimensionless,
    M2_star: ur.dimensionless,
    #
    p0: ur.Pa,
    p1: ur.Pa,
    p2: ur.Pa,
    p01: ur.Pa,
    p02: ur.Pa,
    p2_p1: ur.dimensionless,
    p0_p1: ur.dimensionless,
    p0_p2: ur.dimensionless,
    p02_p01: ur.dimensionless,
    p01_p1: ur.dimensionless,
    p01_p2: ur.dimensionless,
    p02_p1: ur.dimensionless,
    p02_p2: ur.dimensionless,
    p_star: ur.Pa,
    p_star_p0: ur.dimensionless,
    p_star_p1: ur.dimensionless,
    p_star_p2: ur.dimensionless,
    #
    rho0: ur.kg / ur.m**3,
    rho1: ur.kg / ur.m**3,
    rho2: ur.kg / ur.m**3,
    rho01: ur.kg / ur.m**3,
    rho02: ur.kg / ur.m**3,
    rho2_rho1: ur.dimensionless,
    rho0_rho1: ur.dimensionless,
    rho0_rho2: ur.dimensionless,
    rho01_rho1: ur.dimensionless,
    rho02_rho2: ur.dimensionless,
    rho_star: ur.kg / ur.m**3,
    rho_star_rho0: ur.dimensionless,
    rho_star_rho1: ur.dimensionless,
    rho_star_rho2: ur.dimensionless,
    #
    T0: ur.K,
    T1: ur.K,
    T2: ur.K,
    T01: ur.K,
    T02: ur.K,
    T2_T1: ur.dimensionless,
    T0_T1: ur.dimensionless,
    T0_T2: ur.dimensionless,
    T_star: ur.K,
    T_star_T0: ur.dimensionless,
    T_star_T1: ur.dimensionless,
    T_star_T2: ur.dimensionless,
}

durbin_output_units = {
    **si_base_units,
    #
    p0: ur.atm,
    p1: ur.atm,
    p2: ur.atm,
    p01: ur.atm,
    p02: ur.atm,
    p_star: ur.atm,
}

imperial_output_units = {
    **durbin_output_units,
    #
    T0: ur.rankine,
    T1: ur.rankine,
    T2: ur.rankine,
    T01: ur.rankine,
    T02: ur.rankine,
}
