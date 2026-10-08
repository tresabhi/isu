# AERE 463 Homework 3

I am going to transcribe the problem into $\LaTeX$ here so I can transform them into Python easier. Aero solver:

$$
\begin{bmatrix}
  (\theta_0 + d_0)^2 + 3 & 1 \\
  1 & (\theta_1 + d_1)^2 + 5
\end{bmatrix} \begin{bmatrix}
  \Gamma_0 \\
  \Gamma_1
\end{bmatrix} = \begin{bmatrix}
  \theta_0 + d_0 \\
  \theta_1 + d_1
\end{bmatrix}
$$

Structural solver:

$$
\begin{bmatrix}
  10 t_0 - \theta_0 & 1 \\
  1 & 10 t_1 - \theta_1
\end{bmatrix} \begin{bmatrix}
  d_0 \\
  d_1
\end{bmatrix} = \begin{bmatrix}
  \Gamma_0^2 \\
  \Gamma_1^2
\end{bmatrix}
$$

Forces:

$$
L = 10 (\Gamma_0 + \Gamma_1)
$$

$$
D = \Gamma_0 \sin \theta_0 + \Gamma_1 \sin \theta_1
$$

Stress:

$$
\sigma = (d_0 + d_1) * 10^4
$$

Objective function:

$$
f = D
$$

Constraints:

$$
L - 1 = 0
$$

$$
\sigma - 1 \le 0
$$

Initial design variables:

$$
\theta = [0.1, 0.1]^T
$$

$$
t = [1, 1]^T
$$

Fortunately, I started this homework after we went over using OpenMDAO in-class so I was able to solve the homework using the library.

The `AeroSolver` was an `ImplicitComponent` and the implementation is almost identical to what we did in-class. However, I did have to provide dimensionality arguments when adding the inputs and outputs and used NumPy to find the residuals:

```py
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
```

The `StructuralSolver` took on a similar shape:

```py
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
```

And for the other functions, I realized there's no real good reason to create a solver for each one so I combined them into the `Forces` class:

```py
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
```

Just like in-class, I created a problem and added the subsystems with promotions on all variables:

```py
prob = om.Problem()

prob.model.add_subsystem("aero", AeroSolver(), promotes=["*"])
prob.model.add_subsystem("struct", StructuralSolver(), promotes=["*"])
prob.model.add_subsystem("forces", Forces(), promotes=["*"])
```

Then I set up the linear and non-linear solvers and the driver. I am not sure if I really need the linear solver since I only use define `apply_nonlinear` in the classes above, but I can't imagine it'd hurt to add them:

```py
prob.model.nonlinear_solver = om.NewtonSolver(solve_subsystems=False, iprint=2)
prob.model.linear_solver = om.ScipyKrylov()
prob.driver = om.ScipyOptimizeDriver()
```

The design variables and constraints went in easy peasy:

```py
prob.model.add_design_var("theta")
prob.model.add_design_var("t")

prob.model.add_objective("D")

prob.model.add_constraint("L", equals=1.0)
prob.model.add_constraint("sigma", upper=1.0)
```

Through trial and error, I found out that the `set_vals` must happen after the `setup` which I find counter-intuitive?

```py
prob.setup()

prob.set_val("theta", [0.1, 0.1])
prob.set_val("t", [1.0, 1.0])
prob.set_val("Gamma", [0.1, 0.1])
prob.set_val("d", [0.1, 0.1])

prob.run_model()
```

The results are then logged and the MDF diagram is displayed:

```py
print("Gamma =", prob.get_val("Gamma"))
print("d =", prob.get_val("d"))
print("L =", prob.get_val("L"))
print("D =", prob.get_val("D"))
print("sigma =", prob.get_val("sigma"))

om.n2(prob, outfile="mdf.html", show_browser=True)
```

The output is a little concerning but I trust the library using the entire model isn't detrimental:

```
tresabhi@treslaptop:~/Projects/isu$ python aere-463/homeworks/3/mdf.py
/home/tresabhi/.local/lib/python3.14/site-packages/openmdao/utils/relevance.py:1234: OpenMDAOWarning:The top level group has a nonlinear solver that computes gradients, so the entire model will be included in the optimization iteration.
NL: Newton 0 ; 1999.00113 1
NL: Newton 1 ; 0.01003237 5.0186915e-06
NL: Newton 2 ; 6.07293442e-07 3.03798449e-10
NL: Newton 3 ; 3.5917437e-14 1.79676922e-17
NL: Newton Converged
Gamma = [0.02850763 0.0142724 ]
d = [8.08357954e-05 1.24106787e-05]
L = [0.42780035]
D = [0.00427088]
sigma = [0.93246474]
Opening in existing browser session.
[25 zypak-sandbox] Failed to wait for supervisor exit reply: Connection reset by peer (errno 104)
[23:23:0100/000000.183690:ERROR:content/zygote/zygote_linux.cc:662] write: Broken pipe (32)
```

The MDF diagram with the "variable-specific arrows" is a good visualizer for the direction of data-flow:

![](https://i.imgur.com/3NjuxKO.png)

However, I did find looking at the "level 2" diagram (down from "level 3") to be easier to parse visually since it disregards the specific variables:

![](https://i.imgur.com/uND1qEI.png)
