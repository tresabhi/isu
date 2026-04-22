import sympy
from registry import *


class Symbol(sympy.Symbol):
    def __new__(self, name: str, unit: str | None = None):
        symbol = sympy.Symbol.__new__(self, name, positive=True, imaginary=False)

        symbol.name = name
        symbol.unit = ur("dimensionless" if unit is None else unit)

        return symbol
