import openmdao.api as om
import numpy as np


class ImplicitEqn(om.ImplicitComponent):
    def setup(self):
        self.add_input("x", val=1.0)
        self.add_input("y", val=1.0)

    def setup_partials(self):
        return self.declare_partials("*", "*", method="fd")

    def apply_nonlinear(self, inputs, outputs, residuals):
        x = inputs["x"][0]
        y = inputs["y"][0]

        residuals["y"] = np.exp(-x * y) - y


prob = om.Problem()

prob.model.add_subsystem("test", ImplicitEqn(), promotes=["*"])
prob.model.nonlinear_solver = om.NewtonSolver(solve_subsystems=False, iprint=-1)
prob.model.linear_solver = om.ScipyKrylov()

prob.setup()
prob.run_model()
