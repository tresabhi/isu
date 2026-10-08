import numpy as np
import openmdao.api as om


class AeroSolver(om.ExplicitComponent):
    def setup(self):
        self.add_input("theta", shape=2)
        self.add_input("d", shape=2)
        self.add_input("Gamma", shape=2)

        self.add_output("aero_residual", shape=2)

    def setup_partials(self):
        self.declare_partials("*", "*", method="fd")

    def compute(self, inputs, outputs):
        theta = inputs["theta"]
        d = inputs["d"]
        Gamma = inputs["Gamma"]

        A = np.array([[(theta[0] + d[0]) ** 2 + 3, 1], [1, (theta[1] + d[1]) ** 2 + 5]])
        b = np.array([theta[0] + d[0], theta[1] + d[1]])

        outputs["aero_residual"] = A @ Gamma - b
