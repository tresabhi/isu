from pint import Quantity
import sympy as sp
from units import output_units, base_units
from tabulate import tabulate
from symbols import *

headers = ["Symbol", "Value"]


def solve(equations, knowns):
    knowns = {
        key: (
            value.to(base_units[key]).magnitude
            if isinstance(value, Quantity)
            else value
        )
        for key, value in knowns.items()
    }

    last_knowns = 0
    subbed_equations = []

    while len(knowns) > last_knowns:
        last_knowns = len(knowns)
        subbed_equations = [equation.subs(knowns) for equation in equations]

        for equation in subbed_equations:
            symbols = equation.free_symbols

            if len(symbols) != 1:
                continue

            [symbol] = symbols
            solution = sp.nsolve(equation, symbol, 1)
            knowns[symbol] = solution

    solved = []

    for symbol, value in knowns.items():
        units = output_units[symbol] if symbol in output_units else base_units[symbol]
        solved.append((symbol, (float(value) * base_units[symbol]).to(units)))

    if len(solved) > 0:
        print(tabulate(solved, headers=headers))

    return solved
