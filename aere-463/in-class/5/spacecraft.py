from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
import openmdao.api as om


class OrbitRaise(om.ExplicitComponent):
    def setup(self):
        self.add_input("dv_theta", val=0.0)
        self.add_input("dv_r", val=0.0)
        self.add_input("tof", val=3.0)

        self.add_output("r_final", val=0.0)
        self.add_output("delta_v_mag", val=0.0)

    def setup_partials(self):
        self.declare_partials("*", "*", method="fd")

    def compute(self, inputs, outputs):
        dv_theta = inputs["dv_theta"][0]
        dv_r = inputs["dv_r"][0]
        tof = inputs["tof"][0]

        outputs["delta_v_mag"] = np.sqrt(dv_theta**2 + dv_r**2)

        theta_0 = 0
        r_0 = 1
        v_theta_0 = 1 + dv_theta
        v_r_0 = 0 + dv_r

        y_0 = [theta_0, r_0, v_theta_0, v_r_0]
        t_span = [0, tof]

        solution = solve_ivp(self.dynamic_eqn, t_span, y_0, max_step=0.1)

        theta = solution.y[0]
        r = solution.y[1]

        outputs["r_final"] = r[-1]

    def dynamic_eqn(self, t, y):
        [theta, r, v_theta, v_r] = y

        dy_dt = np.zeros(4)

        dy_dt[0] = v_theta / r
        dy_dt[1] = v_r
        dy_dt[2] = -v_r * v_theta / r
        dy_dt[3] = v_theta**2 / r - 1 / r / r

        return dy_dt


model = om.Group()
model.add_subsystem("trajectory_opt", OrbitRaise(), promotes=["*"])

prob = om.Problem(model)

prob.driver = om.ScipyOptimizeDriver()
prob.driver.options["optimizer"] = "SLSQP"

prob.model.add_design_var("dv_theta", lower=-5, upper=5)
prob.model.add_design_var("dv_r", lower=-5, upper=5)
prob.model.add_design_var("tof", lower=0, upper=5)

prob.model.add_objective("delta_v_mag")

prob.model.add_constraint("r_final", upper=2)

prob.setup()
prob.run_driver()

prob.model.list_inputs()
prob.model.list_outputs()

dv_theta = prob.get_val("dv_theta")[0]
dv_r = prob.get_val("dv_r")[0]
tof = prob.get_val("tof")[0]

theta_0 = 0
r_0 = 1
v_theta_0 = 1 + dv_theta
v_r_0 = 0 + dv_r

y_0 = [theta_0, r_0, v_theta_0, v_r_0]
t_span = [0, tof]

solution = solve_ivp(prob.dynamic_eqn, t_span, y_0, max_step=0.1)

theta = solution.y[0]
r = solution.y[1]
