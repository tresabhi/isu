# AERE 463 Individual Project: Optimizing Frontal Tank Armor

## Introduction

Much like how we perform CFD analysis on wings as a whole in an attempt to optimize a certain objective function, given the constraints stemming from all aspects and disciplines of engineering, tanks find themselves in a similar need of optimization for their armor.

Designing the frontal protection for tanks is not a trivial task, often requiring balancing consumer requirements like effect thicknesses and mass ceilings with engineering constraints like minimum internal volumes and manufacturing complexities. Though this optimization problem was solved head first manually in the era of the World Wars, I aim to use a more modern approach.

My goal is to optimize the armor for the frontal plate of a tank using empirical formulations from the early days of armored vehicles using the modern tools of the computer age.

Though I do not doubt computer-aided optimization has been performed on modern tanks, I highly doubt it is common to combine the seemingly primitive formulations with OpenMDAO. My justification for why my project is unique is that my goal isn't to create the best armor mesh for a battle-ready tank, but to create a good enough, feasible design that a more granular solver could resume from, saving compute.

## Method

Constants:

Design variables:

| Variable | Description                                                                                                                                         |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| $v$      | A $(N+1) \times (M+1)$ matrix representing the depth of each vertex in the $z$ axis, constrained to a grid of fidelity $\Delta$ off the $xy$ plane. |

Constraints:

| Inequality                   | Description                                                                                                   |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------- |
| $v_{i, j} \ge v_{i, j, min}$ | The depth for any given vertex of the plate of armor should match or exceed the depth of the internal layout. |

## Formulation

## Results
