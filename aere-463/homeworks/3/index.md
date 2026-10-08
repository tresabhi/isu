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

````py
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
````
