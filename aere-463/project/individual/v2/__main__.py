import openmdao.api as om
import config
import methods


class MassComponent(om.ExplicitComponent):
    def setup(self):
        self.add_input("v", shape=config.n_vertices)
        self.add_input("t", shape=config.n_triangles)

        self.add_output("m", shape=1)
        self.add_output("gamma", shape=1)
        self.add_output("t_e", shape=config.n_triangles)

    def setup_partials(self):
        self.declare_partials("*", "*", method="fd")

    def compute(self, inputs, outputs):
        v = inputs["v"]
        t = inputs["t"]

        m = 0

        m += methods.plate_mass(v, t)
        m += methods.wall_mass(v)

        outputs["m"] = m
        outputs["gamma"] = 0
        outputs["t_e"] = methods.


model = om.Group()
model.add_subsystem("mass_component", MassComponent(), promotes=["*"])

problem = om.Problem(model)
problem.driver = om.ScipyOptimizeDriver(optimizer="SLSQP")

problem.model.add_design_var("v", lower=0.0)
problem.model.add_design_var("t", lower=0.0, upper=config.t_effective)

problem.model.add_constraint("t_e", lower=config.t_effective)

problem.model.add_objective("m")

problem.setup()

problem.set_val("v", 10000.0)
# problem.set_val("t", 10000.0)

problem.run_driver()

print("m", problem.get_val("m")[0])
print("v", problem.get_val("v"))
print("t", problem.get_val("t"))

# problem.model.list_inputs()
# problem.model.list_outputs()
