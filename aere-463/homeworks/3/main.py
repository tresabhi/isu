import numpy as np
import openmdao.api as om


class AeroSolver(om.ImplicitComponent):
    def setup(self):
        self.add_input("theta", shape=2)
        self.add_input("d", shape=2)

        self.add_output("Gamma", shape=2)

        self.declare_partials("Gamma", "Gamma")
        self.declare_partials("Gamma", "theta")
        self.declare_partials("Gamma", "d")
