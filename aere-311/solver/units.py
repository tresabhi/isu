from symbols import *
from registry import *

base_units = {
    u: ur.m / ur.s,
    u_0: ur.m / ur.s,
    M: ur.dimensionless,
    M_0: ur.dimensionless,
    a: ur.m / ur.s,
    a_0: ur.m / ur.s,
    #
    gamma: ur.dimensionless,
    c_p: ur.J / (ur.kg * ur.K),
    c_v: ur.J / (ur.kg * ur.K),
    R: ur.J / (ur.kg * ur.K),
    #
    T_0: ur.K,
    T: ur.K,
    rho_0: ur.kg / ur.m**3,
    rho: ur.kg / ur.m**3,
    P_0: ur.Pa,
    P: ur.Pa,
    #
    T_T_0: ur.dimensionless,
    rho_rho_0: ur.dimensionless,
    P_P_0: ur.dimensionless,
}

output_units = {
    P_0: ur.atm,
    P: ur.atm,
}
