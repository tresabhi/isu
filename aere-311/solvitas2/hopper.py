import sympy
import pint
import tabulate
import logger
from registry import *
import math


class Hopper:
    has_greeted = False

    def greet(self):
        if self.has_greeted:
            return

        self.has_greeted = True

        if self.verbose:
            logger.log("Solvitas 2.0\n")

    def consume(self, knowns):
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

    def propagate(self):
        precision = -math.log10(self.tolerance)

        solved = 0
        iteration = 0

        subbed = []
        frees = []
        resolved = []

        for equation in self.equations:
            lhs, rhs = equation

            lhs_subbed = lhs.subs(self.values)
            rhs_subbed = rhs.subs(self.values)

            frees.append((lhs_subbed.free_symbols, rhs_subbed.free_symbols))
            subbed.append((lhs_subbed, rhs_subbed))
            resolved.append(False)

        while True:
            if self.verbose:
                print(f"Iteration {iteration + 1}:")

            iteration += 1
            solved = 0

            for i in range(len(self.equations)):
                lhs_free, rhs_free = frees[i]
                free_union = lhs_free | rhs_free
                free_count = len(free_union)

                if resolved[i] or free_count > 1:
                    continue

                if free_count == 1:
                    prefix = f"  ({i + 1}): "
                    symbol = free_union.pop()
                    initial = symbol.initial

                    lhs_subbed, rhs_subbed = subbed[i]
                    expression = rhs_subbed - lhs_subbed

                    if symbol in self.initials:
                        initial = self.initials[symbol]

                    try:
                        value = float(
                            sympy.nsolve(expression, symbol, initial, prec=precision)
                        )

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
                            continue

                    self.values[symbol] = value
                    resolved[i] = True
                    solved += 1

                    for j in range(len(self.equations)):
                        if i == j:
                            continue

                        lhs_free, rhs_free = frees[j]
                        is_in_lhs = symbol in lhs_free
                        is_in_rhs = symbol in rhs_free

                        if not is_in_lhs and not is_in_rhs:
                            continue

                        lhs_subbed, rhs_subbed = subbed[j]

                        if is_in_lhs:
                            lhs_free.remove(symbol)
                            lhs_subbed = lhs_subbed.subs(symbol, value)

                        if is_in_rhs:
                            rhs_free.remove(symbol)
                            rhs_subbed = rhs_subbed.subs(symbol, value)

                        subbed[j] = (lhs_subbed, rhs_subbed)
                        free_union = lhs_free | rhs_free
                        frees[j] = (lhs_free, rhs_free)

                        if len(free_union) != 0:
                            continue

                        lhs_float = float(lhs_subbed)
                        rhs_float = float(rhs_subbed)

                        if (
                            lhs_float == rhs_float
                            or abs(1 - lhs_float / rhs_float) < self.tolerance
                        ):
                            resolved[j] = True
                        else:
                            logger.log(
                                f"{prefix}<red>{lhs_float:.{self.sig_figs}g} != {rhs_float:.{self.sig_figs}g}</red>"
                            )

                else:
                    raise ValueError("Equation is unresolved and has 0 free symbols")

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

            print(ur("radian") == ur("dimensionless"))
            if symbol.unit in self.units:
                convoluted_values[symbol] = convoluted_values[symbol].to(
                    self.units[symbol.unit]
                )

            if self.verbose:
                print(f"    {convoluted_values[symbol]}")

        if self.verbose:
            print()

        self.knowns = convoluted_values

    def print_table(self):
        ordered = sorted(self.values.keys(), key=lambda symbol: symbol.name.lower())
        table = []

        for symbol in ordered:
            value = self.knowns[symbol]
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

    def solve(self):
        self.propagate()
        self.convolute()

        if self.tabulate:
            self.print_table()

        return self.knowns

    def __init__(
        self,
        knowns,
        tabulate=True,
        verbose=False,
        sig_figs=5,
        tolerance=2**-10,
    ):
        self.values = {}
        self.givens = []

        self.tabulate = tabulate
        self.verbose = verbose
        self.sig_figs = sig_figs
        self.tolerance = tolerance

        self.initials = getattr(self, "initials", {})

        self.greet()
        self.consume(knowns)
