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

    def solve(self, original_knowns, find=None):
        knowns = {}

        for key, value in original_knowns.items():
            if key not in self.base_units:
                raise SyntaxError(f"{key} has no base units")

            base = self.base_units[key]

            if isinstance(value, Quantity):
                knowns[key] = value.to(self.base_units[key]).magnitude
            elif base == ur.dimensionless:
                knowns[key] = value
            else:
                raise TypeError(f"Expected units for {key} in input")

        last_knowns = 0
        subbed_equations = []
        solved_last_using = {}

        while len(knowns) > last_knowns:
            last_knowns = len(knowns)
            subbed_equations = [equation.subs(knowns) for equation in self.equations]
            index = 0

            for equation in subbed_equations:
                original_equation = self.equations[index]
                symbols = equation.free_symbols
                index += 1

                if len(symbols) != 1:
                    continue

                [symbol] = symbols
                solution = None

                try:
                    solution = sp.nsolve(equation, symbol, 1)
                except:
                    self.log.info(
                        f"{symbol}: <yellow>numerical solving failed; trying symbolic...</yellow>\n\t{original_equation.lhs} = {original_equation.rhs}\n\t{equation.lhs} = {equation.rhs}"
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
                            f"{symbol}: <green>over-solved</green> {knowns[symbol]} == {solution}"
                        )
                    else:
                        last_equation = solved_last_using[symbol]
                        self.log.info(
                            f"{symbol}: <red>over-solved</red> {knowns[symbol]} != {solution}\n\t({last_equation.lhs} = {last_equation.rhs})\n\t({original_equation.lhs} = {original_equation.rhs})"
                        )

                knowns[symbol] = solution
                solved_last_using[symbol] = original_equation

        solved_rows = []
        solved_dict = {}

        for symbol, value in knowns.items():
            units = self.output_units[symbol]
            value_with_units = (float(value) * self.base_units[symbol]).to(units)

            solved_dict[symbol] = value

            if find is None or symbol in find:
                solved_rows.append(
                    (
                        symbol,
                        value_with_units.magnitude,
                        (
                            None
                            if value_with_units.units == ur.dimensionless
                            else f"{value_with_units.units:~}"
                        ),
                    )
                )

        if len(solved_rows) > 0:
            solved_rows = sorted(solved_rows, key=lambda t: f"{t[0]}".lower())
            table = tabulate(solved_rows, headers=HEADERS, disable_numparse=True)

            print()
            index = -2
            for line in table.splitlines():
                if index < 0:
                    print(line)
                else:
                    symbol = solved_rows[index][0]
                    is_input = symbol in original_knowns

                    if is_input:
                        self.log.info(f"<blue>{line}</blue>")
                    else:
                        print(line)

                index += 1

        return solved_dict
