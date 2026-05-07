from states import *


class Shaker:
    def __init__(self, *hops):
        self.hoppers_count = len(self.hoppers)
        self.states = [{**hop} for hop in hops]

        # self.go(False)
        self.go(True)
        # self.go(False)
        # self.go(True)

    def go(self, forward):
        indices = (
            range(self.hoppers_count)
            if forward
            else range(self.hoppers_count - 1, -1, -1)
        )

        for i in indices:
            Hopper = self.hoppers[i]
            hopper = Hopper(self.states[i])
            solutions = hopper.solve()
            self.states[i] = {**self.states[i], **solutions}

            merge_criteria = self.hoppers_count - 1 if forward else 0

            if i != merge_criteria:
                stateA, stateB = self.transformers[i - 1]

                if not forward:
                    stateA, stateB = stateB, stateA

                next_i = i + 1 if forward else i - 1

                self.states[next_i] = {
                    **self.states[next_i],
                    **to_state_space(self.states[i], stateA, stateB),
                }
