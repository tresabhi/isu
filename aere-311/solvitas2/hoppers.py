from symbols import *
import pint


class Hopper:
    has_greeted = False

    values = {}
    givens = []

    def greet(self):
        if not self.__class__.has_greeted:
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

    def hop(self):
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

                print(f"  ({index + 1}): ", end="")

                if len(free) > 1:
                    print(f"{free} free symbols; skipping...")
                elif len(free) == 1:
                    symbol = free.pop()
                    initial = symbol.initial

                    value = sympy.nsolve(rhs_subbed - lhs_subbed, symbol, initial)

                    self.values[symbol] = value
                    solved += 1

                    print(f"{symbol} = {value}")
                else:
                    print(f"{lhs_subbed} == {rhs_subbed}")

                index += 1

            print()

            if solved == 0:
                break

    def __init__(self, knowns):
        self.greet()
        self.knowns(knowns)
        self.hop()


class PerfectlyExpandedSubsonicNozzleHopper(Hopper):
    equations = [
        (
            A_At**2,
            (1 / (M**2))
            * ((2 / (gamma + 1)) * (1 + ((gamma - 1) / 2) * M**2))
            ** ((gamma + 1) / (gamma - 1)),
        )
    ]
