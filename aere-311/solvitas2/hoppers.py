from symbols import *


class Hopper:
    def __init__(self, knowns):
        print(self.equations)


class PerfectlyExpandedSubsonicNozzleHopper(Hopper):
    equations = [
        (
            A_At**2,
            (1 / (M**2))
            * ((2 / (gamma + 1)) * (1 + ((gamma - 1) / 2) * M**2))
            ** ((gamma + 1) / (gamma - 1)),
        )
    ]
