import numpy as np
import matplotlib.pyplot as plt
import openmdao.api as om
from smt.surrogate_models import KRG
from smt.sampling_methods import LHS

x_limits = np.array([[-10, 10], [-10, 10]])
sampling = LHS(xlimits=x_limits, criterion="maximin", seed=0)


xt = sampling(10)
yt = (xt[:, 0] - 3) ** 2 + (xt[:, 1] - 2) ** 2

gt = xt[:, 0] + 2 * xt[:, 1]

sm = KRG(theta0=[1e-2])
sm.set_training_values(xt, yt)
sm.train()

sm_g = KRG(theta0=[1e-2])
sm_g.set_training_values(xt, gt)
sm_g.train()


class SMTExample(om.ExplicitComponent):
    def setup(self):
        self.add_input("x1", val=0)
        self.add_input("x2", val=0)

        self.add_output("y", val=0)
        self.add_output("g", val=0)

    def setup_partials(self):
        self.declare_partials("*", "*", method="fd")

    def compute(self, inputs, outputs):
        x1 = inputs["x1"][0]
        x2 = inputs["x2"][0]

        x_in = np.array([[x1, x2]])
        y_out = sm.predict_values(x_in)

        outputs["y"] = y_out

        g_out = sm_g.predict_values(x_in)
        outputs["g"] = g_out

    def compute_partials(self, inputs, J):
        x1 = inputs["x1"][0]
        x2 = inputs["x2"][0]

        x_in = np.array([[x1, x2]])
        dy_dx1 = sm.predict_derivatives(x_in, 0)
        dy_dx2 = sm.predict_derivatives(x_in, 1)

        J["y", "x1"] = dy_dx1
        J["y", "x2"] = dy_dx2

        dg_dx1 = sm_g.predict_derivatives(x_in, 0)
        dg_dx2 = sm_g.predict_derivatives(x_in, 1)

        J["g", "x1"] = dg_dx1
        J["g", "x2"] = dg_dx2


model = om.Group()
model.add_subsystem("SMTTest", SMTExample(), promotes=["*"])

problem = om.Problem(model)
problem.driver = om.ScipyOptimizeDriver()
problem.driver.options["optimizer"] = "SLSQP"
problem.model.add_design_var("x1", lower=-10, upper=10)
problem.model.add_design_var("x2", lower=-10, upper=10)

problem.model.add_constraint("g", upper=0)
problem.model.add_objective("y")

problem.setup()
problem.run_driver()

x10pt = problem.get_val("x1")
x20pt = problem.get_val("x2")

print("Optimized x1:", x10pt)
print("Optimized x2:", x20pt)
