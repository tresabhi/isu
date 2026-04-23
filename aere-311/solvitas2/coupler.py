import utils


class Coupler:
    tolerance = 2**-8

    def __init__(self, hops, variant_range, target, derivative=1):
        a, b = variant_range
        x = (a + b) / 2

        solutions = None
        target_value = None

        for i in range(len(self.hoppers)):
            hop = hops[i]
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

        error = target_value / target - 1

        if abs(error) < self.tolerance:
            pass
        elif (error > 0) == (derivative > 0):
            b = x
        else:
            a = x

        x = (a + b) / 2
