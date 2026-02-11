from symbols import *
from registry import *

base_units = {
    u: ur.m / ur.s,
    u_0: ur.m / ur.s,
    u_inf: ur.m / ur.s,
    u_star: ur.m / ur.s,
    #
    a: ur.m / ur.s,
    a_0: ur.m / ur.s,
    a_inf: ur.m / ur.s,
    a_star: ur.m / ur.s,
    #
    M: ur.dimensionless,
    M_0: ur.dimensionless,
    M_inf: ur.dimensionless,
    M_star: ur.dimensionless,
    #
    p: ur.Pa,
    p_0: ur.Pa,
    p_inf: ur.Pa,
    p_star: ur.Pa,
    #
    q: ur.Pa,
    q_0: ur.Pa,
    q_inf: ur.Pa,
    q_star: ur.Pa,
    #
    rho: ur.kg / ur.m**3,
    rho_0: ur.kg / ur.m**3,
    rho_inf: ur.kg / ur.m**3,
    rho_star: ur.kg / ur.m**3,
    #
    T: ur.K,
    T_0: ur.K,
    T_inf: ur.K,
    T_star: ur.K,
    #
    gamma: ur.dimensionless,
    c_p: ur.J / (ur.kg * ur.K),
    c_v: ur.J / (ur.kg * ur.K),
    R: ur.J / (ur.kg * ur.K),
    #
    T_0_T: ur.dimensionless,
    T_0_T_inf: ur.dimensionless,
    T_0_T_star: ur.dimensionless,
    #
    p_0_p: ur.dimensionless,
    p_0_p_inf: ur.dimensionless,
    p_0_p_star: ur.dimensionless,
    #
    rho_0_rho: ur.dimensionless,
    rho_0_rho_inf: ur.dimensionless,
    rho_0_rho_star: ur.dimensionless,
}

output_units = {
    p: ur.atm,
    p_0: ur.atm,
    p_inf: ur.atm,
    p_star: ur.atm,
    #
    q: ur.atm,
    q_0: ur.atm,
    q_inf: ur.atm,
    q_star: ur.atm,
}
