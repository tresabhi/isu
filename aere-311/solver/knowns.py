from pint import Quantity
from symbols import *
from registry import *
from units import *

knowns = {
    gamma: 7 / 5,
    R: 287.05 * ur.J / (ur.kg * ur.K),
    #
    M: 0,
    T_0: 950 * ur.K,
    T: 600 * ur.K,
}

knowns = {
    key: (value.to(base_units[key]).magnitude if isinstance(value, Quantity) else value)
    for key, value in knowns.items()
}
