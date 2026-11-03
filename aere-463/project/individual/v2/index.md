# AERE 463 Individual Project: Optimizing Frontal Tank Armor

## Introduction

Much like how we perform CFD analysis on wings as a whole in an attempt to optimize a certain objective function, given the constraints stemming from all aspects and disciplines of engineering, tanks find themselves in a similar need of optimization for their armor.

Designing the frontal protection for tanks is not a trivial task, often requiring balancing consumer requirements like effect thicknesses and mass ceilings with engineering constraints like minimum internal volumes and manufacturing complexities. Though this optimization problem was solved head first manually in the era of the World Wars, I aim to use a more modern approach.

My goal is to optimize the armor for the frontal plate of a tank using empirical formulations from the early days of armored vehicles using the modern tools of the computer age.

Though I do not doubt computer-aided optimization has been performed on modern tanks, I highly doubt it is common to combine primitive WW1 formulations with OpenMDAO. My justification for why my project is unique is that my goal isn't to create the best armor mesh for a battle-ready tank, but to create a good enough, feasible design that a more granular solver could resume from, saving compute overall.

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

## Code

## Results

## Discussion

## Summary
