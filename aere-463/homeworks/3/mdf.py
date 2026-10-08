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
        theta = inputs["theta"]
        d = inputs["d"]
        Gamma = outputs["Gamma"]

        A = np.array([[(theta[0] + d[0]) ** 2 + 3, 1], [1, (theta[1] + d[1]) ** 2 + 5]])
        b = np.array([theta[0] + d[0], theta[1] + d[1]])

        residuals["Gamma"] = A @ Gamma - b


class StructuralSolver(om.ImplicitComponent):
    def setup(self):
        self.add_input("theta", shape=2)
        self.add_input("t", shape=2)
        self.add_input("Gamma", shape=2)

        self.add_output("d", shape=2)

    def setup_partials(self):
        self.declare_partials("*", "*", method="fd")

    def apply_nonlinear(self, inputs, outputs, residuals):
        theta = inputs["theta"]
        t = inputs["t"]
        Gamma = inputs["Gamma"]
        d = outputs["d"]

        A = np.array([[10.0 * t[0] - theta[0], 1.0], [1.0, 10.0 * t[1] - theta[1]]])
        b = Gamma**2

        residuals["d"] = A @ d - b


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


prob = om.Problem()

prob.model.add_subsystem("aero", AeroSolver(), promotes=["*"])
prob.model.add_subsystem("struct", StructuralSolver(), promotes=["*"])
prob.model.add_subsystem("forces", Forces(), promotes=["*"])

prob.model.nonlinear_solver = om.NewtonSolver(solve_subsystems=False, iprint=2)
prob.model.linear_solver = om.ScipyKrylov()
prob.driver = om.ScipyOptimizeDriver()

prob.model.add_design_var("theta")
prob.model.add_design_var("t")

prob.model.add_objective("D")

prob.model.add_constraint("L", equals=1.0)
prob.model.add_constraint("sigma", upper=1.0)

prob.setup()

prob.set_val("theta", [0.1, 0.1])
prob.set_val("t", [1.0, 1.0])
prob.set_val("Gamma", [0.1, 0.1])
prob.set_val("d", [0.1, 0.1])

prob.run_model()

print("Gamma =", prob.get_val("Gamma"))
print("d =", prob.get_val("d"))
print("L =", prob.get_val("L"))
print("D =", prob.get_val("D"))
print("sigma =", prob.get_val("sigma"))

om.n2(prob, outfile="mdf.html", show_browser=True)
