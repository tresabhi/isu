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

            self.values[symbol] = value

        print()

    def __init__(self, knowns):
        self.greet()
        self.knowns(knowns)


class PerfectlyExpandedSubsonicNozzleHopper(Hopper):
    equations = [
        (
            A_At**2,
            (1 / (M**2))
            * ((2 / (gamma + 1)) * (1 + ((gamma - 1) / 2) * M**2))
            ** ((gamma + 1) / (gamma - 1)),
        )
    ]
