# implicit equation: x^(-xy) - y = 0
# objective function: f = 2y^2 - y

import openmdao.api as om
import numpy as np


class ImplicitEqn(om.ImplicitComponent):
    def setup(self):
        self.add_input("x", val=2.0)
        self.add_output("y", val=1.0)

    def setup_partials(self):
        self.declare_partials("*", "*", method="fd")

    def apply_nonlinear(self, inputs, outputs, residuals):
        x = inputs["x"][0]
        y = outputs["y"][0]

        residuals["y"] = np.exp(-x * y) - y


class ObjFunc(om.ExplicitComponent):
    def setup(self):
        self.add_input("y", val=0.0)
        self.add_output("f", val=0.0)

    def setup_partials(self):
        self.declare_partials("*", "*", method="fd")

    def compute(self, inputs, outputs):
        y = inputs["y"][0]
        f = 2 * y**2 - y
        outputs["f"] = f


prob = om.Problem()

prob.model.add_subsystem("test", ImplicitEqn(), promotes=["*"])
prob.model.add_subsystem("obj", ObjFunc(), promotes=["*"])

prob.model.nonlinear_solver = om.NewtonSolver(solve_subsystems=False, iprint=2)
prob.model.linear_solver = om.ScipyKrylov()

prob.setup()
prob.run_model()

print(prob.get_val("test.y"))
print(prob.get_val("obj.f"))
