from pint import Quantity
from symbols import *
from registry import *
from units import *

knowns = {
    gamma: 7 / 5,
    R: 287.05 * ur.J / (ur.kg * ur.K),
    M: 2.6,
    T_0: 269.15 * ur.K,
    P: 1 * ur.atm,
}

knowns = {
    key: (value.to(base_units[key]).magnitude if isinstance(value, Quantity) else value)
    for key, value in knowns.items()
}
