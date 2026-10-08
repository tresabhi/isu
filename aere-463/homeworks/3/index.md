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

Through trial and error, I found out that the `set_vals` must happen after the `setup` which I find counter-intuitive? Also, for the longest time, I was using `prob.run_model()` and was confused why it converged so far. That's just one evaluation! I had to switch to `prob.run_driver()`:

```py
prob.setup()

prob.set_val("theta", [0.1, 0.1])
prob.set_val("t", [1.0, 1.0])
prob.set_val("Gamma", [0.1, 0.1])
prob.set_val("d", [0.1, 0.1])

prob.run_driver()
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
NL: Newton 0 ; 3.5917437e-14 1
NL: Newton Converged
NL: Newton 0 ; 0.498254204 1
NL: Newton 1 ; 0.0107031147 0.0214812331
NL: Newton 2 ; 3.57332044e-07 7.17168146e-07
NL: Newton 3 ; 7.93829816e-14 1.59322251e-13
NL: Newton Converged
NL: Newton 0 ; 0.406027953 1
NL: Newton 1 ; 0.00814154187 0.0200516783
NL: Newton 2 ; 5.82414364e-08 1.43441938e-07
NL: Newton 3 ; 1.18085129e-14 2.90830048e-14
NL: Newton Converged
NL: Newton 0 ; 0.384777448 1
NL: Newton 1 ; 0.0146365099 0.0380388976
NL: Newton 2 ; 1.37152564e-07 3.56446472e-07
NL: Newton 3 ; 4.84684694e-14 1.25964943e-13
NL: Newton Converged
NL: Newton 0 ; 0.323283713 1
NL: Newton 1 ; 0.0108049608 0.0334225337
NL: Newton 2 ; 1.11992943e-07 3.4642309e-07
NL: Newton 3 ; 3.04785607e-14 9.42780583e-14
NL: Newton Converged
NL: Newton 0 ; 0.0264549816 1
NL: Newton 1 ; 7.59153248e-05 0.00286960414
NL: Newton 2 ; 4.87265673e-12 1.84186737e-10
NL: Newton Converged
NL: Newton 0 ; 0.169548379 1
NL: Newton 1 ; 0.000758892577 0.0044759648
NL: Newton 2 ; 5.23516906e-11 3.08771401e-10
NL: Newton Converged
NL: Newton 0 ; 0.0129095486 1
NL: Newton 1 ; 9.68304386e-06 0.000750068355
NL: Newton 2 ; 3.7891009e-14 2.93511495e-12
NL: Newton Converged
NL: Newton 0 ; 0.00448273186 1
NL: Newton 1 ; 1.34837341e-06 0.000300792786
NL: Newton 2 ; 5.53826976e-15 1.23546755e-12
NL: Newton Converged
NL: Newton 0 ; 7.38810879e-05 1
NL: Newton 1 ; 2.8019147e-10 3.79246541e-06
NL: Newton 2 ; 2.48259855e-16 3.36026258e-12
NL: Newton Converged
NL: Newton 0 ; 0.000408367565 1
NL: Newton 1 ; 1.12852712e-08 2.7635082e-05
NL: Newton 2 ; 1.36195818e-16 3.33512819e-13
NL: Newton Converged
NL: Newton 0 ; 0.0020348644 1
NL: Newton 1 ; 2.80239344e-07 0.000137718928
NL: Newton 2 ; 1.25051546e-15 6.14544861e-13
NL: Newton Converged
NL: Newton 0 ; 0.00988415847 1
NL: Newton 1 ; 6.6170369e-06 0.000669458803
NL: Newton 2 ; 2.76560507e-14 2.79801774e-12
NL: Newton Converged
NL: Newton 0 ; 0.0417469552 1
NL: Newton 1 ; 0.000118367664 0.0028353604
NL: Newton 2 ; 5.18470366e-13 1.24193576e-11
NL: Newton Converged
NL: Newton 0 ; 0.0194375632 1
NL: Newton 1 ; 2.55192665e-05 0.00131288404
NL: Newton 2 ; 9.42549807e-14 4.84911508e-12
NL: Newton Converged
NL: Newton 0 ; 0.029581831 1
NL: Newton 1 ; 5.97472608e-05 0.00201972828
NL: Newton 2 ; 2.02768397e-13 6.8544911e-12
NL: Newton Converged
NL: Newton 0 ; 0.00384120798 1
NL: Newton 1 ; 1.03838982e-06 0.000270328976
NL: Newton 2 ; 4.1940252e-15 1.09185059e-12
NL: Newton Converged
NL: Newton 0 ; 0.00330833438 1
NL: Newton 1 ; 7.48907119e-07 0.000226369838
NL: Newton 2 ; 2.88875469e-15 8.73174944e-13
NL: Newton Converged
NL: Newton 0 ; 0.000961956933 1
NL: Newton 1 ; 6.33961917e-08 6.59033576e-05
NL: Newton 2 ; 2.4572528e-16 2.55443119e-13
NL: Newton Converged
Optimization terminated successfully    (Exit mode 0)
            Current function value: 0.023417738818650977
            Iterations: 14
            Function evaluations: 19
            Gradient evaluations: 14
Optimization Complete
-----------------------------------
Gamma = [0.06619126 0.0338087 ]
d = [7.78753175e-05 2.14643713e-05]
L = [0.99999968]
D = [0.02341774]
sigma = [0.99339689]
tresabhi@treslaptop:~/Projects/isu$ Opening in existing browser session.
[23:23:0100/000000.841593:ERROR:content/zygote/zygote_linux.cc:662] write: Broken pipe (32)
```

Thus, the values are:

$$
\Gamma = \begin{bmatrix}
  0.06619126 \\
  0.0338087
\end{bmatrix}
$$

$$
d = \begin{bmatrix}
  7.78753175 \times 10^{-5} \\
  2.14643713 \times 10^{-5}
\end{bmatrix}
$$

$$
L = 0.99999968
$$

$$
D = 0.02341774
$$

$$
\sigma = 0.99339689
$$

The MDF diagram with the "variable-specific arrows" is a good visualizer for the direction of data-flow:

![](https://i.imgur.com/3NjuxKO.png)

However, I did find looking at the "level 2" diagram (down from "level 3") to be easier to parse visually since it disregards the specific variables:

![](https://i.imgur.com/uND1qEI.png)

To make the problem an IDF, all I really have to do is make the residuals the difference between the solver's outputs and the passed estimate from the IDF loop.
