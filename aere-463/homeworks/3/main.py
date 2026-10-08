import numpy as np
import openmdao.api as om


class AeroSolver(om.ImplicitComponent):
    def setup(self):
        self.add_input("theta", shape=2)
        self.add_input("d", shape=2)

        self.add_output("Gamma", shape=2)

    def setup_partials(self):
        self.declare_partials("*", "*", method="fd")

    def apply_nonlinear(self, inputs, outputs, residuals):
        theta = inputs["theta"][0]
        t = inputs["t"][0]
        Gamma = inputs["Gamma"][0]
        d = outputs["d"][0]

        A = np.array([[10 * t[0] - theta[0], 1], [1, 10 * t[1] - theta[1]]])

        residuals["d"] = A @ d - Gamma**2


class StructuralSolver(om.ImplicitComponent):
    def setup(self):
        self.add_input("t", shape=2)
        self.add_input("Gamma", shape=2)

        self.add_output("d", shape=2)

    def setup_partials(self):
        self.declare_partials("*", "*", method="fd")

    def apply_nonlinear(self, inputs, outputs, residuals):
        theta = inputs["theta"][0]
        t = inputs["t"][0]
        Gamma = inputs["Gamma"][0]
        d = outputs["d"][0]

        A = np.array([[10.0 * t[0] - theta[0], 1.0], [1.0, 10.0 * t[1] - theta[1]]])
        b = Gamma**2

        residuals["d"] = A @ d - b
