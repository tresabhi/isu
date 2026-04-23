import sympy
import pint
import tabulate
import logger
from registry import *


class Hopper:
    has_greeted = False
    verbose = False
    sig_figs = 5
    threshold = 2**-8

    def greet(self):
        if self.has_greeted:
            return

        self.has_greeted = True

        if self.verbose:
            logger.log("Solvitas 2.0\n")

    def knowns(self, knowns):
        if self.verbose:
            print("Basing:")

        for symbol, convoluted_value in knowns.items():
            self.givens.append(symbol)

            if isinstance(convoluted_value, pint.Quantity):
                value = convoluted_value
            else:
                value = convoluted_value * symbol.unit

            value = value.to(symbol.unit)

            if self.verbose:
                print(f"  {symbol}")
                print(f"    {convoluted_value} ⤵")
                print(f"    {value}")

            self.values[symbol] = value.magnitude

        if self.verbose:
            print()

    def solve(self):
        solved = 0
        iteration = 0

        while True:
            if self.verbose:
                print(f"Iteration {iteration + 1}:")

            iteration += 1
            solved = 0
            index = 0

            for equation in self.equations:
                lhs, rhs = equation

                lhs_subbed = lhs.subs(self.values)
                rhs_subbed = rhs.subs(self.values)

                free = lhs_subbed.free_symbols | rhs_subbed.free_symbols

                prefix = f"  ({index + 1}): "

                if len(free) > 1:
                    if self.verbose:
                        print(f"{prefix}{len(free)} free symbols {free}; skipping...")
                elif len(free) == 1:
                    symbol = free.pop()
                    expression = rhs_subbed - lhs_subbed
                    initial = symbol.initial

                    if symbol in self.initials:
                        initial = self.initials[symbol]

                    try:
                        value = float(sympy.nsolve(expression, symbol, initial))

                        if self.verbose:
                            logger.log(f"{prefix}{symbol} = {value:.{self.sig_figs}g}")
                    except:
                        logger.log(
                            f"{prefix}<yellow>nsolve failed; trying symbolic...</yellow>"
                        )

                        values = sympy.solve(expression, symbol)

                        if len(values) > 1:
                            value = float(values[-1])

                            logger.log(
                                f"{prefix}<yellow>symbolic solver found {len(values)} solutions; using last...</yellow>"
                            )
                            print(f"{prefix}{symbol} = {value:.{self.sig_figs}g}")
                        elif len(values) == 1:
                            value = float(values[0])

                            if self.verbose:
                                print(f"{prefix}{symbol} = {value:.{self.sig_figs}g}")
                        else:
                            logger.log(f"{prefix}<red>symbolic solver failed</red>")

                    self.values[symbol] = value
                    solved += 1

                else:
                    lhs_float = float(lhs_subbed)
                    rhs_float = float(rhs_subbed)

                    if (
                        lhs_float == rhs_float
                        or abs(1 - lhs_float / rhs_float) < self.threshold
                    ):
                        if self.verbose:
                            print(
                                f"{prefix}{lhs_subbed:.{self.sig_figs}g} == {rhs_subbed:.{self.sig_figs}g}"
                            )
                    else:
                        logger.log(
                            f"{prefix}<red>{lhs_subbed:.{self.sig_figs}g} != {rhs_subbed:.{self.sig_figs}g}</red>"
                        )

                index += 1

            if self.verbose:
                print()

            if solved == 0:
                break

        if not self.verbose:
            print()

    def convolute(self):
        if self.verbose:
            print("Convoluting:")

        convoluted_values = {}

        for symbol, value in self.values.items():
            convoluted_values[symbol] = value * symbol.unit

            if self.verbose:
                print(f"  {symbol}")
                print(f"    {value} {symbol.unit} ⤵")

            if symbol.unit in self.units:
                convoluted_values[symbol] = convoluted_values[symbol].to(
                    self.units[symbol.unit]
                )

            if self.verbose:
                print(f"    {convoluted_values[symbol]}")

        if self.verbose:
            print()

        return convoluted_values

    def present(self):
        convoluted_values = self.convolute()
        ordered = sorted(self.values.keys(), key=lambda symbol: symbol.name.lower())
        table = []

        for symbol in ordered:
            value = convoluted_values[symbol]
            name = f"{symbol}"
            magnitude = f"{value.magnitude:.{self.sig_figs}g}"
            pretty_unit = "" if value.units == ur.dimensionless else f"{value.units:~}"
            table.append((name, magnitude, pretty_unit))

        lines = tabulate.tabulate(
            table,
            headers=["Symbol", "Value", "Units"],
            disable_numparse=True,
            tablefmt="rounded_outline",
        )
        lines = lines.splitlines()

        print(self.__class__.__name__)
        print(f"{"\n".join(lines[0:3])}")

        for index in range(len(ordered)):
            symbol = ordered[index]
            is_input = symbol in self.givens
            line = lines[index + 3]

            if is_input:
                logger.log(f"<blue>{line}</blue>")
            else:
                print(line)

        print(f"{lines[-1]}\n")

    def __init__(self, knowns):
        self.values = {}
        self.givens = []

        self.initials = getattr(self, "initials", {})

        self.greet()
        self.knowns(knowns)
        self.solve()
        self.present()
