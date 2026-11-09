# AERE 463 Individual Project: Optimizing Frontal Tank Armor

## Introduction

Much like how we perform CFD analysis on wings as a whole in an attempt to optimize a certain objective function, given the constraints stemming from all aspects and disciplines of engineering, tanks find themselves in a similar need of optimization for their armor.

Designing the frontal protection for tanks is not a trivial task, often requiring balancing consumer requirements like effect thicknesses and mass ceilings with engineering constraints like minimum internal volumes and manufacturing complexities. Though this optimization problem was solved head first manually in the era of the World Wars, I aim to use a more modern approach.

My goal is to optimize the armor for the frontal plate of a tank using empirical formulations from the early days of armored vehicles using the modern tools of the computer age.

Though I do not doubt computer-aided optimization has been performed on modern tanks, I highly doubt it is common to combine primitive WW1 formulations with OpenMDAO. My justification for why my project is unique is that my goal isn't to create the best armor mesh for a battle-ready tank, but to create a good enough, feasible design that a more granular solver could resume from, saving compute overall.

In the process, I have come up with a unique set of novel formulations that I don't believe have been combined together in this manner. The meat of this project is the formulation itself. I highly encourage giving it an earnest read as I am quite proud of the organic nature of the results that stem from it.

## Literature Review

TODO

## Nomenclature

| Term     | Definition                                                                                                          |
| -------- | ------------------------------------------------------------------------------------------------------------------- |
| Shell    | The projectile that is fired from a tank.                                                                           |
| Quad     | A pair of triangles in a mesh that form a rectangle. In my project, they always for a square. There's $NM$ of them. |
| Triangle | In this context, a triangle is identical to the one from computer graphics. There's $2NM$ of them.                  |

## Technical Approach

### Constants

| Variable                             | Description                                                                    |
| ------------------------------------ | ------------------------------------------------------------------------------ |
| $N = 15$                             | Number of segmentation horizontally.                                           |
| $M = 10$                             | Number of segmentation vertically.                                             |
| $w = 3 \text{m}$                     | Width of the armor plate.                                                      |
| $\rho = 7850 \text{kg} / \text{m}^3$ | Density of the material used for the armor plate. This is steel.               |
| $t_\text{effective} = 120 \text{mm}$ | The effective thickness of armor that the optimizer must attain at all places. |
| $t_\text{wall} = 5 \text{mm}$        | The thickness of the side wall of the armor.                                   |

### Derived Constants

| Variable         | Description                |
| ---------------- | -------------------------- |
| $\Delta = w / N$ | Quad spacing.              |
| $h = M \Delta$   | Height of the armor plate. |

### Design Variables

| Variable           | Description                                                                                                                                                                         |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $v ~ [\text{m}]$   | A $(N+1) \times (M+1)$ matrix representing the depth of each vertex in the $z$ axis, constrained to a grid of fidelity $\Delta$ off the $xy$ plane.                                 |
| $t ~ [\text{mm}]$  | A $N \times M \times 2$ tensor representing the thickness of every triangle in the armor mesh. Please see the formulation below to see why I am using a tensor instead of a matrix. |
| $t' ~ [\text{mm}]$ | A $N \times M \times 2$ tensor representing the effective thickness of every triangle in the armor mesh from the perspective of a shell traveling in the negative $z$ direction.    |

### Outputs

| Variable          | Description                                                                                                                                                                                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| $m ~ [\text{kg}]$ | A scalar representing the total mass of the plate of armor.                                                                                                                                                                                            |
| $\gamma$          | A sum of scalars measuring the concavity of the armor when viewed from the negative $z$ direction. This is used purely to nudge the solver out of ambiguous degenerate critical points. Please see the Results section to see why this was introduced. |

### Constraints

| Inequality                   | Description                                                                                                                                                                                         |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $v_{i, j} \ge v_{i, j, min}$ | The depth for any given vertex of the plate of armor should match or exceed the depth of the internal layout.                                                                                       |
| $\gamma \le 0$               | Negative concavity encourages the solver to produce a convex design which is a desirable characteristic for the frontal armor of a tank. Please see formulation for more information on this topic. |

### Objective Function

The optimizer must minimize $m$, the total mass of the armor by perturbing $v$ and $t$, given constraints on their minimum depths and required effective thicknesses, using OpenMDAO. The optimizer will be aided with a $\gamma$ term to gently guide the solver towards a convex solution.

Though it is common to use $\text{mm}$ and $\text{m}$ together in this field, everything in my work will be normalized to just $\text{m}$, with `ref` values passed into the solver to help it scale the values better.

## Formulation

### Mesh Grid

The plate of armor will be split into quads across a $N \times M$ grid, spaced apart by $\Delta$, split into triangles, all formed by vertices that can be perturbed in just the $z$ axis, normal to the screen. The total width and height of the plate of armor will be $w$ and $h$ respectively.

![](https://i.imgur.com/cPmccMj.png)

In my code, $N$, $M$, and $w$ are well defined. The rest must be recovered, starting off with the resolution $\Delta$:

$$
\Delta = \frac{w}{N}
$$

From this, the height can be calculated, assuming a perfectly square quad:

$$
h = M \Delta
$$

Each pair of triangles will be stored as 2 components of each element of a $N \times M$ matrix. So, really, it's a $N \times M \times 2$ tensor. In my experience, flattening this out made my code unnecessarily complex.

### Vertex Depths

Every vertex of the mesh is a controllable node. However, the axis of perturbation will be limited to just the $z$ axis while the $x$ and $y$ components of the vertices are determined by the resolution of the mesh, aligned to a uniform grid.

![](https://i.imgur.com/lKGBVUQ.png)

### Armor Mass

For every triangle, a thickness will be computable. An increase in thickness improves the effectiveness of the armor, but at the expense of increasing the mass. The mass is given by a product of the area of the triangle and its thickness, giving us the volume, which is then multiplied to the density:

$$
m_i = \rho A_i t_i
$$

Computing $A_i$ for a triangle will be discussed later.

![](https://i.imgur.com/mIjqAld.png)

### Wall Mass

To discourage the optimizer from infinitely expanding the armor forwards, away from the tank as it wrestles with optimization, the total mass will also include the mass of the walls.

For every pair of vertices on the edge of the block of armor, a wall mass will be computed, using a thickness $t_w$. Similar to before, the volume of this trapezoid will be its area times its thickness times the density. The thickness of the side walls is constant:

$$
m_j = \rho \frac{v_0 + v_1}{2} t_\text{wall} \Delta = \frac{1}{2} \rho (v_0 + v_1) t_\text{wall} \Delta
$$

![](https://i.imgur.com/SdHspWx.png)

### Total Mass

The total mass is the sum of every triangle and trapezoid from the frontal armor and the side walls respectively:

$$
m = \sum m_i + \sum m_j
$$

### Effective Thickness

The thickness of every plate of armor does not paint the full picture. The angle the plate lies with respect to the oncoming shell changes the "effective" thickness observed by the shell. In other words, the effective thickness of a plate of armor grows when it is angled. Mass can be saved by angling a plate of armor and reducing its nominal thickness to achieve the same effective thickness at a lower mass deficit:

![](https://i.imgur.com/Raz5oHM.png)

The effective thickness for an armor plate of thickness $t_i$ is:

$$
\cos \theta_i = \frac{t_i}{t_i'} \implies t_i' = \frac{t_i}{\cos \theta_i}
$$

An equation for $\theta_i$ is needed. Thankfully, this is a well known and solved problem in computer graphics. We define our vertices in a counter-clockwise fashion on the $xy$ plane with extrusion happening along the $z$ axis:

![](https://i.imgur.com/A3DtI8M.png)

This lets us define the positions of our vertices in the standard winding order in computer graphics:

$$
(0, 0, v_0) \\
(\Delta, 0, v_1) \\
(0, \Delta, v_2) \\
$$

We can use the edges of this triangle to get a normal vector. Those edges are:

$$
(0, 0, v_0) - (\Delta, 0, v_1) = (-\Delta, 0, v_0 - v_1) \\
(0, \Delta, v_2) - (\Delta, 0, v_1) = (-\Delta, \Delta, v_2 - v_1)
$$

A straight forward cross product can be used to get a normal vector:

$$
\vec{n}
= (-\Delta, \Delta, v_2 - v_1) \times (-\Delta, 0, v_0 - v_1)
= \left( (v_0 - v_1) \Delta, ~ (v_0 - v_2) \Delta, ~ \Delta^2 \right)
$$

Since we're evaluating the performance for a head-on confrontation, the incoming shells will follow a path parallel to the $z$ axis. Thus our normal vector to use for the dot product when computing $\theta$ will be $\hat{k} = \left( 0, 0, 1 \right)$:

$$
\cos \theta = \frac{\vec{n}}{|\vec{n}|} \cdot \hat{k} = \frac{\vec{n} \cdot \hat{k}}{|\vec{n}|}
$$

The dot product with $\hat{k}$ in the numerator strips the everything but the $z$ component:

$$
\cos \theta_i = \frac{\Delta^2}{|\vec{n}_i|}
$$

And here, $|\vec{n}_i|$ of course is:

$$
|\vec{n}_i| = \sqrt{(v_0 - v_1)^2 \Delta^2 + (v_0 - v_2)^2 \Delta^2 + \Delta^4} = \Delta \sqrt{(v_0 - v_1)^2 + (v_0 - v_2)^2 + \Delta^2}
$$

Another property of the cross product is of course the area of the prism that it forms, half of which is the area of the triangle:

$$
A_i = \frac{|\vec{n}_i|}{2}
$$

$A_i$ as shown here can be used up above for the masses, as discussed previously.

### Concavity

Usually, armor performs best if it is convex as a concave plate of armor would "trap" the shell, causing further damage even after a ricochet.

![](https://i.imgur.com/WTnk0j6.png)

However, the optimizer gets no input in what it means to have a bad ricochet that lands the shell right back into the tank, so it often had a hard time picking between the two designs when on a degenerate critical point.

To nudge it into the right direction, I introduced $\gamma$ to keep track of the sum of the concavity at all points, with a constraint that it be negative to encourage convexity:

$$
\gamma \le 0
$$

The formulation thus far has been my work. However, my formulation for the curvature always produced edge causes where it'd give the solver a hard time for infliction points. So, I look up a formulation on the internet, which resulted in a very robust equation, thanks to the simplicity of my grid distribution of vertices.

For a smooth surface $z = v(x, y)$, concavity is described by the second derivatives $\partial^2 v / \partial x^2$ and $\partial^2 v / \partial y^2$. My surface is sampled on a uniform grid with spacing $\Delta$, so these are approximated with central finite differences. For an interior vertex $(i, j)$:

$$
\frac{\partial^2 v}{\partial x^2} \approx \frac{v_{i+1,j} - 2 v_{i,j} + v_{i-1,j}}{\Delta^2} \qquad
\frac{\partial^2 v}{\partial y^2} \approx \frac{v_{i,j+1} - 2 v_{i,j} + v_{i,j-1}}{\Delta^2}
$$

Because $\Delta$ is constant across the whole mesh, it can be factored out and absorbed into the weighting of the term. I therefore define the unscaled second differences:

$$
d_{xx,i,j} = v_{i+1,j} - 2 v_{i,j} + v_{i-1,j} \\
d_{yy,i,j} = v_{i,j+1} - 2 v_{i,j} + v_{i,j-1}
$$

These are only defined for interior vertices, $1 \le i \le N-1$ and $1 \le j \le M-1$, since boundary vertices lack a neighbor on one side. Boundary vertices are already controlled by the minimum depth constraint and the wall mass.

Each second difference compares a vertex to the average of its two neighbors:

$$
d_{xx,i,j} = 2\left(\frac{v_{i+1,j} + v_{i-1,j}}{2} - v_{i,j}\right)
$$

- $d > 0$: the vertex sits behind the midpoint of its neighbors, forming a valley. This is concave, and it traps shells.
- $d < 0$: the vertex sits in front of the midpoint of its neighbors, forming a ridge. This is convex, and it deflects shells.
- $d = 0$: the vertex lies on the line between its neighbors, which is locally flat.

Only concave (positive) contributions should be penalized, so convexity is not punished. Negative values are clipped with $\max(\cdot, 0)$, the same hinge used in a ReLU, and the results are summed over every interior vertex and both axes:

$$
\gamma = \sum_{i=1}^{N-1} \sum_{j=1}^{M-1} \left[ \max(d_{xx,i,j}, 0) + \max(d_{yy,i,j}, 0) \right]
$$

## Code

I split up my code across many files to ensure ease of understanding. Starting with `__main__.py`, it handles the OpenMDAO optimization:

```py
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
        outputs["gamma"] = methods.concavity(v)
        outputs["t_prime"] = methods.effective_thickness(v, t)


model = om.Group()
model.add_subsystem("mass_component", MassComponent(), promotes=["*"])

problem = om.Problem(model)
problem.driver = om.ScipyOptimizeDriver(optimizer="SLSQP")


problem.model.add_design_var("v", lower=0.0, ref=1.0)
problem.model.add_design_var("t", lower=0.0, ref=config.t_effective)

problem.model.add_constraint("gamma", upper=0.0)
problem.model.add_constraint(
    "t_prime", lower=config.t_effective, ref=config.t_effective
)

problem.model.add_objective("m")

problem.setup()

problem.set_val("v", 1)
problem.set_val("t", config.t_effective * 2)

problem.run_driver()

plot.plot_mesh(problem.get_val("v"), problem.get_val("t"))
x
```

Another fundamental file in this project is `config.py` which stores a lot of my constants, all stored as scalars or base-SI units:

```py
N = 15  # horizontal node count [1]
M = 10  # vertical node count [1]

w = 3  # width [m]
Delta = w / N  # node spacing [m]
h = Delta * M  # height [m]

rho = 7850  # metal density [kg/m^3]

t_effective = 120 / 1000  # frontal effective thickness
t_wall = 5 / 1000  # side wall thickness [m]
```

The OpenMDAO class methods use the mass, effective thickness, and concavity functions defined in `methods.py` which are identical to my formulations discussed above:

```py
import config
import math
import numpy as np


def plate_mass(v, t):
    m = 0

    for y in range(config.M):
        for x in range(config.N):
            v1 = v[x + 1, y]  # bottom right
            v2 = v[x, y + 1]  # top left

            for j in range(2):
                if j == 0:
                    # bottom left corner
                    v0 = v[x, y]
                else:
                    # top right corner
                    v0 = v[x + 1, y + 1]

                abs_n_i = config.Delta * math.sqrt(
                    (v0 - v1) ** 2 + (v0 - v2) ** 2 + config.Delta**2
                )
                A_i = abs_n_i / 2

                t_i = t[x, y, j]

                m += config.rho * A_i * t_i

    return m


def wall_segment_mass(v0, v1):
    return 0.5 * config.t_wall * config.rho * (v0 + v1) * config.Delta


def wall_mass(v):
    m = 0

    # bottom wall
    for x in range(config.N):
        m += wall_segment_mass(v[x, 0], v[x + 1, 0])

    # top wall
    for x in range(config.N):
        m += wall_segment_mass(v[x, config.M], v[x + 1, config.M])

    # left wall
    for y in range(config.M):
        m += wall_segment_mass(v[0, y], v[0, y + 1])

    # right wall
    for y in range(config.M):
        m += wall_segment_mass(v[config.N, y], v[config.N, y + 1])

    return m


def effective_thickness(v, t):
    t_prime = np.zeros((config.N, config.M, 2))

    for y in range(config.M):
        for x in range(config.N):
            v1 = v[x + 1, y]  # bottom right
            v2 = v[x, y + 1]  # top left

            for j in range(2):
                if j == 0:
                    # bottom left corner
                    v0 = v[x, y]
                else:
                    # top right corner
                    v0 = v[x + 1, y + 1]

                abs_n_i = config.Delta * math.sqrt(
                    (v0 - v1) ** 2 + (v0 - v2) ** 2 + config.Delta**2
                )

                cos_theta_i = (config.Delta**2) / abs_n_i

                t_prime[x, y, j] = t[x, y, j] / cos_theta_i

    return t_prime


def concavity(v):
    d_xx = v[2:, 1:-1] - 2 * v[1:-1, 1:-1] + v[:-2, 1:-1]
    d_yy = v[1:-1, 2:] - 2 * v[1:-1, 1:-1] + v[1:-1, :-2]

    c = np.sum(np.maximum(d_xx, 0)) + np.sum(np.maximum(d_yy, 0))

    # print(c)

    return c
```

Finally, to present the results, I created `plot.py`. Visualizing both the depth and thickness was a challenge, but in the end `matplotlib` in combination with `mpl_toolkits` made coloring every triangle possible:

```py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import cm, colors
import config


def plot_mesh(v, t, show_walls=True, z_exaggeration=1.0, v_decimals=4, t_decimals=4):
    # round for display only; v to 0.1 mm, t to 0.1 mm
    v = np.round(v, v_decimals)
    t = np.round(t, t_decimals)

    N, M, D = config.N, config.M, config.Delta

    def p(ix, iy):
        return (ix * D, iy * D, v[ix, iy])

    tris, vals = [], []
    for iy in range(M):
        for ix in range(N):
            # j = 0: bottom left, bottom right, top left
            tris.append([p(ix, iy), p(ix + 1, iy), p(ix, iy + 1)])
            vals.append(t[ix, iy, 0])
            # j = 1: top right, bottom right, top left
            tris.append([p(ix + 1, iy + 1), p(ix + 1, iy), p(ix, iy + 1)])
            vals.append(t[ix, iy, 1])

    # fixed scale: 0 thickness = green, t_effective (or more) = red
    norm = colors.Normalize(vmin=np.min(vals), vmax=config.t_effective, clip=True)
    cmap = cm.RdYlGn_r  # green -> yellow -> red

    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(111, projection="3d")

    ax.add_collection3d(
        Poly3DCollection(
            tris,
            facecolors=cmap(norm(vals)),
            edgecolors="k",
            linewidths=0.8,
            alpha=0.95,
        )
    )

    if show_walls:
        walls = []
        for ix in range(N):  # bottom (iy = 0) and top (iy = M)
            for iy in (0, M):
                a, b = p(ix, iy), p(ix + 1, iy)
                walls.append([(a[0], a[1], 0), (b[0], b[1], 0), b, a])
        for iy in range(M):  # left (ix = 0) and right (ix = N)
            for ix in (0, N):
                a, b = p(ix, iy), p(ix, iy + 1)
                walls.append([(a[0], a[1], 0), (b[0], b[1], 0), b, a])
        ax.add_collection3d(
            Poly3DCollection(
                walls, facecolors="lightgray", edgecolors="gray", alpha=0.35
            )
        )

    z_max = max(v.max(), 1e-3) * 1.1
    ax.set_xlim(0, N * D)
    ax.set_ylim(0, M * D)
    ax.set_zlim(0, z_max)
    ax.set_box_aspect((N * D, M * D, z_max * z_exaggeration))
    ax.set_xlabel("x [m]")
    ax.set_ylabel("y [m]")
    ax.set_zlabel("v [m]")
    ax.view_init(elev=25, azim=-60)

    fig.colorbar(
        cm.ScalarMappable(norm=norm, cmap=cmap),
        ax=ax,
        shrink=0.6,
        label="t [m]",
    )
    plt.show()
```

## Results

## Discussion

## Summary
