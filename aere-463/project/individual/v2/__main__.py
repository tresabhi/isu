import openmdao.api as om
import config
import methods
import plot


class MassComponent(om.ExplicitComponent):
    def setup(self):
        self.add_input("v", shape=(config.N + 1, config.M + 1))
        self.add_input("t", shape=(config.N, config.M, 2))

        self.add_output("m", shape=1)
        self.add_output("gamma", shape=1)
        self.add_output("t_prime", shape=(config.N, config.M, 2))

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
        outputs["t_prime"] = methods.effective_thickness(v, t)


model = om.Group()
model.add_subsystem("mass_component", MassComponent(), promotes=["*"])

problem = om.Problem(model)
problem.driver = om.ScipyOptimizeDriver(optimizer="SLSQP")


problem.model.add_design_var("v", lower=0.0, ref=1.0)
problem.model.add_design_var("t", lower=0.0, ref=config.t_effective)

problem.model.add_constraint(
    "t_prime", lower=config.t_effective, ref=config.t_effective
)

problem.model.add_objective("m")

problem.setup()

problem.set_val("v", 1)
problem.set_val("t", config.t_effective * 2)

problem.run_driver()

plot.plot_mesh(problem.get_val("v"), problem.get_val("t"))
