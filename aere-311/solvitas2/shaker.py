from states import *


class Shaker:
    def __init__(self, hops):
        hoppers_count = len(self.hoppers)
        states = [{**hop} for hop in hops]

        for i in range(hoppers_count):
            Hopper = self.hoppers[i]

            solutions = Hopper(states[i]).solve()
            states[i] = {**states[i], **solutions}

            if i != hoppers_count - 1:
                stateA, stateB = self.transformers[i]
                states[i + 1] = {
                    **states[i + 1],
                    **to_state_space(states[i], stateA, stateB),
                }
