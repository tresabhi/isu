import debug
import openmdao.api as om
import solver
import airfoils

last_method = None


class AeroOptimization(om.ExplicitComponent):
    def setup(self):
        self.add_input("alpha", val=0.0)
        self.add_input("Gamma", val=0.0)
        self.add_input("theta_tip", val=0.0)
        self.add_input("c_root", val=1.0)
        self.add_input("c_tip", val=1.0)

        self.add_output("C_L", val=0.0)
        self.add_output("C_D", val=0.0)
        self.add_output("V", val=0.0)
        self.add_output("lambda", val=1.0)

    def setup_partials(self):
        self.declare_partials("*", "*", method="fd")

    def compute(self, inputs, outputs):
        global last_method

        alpha = inputs["alpha"][0]
        Gamma = inputs["Gamma"][0]
        theta_tip = inputs["theta_tip"][0]
        c_root = inputs["c_root"][0]
        c_tip = inputs["c_tip"][0]

        X = [alpha, Gamma, theta_tip, c_root, c_tip]

        C_L, C_D, V, last_method = solver.Solve(airfoils.naca641212, X)
        _lambda = c_tip / c_root

        outputs["C_L"] = C_L
        outputs["C_D"] = C_D
        outputs["V"] = V
        outputs["lambda"] = _lambda


_, _, V0, base_model = solver.Solve(
    airfoils.naca0012,
    [
        0.0,  # alpha [deg]
        0.0,  # Gamma [deg]
        0.0,  # theta_tip [deg]
        1.0,  # c_root [m]
        1.0,  # c_tip [m]
    ],
)

# debug.render_wing(base_model)

model = om.Group()
model.add_subsystem("aero_opt", AeroOptimization(), promotes=["*"])

prob = om.Problem(model)

prob.driver = om.ScipyOptimizeDriver()
prob.driver.options["optimizer"] = "SLSQP"

prob.model.add_design_var("alpha", lower=0.0, upper=10.0)
prob.model.add_design_var("Gamma", lower=-10, upper=10.0)
prob.model.add_design_var("theta_tip", lower=-10.0, upper=10.0)
prob.model.add_design_var("c_root", lower=0.2, upper=3.0)
prob.model.add_design_var("c_tip", lower=0.2, upper=3.0)

prob.model.add_objective("C_D")

prob.model.add_constraint("C_L", lower=0.4)
prob.model.add_constraint("V", lower=V0)
prob.model.add_constraint("lambda", lower=0, upper=1.0)

prob.setup()
prob.run_driver()

prob.model.list_inputs()
prob.model.list_outputs()

debug.render_wing(last_method)
# debug.render_airfoil(airfoils.naca641212)
