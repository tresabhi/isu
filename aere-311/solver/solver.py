from pathlib import Path
from pint import Quantity
import sympy as sp
from tabulate import tabulate
from symbols import Symbol
from logger import logger
from registry import ur

HEADERS = ["Symbol", "Value", "Units"]
EQUIVALENCY_THRESHOLD = 0.001


class Solver:
    solution_set = 1
    log = logger.opt(colors=True)
    solutions_dir = Path(__file__).resolve().parent / "solutions"

    def __init__(self, equations, output_units, sig_figs=5):
        self.equations = [sp.Eq(*equation) for equation in equations]
        self.output_units = output_units
        self.sig_figs = sig_figs

        for item in self.solutions_dir.iterdir():
            item.unlink()

    def solve(self, original_knowns: dict[Symbol, Quantity | float]):
        knowns = {}

        for key, value in original_knowns.items():
            if isinstance(value, Quantity):
                knowns[key] = value.to(key.unit).magnitude
            elif key.unit == ur.dimensionless:
                knowns[key] = value
            else:
                raise TypeError(f"Expected units for {key} in input")

        last_knowns = 0
        subbed_equations = []
        solved_last_using = {}

        while len(knowns) > last_knowns:
            last_knowns = len(knowns)
            subbed_equations = []
            index = 0

            for equation in self.equations:
                lhs = equation.lhs.subs(knowns)
                rhs = equation.rhs.subs(knowns)

                if (
                    lhs.is_number
                    and rhs.is_number
                    and not abs(rhs - lhs) < EQUIVALENCY_THRESHOLD
                ):
                    self.log.info(f"{equation}: <red>inequality</red> {lhs} != {rhs}")

                subbed_equations.append(equation.subs(knowns))

            for equation in subbed_equations:
                original_equation = self.equations[index]
                symbols = equation.free_symbols
                index += 1

                if len(symbols) != 1:
                    continue

                [symbol] = symbols
                solution = None

                try:
                    solution = sp.nsolve(equation, symbol, symbol.initial)
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
                    if knowns[symbol] - solution <= EQUIVALENCY_THRESHOLD:
                        self.log.info(
                            f"{symbol}: <green>over-solved</green> {knowns[symbol]} == {solution}"
                        )
                    else:
                        last_equation = solved_last_using[symbol]
                        self.log.info(
                            f"{symbol}: <red>over-solved</red> {knowns[symbol]} != {solution}\n\t({last_equation.lhs} = {last_equation.rhs})\n\t({original_equation.lhs} = {original_equation.rhs})"
                        )

                else:
                    knowns[symbol] = solution

                solved_last_using[symbol] = original_equation

        solved_dict = {}
        ordered_known_symbols = sorted(
            knowns.keys(), key=lambda symbol: symbol.name.replace("\\", "").lower()
        )

        solutions_section = ""
        solutions_section += "## Solutions\n\n"
        solutions_section += "| Symbol | Value | Units |\n"
        solutions_section += "| - | - | - |\n"

        for symbol in ordered_known_symbols:
            unit = (
                self.output_units[symbol]
                if symbol in self.output_units
                else symbol.unit
            )
            value = knowns[symbol]
            value_with_unit = (float(value) * symbol.unit).to(unit)

            solved_dict[symbol] = value
            name = sp.latex(symbol)
            magnitude = f"{value_with_unit.magnitude:.{self.sig_figs}g}"
            pretty_unit = (
                ""
                if value_with_unit.units == ur.dimensionless
                else f"{value_with_unit.units:~}"
            )

            wrapper0 = wrapper1 = ""

            if symbol in original_knowns:
                wrapper0 = '<span style="color:#7aaeff">'
                wrapper1 = "</span>"

            solutions_section += f"| {wrapper0}${name}${wrapper1} | "
            solutions_section += f"{wrapper0}${magnitude}${wrapper1} | "
            solutions_section += f"{wrapper0}{pretty_unit}{wrapper1} |\n"

        intro_section = ""
        intro_section += "# Sunrise Solver\n\n"

        with open(self.solutions_dir / f"{self.solution_set}.md", "w") as file:
            file.write(intro_section)
            file.write(solutions_section)

        self.solution_set += 1

        return solved_dict
