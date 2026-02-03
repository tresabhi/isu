from symbols import *
from registry import *

base_units = {
    u: ur.m / ur.s,
    M: ur.dimensionless,
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
}

output_units = {
    P_0: ur.atm,
    P: ur.atm,
}
