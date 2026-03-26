from pathlib import Path
import shutil
from pint import Quantity
import sympy as sp
from tabulate import tabulate
from logger import logger
from registry import ur

EQUIVALENCY_THRESHOLD = 0.001


class Solver:
    solution_set = 1
    log = logger.opt(colors=True)
    terminal_size = shutil.get_terminal_size()
    working_dir = Path(__file__).resolve().parent
    name_file = working_dir / "name.txt"

    def __init__(self, equations, output_units, sig_figs=5):
        self.print_name()

        self.equations = equations
        self.output_units = output_units
        self.sig_figs = sig_figs

    def normalize_equations(self):
        self.equations = [
            equation if isinstance(equation, sp.Eq) else sp.Eq(*equation)
            for equation in self.equations
        ]

    def normalize_knowns(self, original_knowns):
        knowns = {}

        for key, value in original_knowns.items():
            if isinstance(value, Quantity):
                knowns[key] = value.to(key.unit).magnitude
            elif key.unit == ur.dimensionless:
                knowns[key] = value
            else:
                raise TypeError(f"Expected units for {key} in input")

        return knowns

    def sub_equations(self, knowns):
        subbed_equations = []

        for equation in self.equations:
            lhs = equation.lhs.subs(knowns)
            rhs = equation.rhs.subs(knowns)

            if (
                lhs.is_number
                and rhs.is_number
                and abs(rhs - lhs) > EQUIVALENCY_THRESHOLD
            ):
                self.log.info(f"<red>inequality in</red> {equation}")
                self.log.info(f"\t{lhs:.{self.sig_figs}g} != {rhs:.{self.sig_figs}g}")

            subbed_equations.append(equation.subs(knowns))

        return subbed_equations

    def solve_equations(self, knowns):
        last_knowns = 0
        solved_last_using = {}

        while len(knowns) > last_knowns:
            last_knowns = len(knowns)
            subbed_equations = self.sub_equations(knowns)

            for index in range(len(self.equations)):
                original_equation = self.equations[index]
                equation = subbed_equations[index]
                symbols = equation.free_symbols

                if len(symbols) != 1:
                    continue

                [symbol] = symbols
                solution = None

                try:
                    solution = sp.nsolve(equation, symbol, symbol.initial)
                except:
                    self.log.info(
                        f"<yellow>nsolve failed for {symbol}; trying symbolic...</yellow>"
                    )
                    self.log.info(
                        f"\t{original_equation.lhs} = {original_equation.rhs}"
                    )
                    self.log.info(f"\t{equation.lhs} = {equation.rhs}")

                    solutions = sp.solve(equation, symbol)
                    solutions_count = len(solutions)

                    if solutions_count == 1:
                        solution = float(solutions[0])
                    else:
                        self.log.info(
                            f"<yellow>{solutions_count} solutions {symbol}; using last...</yellow>"
                        )

                        solution = float(solutions[-1])

                if symbol in knowns:
                    if knowns[symbol] - solution <= EQUIVALENCY_THRESHOLD:
                        self.log.info(f"<green>over-solved</green> {symbol}")
                        self.log.info(
                            f"\t{knowns[symbol]:.{self.sig_figs}g} == {solution:.{self.sig_figs}g}"
                        )

                    else:
                        last_equation = solved_last_using[symbol]
                        self.log.info(f"<red>over-solved</red> {symbol}")
                        self.log.info(
                            f"\t{knowns[symbol]:.{self.sig_figs}g} != {solution:.{self.sig_figs}g}"
                        )
                        self.log.info(f"\t({last_equation.lhs} = {last_equation.rhs})")
                        self.log.info(
                            f"\t({original_equation.lhs} = {original_equation.rhs})"
                        )

                else:
                    knowns[symbol] = solution

                solved_last_using[symbol] = original_equation

    def print_name(self):
        with open(self.name_file) as file:
            name = file.read()
            self.log.info(f"<white>{name}</white>")

        self.print_divider()

    def print_divider(self):
        line = "─" * self.terminal_size.columns
        self.log.info(f"\n<white>{line}</white>\n")

    def print_solutions(self, knowns, original_knowns):
        solved_dict = {}
        ordered_known_symbols = sorted(
            knowns.keys(), key=lambda symbol: symbol.name.replace("\\", "").lower()
        )
        table = []

        for symbol in ordered_known_symbols:
            unit = (
                self.output_units[symbol]
                if symbol in self.output_units
                else symbol.unit
            )
            value = knowns[symbol]
            value_with_unit = (float(value) * symbol.unit).to(unit)

            solved_dict[symbol] = value_with_unit
            name = f"{symbol}"
            memo = symbol.memo
            magnitude = f"{value_with_unit.magnitude:.{self.sig_figs}g}"
            pretty_unit = (
                ""
                if value_with_unit.units == ur.dimensionless
                else f"{value_with_unit.units:~}"
            )
            table.append((name, magnitude, pretty_unit, memo))

        lines = tabulate(
            table,
            headers=["Symbol", "Value", "Units", "Memo"],
            disable_numparse=True,
            tablefmt="rounded_outline",
        )
        lines = lines.splitlines()

        print(f"\n{"\n".join(lines[0:3])}")

        for index in range(len(ordered_known_symbols)):
            symbol = ordered_known_symbols[index]
            is_input = symbol in original_knowns
            line = lines[index + 3]

            if is_input:
                self.log.info(f"<blue>{line}</blue>")
            else:
                print(line)

        print(lines[-1])

        return solved_dict

    def solve(self, original_knowns):
        self.normalize_equations()

        knowns = self.normalize_knowns(original_knowns)

        self.solve_equations(knowns)
        solved_dict = self.print_solutions(knowns, original_knowns)

        self.print_divider()

        return solved_dict
