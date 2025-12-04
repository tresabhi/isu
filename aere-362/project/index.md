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

### $C_L$ and $C_D$ as Functions of $\alpha$

This is going to be a very low resolution figure since there are only 3 points of data. The data tabulated:

| $\alpha$ (deg) | $C_L$      | $C_D$      |
| -------------- | ---------- | ---------- |
| 1              | 0.10339017 | 0.01247696 |
| 2              | 0.20600859 | 0.01308758 |
| 3              | 0.30687305 | 0.01411271 |

The code to plot the data above:

```m
alpha = [1, 2, 3];
CL = [0.10339017, 0.20600859, 0.30687305];
CD = [0.01247696, 0.01308758, 0.01411271];

figure;
plot(alpha, CL, 'o-');
xlabel('\alpha (deg)');
ylabel('C_L');
title('Lift Coefficient vs Angle of Attack');
grid on;

figure;
plot(alpha, CD, 'o-');
xlabel('\alpha (deg)');
ylabel('C_D');
title('Drag Coefficient vs Angle of Attack');
grid on;
```

And the plots:

![](https://i.imgur.com/Fi1VC2y.png)

![](https://i.imgur.com/NVVvlfa.png)

### CFD Meshes

It is unclear what mesh the project wants exactly, so I will be displaying both the external mesh surface with edges and the border surface without edges.

![](https://i.imgur.com/3tVnRt5.png)

![](https://i.imgur.com/Bc7qU21.png)
