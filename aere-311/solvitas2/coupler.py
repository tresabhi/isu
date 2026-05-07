from states import *
from hopper import *


class Coupler:
    tolerance = 2**-10
    max_iterations = 64

    def __init__(self, hops, range, target):
        self.range = range
        self.target = target
        self.hoppers_count = len(self.hoppers)
        self.hops = hops

    def solve(self):
        a, b = self.range

        best_guess = None
        best_error = float("inf")

        for _ in range(self.max_iterations):
            width = b - a

            if width < self.tolerance:
                break

            m1 = a + width / 3
            m2 = b - width / 3

            y1 = self.go(True, m1, [{**hop} for hop in self.hops])
            y2 = self.go(True, m2, [{**hop} for hop in self.hops])

            e1 = abs(y1 / self.target - 1)
            e2 = abs(y2 / self.target - 1)

            if e1 < best_error:
                best_error = e1
                best_guess = m1

            if e2 < best_error:
                best_error = e2
                best_guess = m2

            if best_error < self.tolerance:
                break

            if e1 < e2:
                b = m2
            else:
                a = m1

        return best_guess

    def go(self, forward, guess, states):
        indices = (
            range(self.hoppers_count)
            if forward
            else range(self.hoppers_count - 1, -1, -1)
        )

        for i in indices:
            Hopper = self.hoppers[i]

            passed_state = {}
            target_key = None

            for key, value in states[i].items():
                if value is x:
                    passed_state[key] = guess
                elif value is y:
                    target_key = key
                else:
                    passed_state[key] = value

            hopper = Hopper(passed_state)
            solutions = hopper.solve()

            if target_key is not None and target_key in solutions:
                return solutions[target_key]

            states[i] = {**solutions, **states[i]}

            merge_criteria = self.hoppers_count - 1 if forward else 0

            if i != merge_criteria:
                stateA, stateB = self.transformers[i if forward else i - 1]

                if not forward:
                    stateA, stateB = stateB, stateA

                next_i = i + 1 if forward else i - 1

                states[next_i] = {
                    **states[next_i],
                    **to_state_space(states[i], stateA, stateB),
                }
