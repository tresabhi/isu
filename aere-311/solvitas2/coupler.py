import utils


class Coupler:
    def __init__(self, hops, variant_range):
        a, b = variant_range
        x = (a + b) / 2
        x = 1.204

        solutions = None

        for i in range(len(self.hoppers)):
            knowns = {**hops[i]["invariants"]}

            if "variant" in hops[i]:
                knowns = {
                    **knowns,
                    hops[i]["variant"]: x,
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
