import openmdao.api as om
import config


class MassComponent(om.ExplicitComponent):
    def setup(self):
        self.add_input("v", shape=config.N_v)
        self.add_input("t", shape=config.N_t)

        self.add_output("m", shape=1)
        self.add_output("gamma", shape=1)

    def setup_partials(self):
        self.declare_partials("*", "*", method="fd")

    def compute(self, inputs, outputs):
        v = inputs["v"]
        t = inputs["t"]

        m = 0

        outputs["m"] = m
        outputs["gamma"] = 0


model = om.Group()
model.add_subsystem("mass_component", MassComponent(), promotes=["*"])

problem = om.Problem(model)
problem.driver = om.ScipyOptimizeDriver(optimizer="SLSQP")

problem.model.add_design_var("v", lower=0.0)

problem.model.add_objective("m")

problem.setup()
problem.run_driver()

problem.model.list_inputs()
problem.model.list_outputs()
