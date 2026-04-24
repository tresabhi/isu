import utils
from hopper import *


class Coupler:
    max_iterations = 2**5

    def hop(self, x):
        solutions = None
        target_value = None

        for i in range(len(self.hoppers)):
            hop = self.hops[i]
            knowns = {**hop["invariants"]}

            if "variant" in hop:
                knowns = {
                    **knowns,
                    hop["variant"]: x,
                }

            if i > 0:
                knowns = {
                    **knowns,
                    **utils.to_state_space(
                        solutions,
                        *self.transformers[i - 1],
                    ),
                }

            Hopper = self.hoppers[i]
            solutions = Hopper(knowns).knowns

            if "target" in hop:
                if target_value is not None:
                    raise Exception("Multiple targets")

                target_value = solutions[hop["target"]]

        return target_value

    def solve(self):
        a, b = self.range

        for _ in range(self.max_iterations):
            x = (a + b) / 2

            value = self.hop(x)
            error = abs(value / self.target - 1)

            if error < Hopper.tolerance:
                return x

            if (value > self.target) == self.increasing:
                b = x
            else:
                a = x

        raise Exception(f"Failed to converge in {self.max_iterations} iterations")

    def __init__(self, hops, variant_range, target):
        self.hops = hops
        self.range = variant_range
        self.target = target

        a, b = self.range

        value_a = self.hop(a)
        value_b = self.hop(b)

        self.increasing = value_b > value_a
