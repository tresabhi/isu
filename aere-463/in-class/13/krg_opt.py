import numpy as np
import matplotlib.pyplot as plt
import openmdao.api as om
from smt.surrogate_models import KRG
from smt.sampling_methods import LHS

x_limits = np.array([[-10, 10], [-10, 10]])
sampling = LHS(xlimits=x_limits, criterion="maximin")


xt = sampling(10)
yt = (xt[:, 0] - 3) ** 2 + (xt[:, 1] - 2) ** 2

# print(xt)
# print(yt)

sm = KRG(theta0=[1e-2])

sm.set_training_values(xt, yt)
sm.train()


class SMTExample(om.ExplicitComponent):
    def setup(self):
        self.add_input("x1", val=0)
        self.add_input("x2", val=0)

        self.add_output("y", val=0)

    def setup_partials(self):
        self.declare_partials("*", "*", method="fd")

    def compute(self, inputs, outputs):
        x1 = inputs["x1"][0]
        x2 = inputs["x2"][0]

        x_in = np.array([[x1, x2]])
        y_out = sm.predict_values(x_in)

        outputs["y"] = y_out
