from pint import Quantity
from symbols import *
from registry import *
from units import *

knowns = {
    gamma: 7 / 5,
    R: 287.05 * ur.J / (ur.kg * ur.K),
    #
    P_0: 0.61 * ur.atm,
    rho_0: 0.819 * ur.kg / ur.m**3,
    u_0: 300 * ur.m / ur.s,
    P: 0.460 * ur.atm,
}

knowns = {
    key: (value.to(base_units[key]).magnitude if isinstance(value, Quantity) else value)
    for key, value in knowns.items()
}
