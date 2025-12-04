# AERE 362 Project

## Task 1: Airfoil Aerodynamic Analysis

### I/O of Aerodynamic Analysis Tools

Numerical aerodynamic solvers, commonly known as computational fluid dynamics, or CFD, traditionally accept meshes of the object in question, often in the `.stl` or `.step` format, along side parametric data such as the characteristics of the fluid the mesh will be submerged in (density, viscosity, Reynold's number, etc.) and a volume where the simulation will take place, composed of walls (cylindrical, planer, slipping, pressure outlet, etc.). In a converging system, the true actual outputs of solves include forces and moments, which are often converted to more relevant coefficients such as $C_L$, $C_D$, $C_m$, etc.

### Subject

I have been assigned the following criteria for this project.

- Airfoil: `NACA 0012`
- Mach number: `0.04`
- Reynolds number: `3000000`
- Target lift coefficient: `0.3`

### Analysis at $\alpha = 1\degree, 2\degree, 3\degree$

An incompressible flow analysis was run on the NACA 0012 airfoil using ParaView at angle of attacks of $1\degree, 2\degree, 3\degree$. Even with Docker installed on my computer, I chose to use the Nova HPC's instead, following the instructions from `21 Computer Lab.pdf`. The raw results can be found in the Canvas submission or [the GitHub directory associated with this project](https://github.com/tresabhi/isu/tree/main/aere-362/project).

pvOptAirfoil post processing of all three angles of attack:

![](https://i.imgur.com/gSAIkR6.png)

![](https://i.imgur.com/zHL8d4R.png)

![](https://i.imgur.com/6tIWheM.png)
