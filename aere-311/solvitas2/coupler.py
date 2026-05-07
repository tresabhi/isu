from states import *
from hopper import *


class Coupler:
    def __init__(self, hops, range, target):
        self.range = range
        self.target = target
        self.hoppers_count = len(self.hoppers)
        self.states = [{**hop} for hop in hops]

        a, b = self.range

        self.go(True, (a + b) / 2)

    def go(self, forward, guess):
        indices = (
            range(self.hoppers_count)
            if forward
            else range(self.hoppers_count - 1, -1, -1)
        )

        for i in indices:
            Hopper = self.hoppers[i]

            passed_state = {}
            target_key = None

            for key, value in self.states[i].items():
                if value is x:
                    passed_state[key] = guess
                elif value is y:
                    target_key = key
                else:
                    passed_state[key] = value

            hopper = Hopper(passed_state)
            solutions = hopper.solve()

            if target_key is not None and target_key in solutions:
                return target_key

            self.states[i] = {**solutions, **self.states[i]}

            merge_criteria = self.hoppers_count - 1 if forward else 0

            if i != merge_criteria:
                stateA, stateB = self.transformers[i if forward else i - 1]

                if not forward:
                    stateA, stateB = stateB, stateA

                next_i = i + 1 if forward else i - 1

                self.states[next_i] = {
                    **self.states[next_i],
                    **to_state_space(self.states[i], stateA, stateB),
                }
