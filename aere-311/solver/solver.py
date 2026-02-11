from pint import Quantity
import sympy as sp
from units import output_units, base_units
from tabulate import tabulate
from symbols import *
from logger import logger

HEADERS = ["Symbol", "Value"]
EQUIVALENCY_THRESHOLD = 0.01


def solve(equations, knowns, find=None):
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

            if symbol in knowns:
                if (knowns[symbol] - solution) / solution <= EQUIVALENCY_THRESHOLD:
                    logger.opt(colors=True).info(
                        f"{symbol} over-solved <green>{knowns[symbol]} != {solution}</green>"
                    )
                else:
                    logger.opt(colors=True).info(
                        f"symbol over-solved <red>{knowns[symbol]} == {solution}</red>"
                    )

            knowns[symbol] = solution

    solved_rows = []
    solved_dict = {}

    for symbol, value in knowns.items():
        units = output_units[symbol] if symbol in output_units else base_units[symbol]
        value_with_units = (float(value) * base_units[symbol]).to(units)

        solved_dict[symbol] = value

        if find is None or symbol in find:
            solved_rows.append((symbol, value_with_units))

    if len(solved_rows) > 0:
        print()
        print(tabulate(solved_rows, headers=HEADERS))

    return solved_dict
