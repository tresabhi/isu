from symbols import *
import pint
from curries import *


class Hopper:
    has_greeted = False

    values = {}
    givens = []

    def greet(self):
        if self.__class__.has_greeted:
            return

        self.__class__.has_greeted = True
        print("This is Solvitas 2.0\n")

    def knowns(self, knowns):
        for symbol, convoluted_value in knowns.items():
            self.givens.append(symbol)

            if isinstance(convoluted_value, pint.Quantity):
                value = convoluted_value
            else:
                value = convoluted_value * symbol.unit

            value = value.to(symbol.unit)

            print(f"{symbol}: {convoluted_value} -> {value}")

            self.values[symbol] = value.magnitude

        print()

    def solve(self):
        solved = 0
        iteration = 0

        while True:
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
                    print(f"{prefix}{free} free symbols; skipping...")
                elif len(free) == 1:
                    symbol = free.pop()
                    initial = symbol.initial
                    expression = rhs_subbed - lhs_subbed

                    try:
                        value = sympy.nsolve(expression, symbol, initial)

                        print(f"{prefix}{symbol} = {value}")
                    except:
                        print(f"{prefix} nsolve failed; trying symbolic...")

                        values = sympy.solve(expression, symbol)

                        if len(values) > 1:
                            value = values[-1]

                            print(
                                f"{prefix} symbolic solver found {len(values)} solutions; using last..."
                            )
                            print(f"{prefix}{symbol} = {value}")
                        elif len(values) == 1:
                            value = values[0]

                            print(f"{prefix}{symbol} = {value}")
                        else:
                            raise ValueError(f"Could not solve {expression}")

                    self.values[symbol] = value
                    solved += 1

                else:
                    print(f"{prefix}{lhs_subbed} == {rhs_subbed}")

                index += 1

            print()

            if solved == 0:
                break

    def __init__(self, knowns):
        self.greet()
        self.knowns(knowns)
        self.solve()
        self.present()

        print(self.values)


class PerfectlyExpandedSubsonicNozzleHopper(Hopper):
    equations = [
        (
            A_At**2,
            (1 / (M**2))
            * ((2 / (gamma + 1)) * (1 + ((gamma - 1) / 2) * M**2))
            ** ((gamma + 1) / (gamma - 1)),
        ),
        #
        *state_curry(
            M,
            (p, p0, p_p0, p0_p),
        ),
    ]
