from pint import Quantity
import sympy as sp
from tabulate import tabulate
from symbols import *
from logger import logger
from registry import ur

HEADERS = ["Symbol", "Value", "Units"]
EQUIVALENCY_THRESHOLD = 0.01


class Solver:
    log = logger.opt(colors=True)

    def __init__(self, equations, base_units, output_units, sig_figs=5):
        self.equations = [sp.Eq(*equation) for equation in equations]
        self.base_units = base_units
        self.output_units = {**base_units, **output_units}

        pass

    def solve(self, knowns, find=None):
        knowns = {
            key: (
                value.to(self.base_units[key]).magnitude
                if isinstance(value, Quantity)
                else value
            )
            for key, value in knowns.items()
        }

        last_knowns = 0
        subbed_equations = []

        while len(knowns) > last_knowns:
            last_knowns = len(knowns)
            subbed_equations = [equation.subs(knowns) for equation in self.equations]

            for equation in subbed_equations:
                symbols = equation.free_symbols

                if len(symbols) != 1:
                    continue

                [symbol] = symbols
                solution = None

                try:
                    solution = sp.nsolve(equation, symbol, 1)
                except:
                    self.log.info(
                        f"{symbol}: <yellow>numerical solving failed; trying symbolic...</yellow>"
                    )

                    solutions = sp.solve(equation, symbol)
                    solutions_count = len(solutions)

                    if solutions_count == 1:
                        solution = float(solutions[0])
                    else:
                        self.log.info(
                            f"{symbol}: <yellow>{solutions_count} solutions; using last...</yellow>"
                        )

                        solution = float(solutions[-1])

                if symbol in knowns:
                    if (knowns[symbol] - solution) / solution <= EQUIVALENCY_THRESHOLD:
                        self.log.info(
                            f"{symbol}: over-solved <green>{knowns[symbol]} == {solution}</green>"
                        )
                    else:
                        self.log.info(
                            f"{symbol}: over-solved <red>{knowns[symbol]} != {solution}</red>"
                        )

                knowns[symbol] = solution

        solved_rows = []
        solved_dict = {}

        for symbol, value in knowns.items():
            units = self.output_units[symbol]
            value_with_units = (float(value) * self.base_units[symbol]).to(units)

            solved_dict[symbol] = value

            if find is None or symbol in find:
                solved_rows.append(
                    (
                        f"{symbol}",
                        # f"{value_with_units.magnitude:.5g}",
                        value_with_units.magnitude,
                        (
                            None
                            if value_with_units.units == ur.dimensionless
                            else f"{value_with_units.units:~}"
                        ),
                    )
                )

        if len(solved_rows) > 0:
            solved_rows = sorted(solved_rows, key=lambda t: t[0].lower())

            print()
            print(tabulate(solved_rows, headers=HEADERS, disable_numparse=True))

        return solved_dict
