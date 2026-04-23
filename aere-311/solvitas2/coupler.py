import utils


class Coupler:
    def __init__(self, invariants, targets, variants):
        solutions = None

        for i in range(len(self.hoppers)):
            knowns = {
                **invariants[i],
                **variants[i],
            }

            if i > 0:
                knowns = {
                    **knowns,
                    **utils.to_state_space(
                        solutions,
                        *self.transformers[i - 1],
                    ),
                }

            solutions = self.hoppers[i](knowns).knowns
