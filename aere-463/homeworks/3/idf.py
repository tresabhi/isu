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


class StructuralSolver(om.ExplicitComponent):
    def setup(self):
        self.add_input("theta", shape=2)
        self.add_input("t", shape=2)
        self.add_input("Gamma", shape=2)
        self.add_input("d", shape=2)

        self.add_output("struct_residual", shape=2)

    def setup_partials(self):
        self.declare_partials("*", "*", method="fd")

    def compute(self, inputs, outputs):
        theta = inputs["theta"]
        t = inputs["t"]
        Gamma = inputs["Gamma"]
        d = inputs["d"]

        A = np.array([[10.0 * t[0] - theta[0], 1.0], [1.0, 10.0 * t[1] - theta[1]]])
        b = Gamma**2

        outputs["struct_residual"] = A @ d - b


class Forces(om.ExplicitComponent):
    def setup(self):
        self.add_input("theta", shape=2)
        self.add_input("Gamma", shape=2)
        self.add_input("d", shape=2)

        self.add_output("L")
        self.add_output("D")
        self.add_output("sigma")

    def setup_partials(self):
        self.declare_partials("*", "*", method="fd")

    def compute(self, inputs, outputs):
        theta = inputs["theta"]
        Gamma = inputs["Gamma"]
        d = inputs["d"]

        outputs["L"] = 10.0 * (Gamma[0] + Gamma[1])
        outputs["D"] = Gamma[0] * np.sin(theta[0]) + Gamma[1] * np.sin(theta[1])
        outputs["sigma"] = (d[0] + d[1]) * 10**4
