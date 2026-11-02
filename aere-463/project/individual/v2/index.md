# AERE 463 Individual Project: Optimizing Frontal Tank Armor

## Introduction

Much like how we perform CFD analysis on wings as a whole in an attempt to optimize a certain objective function, given the constraints stemming from all aspects and disciplines of engineering, tanks find themselves in a similar need of optimization for their armor.

Designing the frontal protection for tanks is not a trivial task, often requiring balancing consumer requirements like effect thicknesses and mass ceilings with engineering constraints like minimum internal volumes and manufacturing complexities. Though this optimization problem was solved head first manually in the era of the World Wars, I aim to use a more modern approach.

My goal is to optimize the armor for the frontal plate of a tank using empirical formulations from the early days of armored vehicles using the modern tools of the computer age.

Though I do not doubt computer-aided optimization has been performed on modern tanks, I highly doubt it is common to combine the seemingly primitive formulations with OpenMDAO. My justification for why my project is unique is that my goal isn't to create the best armor mesh for a battle-ready tank, but to create a good enough, feasible design that a more granular solver could resume from, saving compute.

## Nomenclature

| Term  | Definition |
| ----- | ---------- |
| Shell |            |
| Quad  |            |

## Method

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

## Formulation

## Results
