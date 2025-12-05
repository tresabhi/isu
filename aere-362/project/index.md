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

**Figure 1:** converged plots for airfoil at $\alpha = 1\degree$.

![](https://i.imgur.com/zHL8d4R.png)

**Figure 2:** converged plots for airfoil at $\alpha = 2\degree$.

![](https://i.imgur.com/6tIWheM.png)

**Figure 3:** converged plots for airfoil at $\alpha = 3\degree$.

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

**Figure 4:** $C_L$ vs $\alpha$.

![](https://i.imgur.com/NVVvlfa.png)

**Figure 5:** $C_D$ vs $\alpha$.

### CFD Meshes

It is unclear what mesh the project wants exactly, so I will be displaying both the external mesh surface with edges and the border surface without edges for the $\alpha = 3\degree$ case.

![](https://i.imgur.com/3tVnRt5.png)

**Figure 6:** mesh for $\alpha = 3\degree$ showing the external surface with edges.

![](https://i.imgur.com/Bc7qU21.png)

**Figure 7:** mesh for $\alpha = 3\degree$ showing the border surface without edges.

### Pressure Profile

The pressure profile for the $\alpha = 3\degree$ case is shown below:

![](https://i.imgur.com/d15lmxf.png)

**Figure 8:** pressure profile for the $\alpha = 3\degree$ case.

## Task 2. Airfoil Aerodynamic Optimization

### What's Being Optimized

Unlike what we have primarily discussed in class so far (reducing drag), the optimization problem for this project is attainting a desired lift coefficient. More specifically, I need to let the NACA 0012 airfoil evolve to achieve a $C_L \geq 0.3$, also known as the object function at a low level. The design variables compose the mesh of the airfoil. It is implicit that one of the greatest constraints is the equality of the airfoil across the span of the wing. I say this is implicit since we're not optimizing all slices of the wing in one go, just one airfoil, mutating the entire wing together. All of this is subject to the scenario of Mach 0.04 and Reynolds number of 3000000.

### How It's Optimized

The geometry-parametrization module takes control-point design variables and generates an updated geometry. This feeds the mesh-deformation module, which adjusts the original volume mesh to match the new boundary. The resulting mesh goes to the CFD solver, which computes the flow field. Using this flow solution, the discrete-adjoint solver evaluates sensitivities of objectives and constraints with respect to the design variables. These gradients are then used by the optimization module to update the design variables, which are sent back to the geometry-parametrization stage, completing the loop.

### Optimized NACA 0012

It shouldn't be surprising to see such a tiny difference in $C_L$ since the wing could already achieve $C_L = 3.0$ even before the optimization.

![](https://i.imgur.com/5ZuotS2.png)

**Figure 9:** optimized graphs for NACA 0012 airfoil at MACH 0.04 and Reynold's number 3000000.

The drag, however, was reduced while keeping the lift constant which is impressive. The reduction:

$$
C_D^0 = 0.01402712
$$

$$
C_D^1 = 0.01255188
$$

$$
R = 1 - \frac{0.01255188}{0.01402712} = 0.10517056 = \boxed{10.517056\%}
$$

### Comparing Meshes

Here's the baseline and optimized meshes:

![](https://i.imgur.com/At3UU72.png)

**Figure 10:** baseline mesh for NACA 0012.

![](https://i.imgur.com/Ra8nSM6.png)

**Figure 11:** optimized mesh.

### Optimality and Feasibility Over Iterations

The feasibility and optimality can be gleaned from `logMeshGeneration.txt` from which an excerpt can be seen below.

$$
\text{feasibility} = \boxed{3.54 \times 10^{-8}}
$$

$$
\text{optimality} = \boxed{7.53 \times 10^{-7}}
$$

```
iter    objective    inf_pr   inf_du lg(mu)  ||d||  lg(rg) alpha_du alpha_pr  ls
   0  1.4027120e-02 4.23e-06 7.40e-03   0.0 0.00e+00    -  0.00e+00 0.00e+00   0
   1  1.3954881e-02 6.84e-05 4.33e-02  -5.9 7.17e-03    -  9.56e-01 1.00e+00h  1
   2  1.3634575e-02 4.77e-04 1.84e-01  -7.3 1.34e-02    -  9.77e-01 1.00e+00h  1
   3  1.3262222e-02 7.53e-04 1.81e-03  -4.8 7.03e-02    -  9.65e-01 1.00e+00h  1
   4  1.3043721e-02 3.03e-05 3.64e-03  -5.5 9.61e-02    -  1.00e+00 1.00e+00h  1
   5  1.2941941e-02 4.03e-05 2.05e-03  -6.7 1.37e-01    -  1.00e+00 9.01e-01h  1
   6  1.2929342e-02 5.21e-05 1.98e-03  -6.0 9.55e-02    -  1.00e+00 1.00e+00h  1
   7  1.2921503e-02 2.36e-04 6.81e-03  -6.4 1.32e-01    -  1.00e+00 1.00e+00h  1
   8  1.2812992e-02 1.39e-04 8.40e-03  -6.7 3.06e-01    -  1.00e+00 1.00e+00h  1
   9  1.2794951e-02 4.90e-04 1.11e-02  -6.4 3.35e+00    -  1.00e+00 8.49e-02h  4
  10  1.2641569e-02 1.61e-03 2.04e-02  -7.1 1.22e+00    -  1.00e+00 1.00e+00h  1
  11  1.2646263e-02 1.06e-03 2.39e-02  -5.1 1.96e+00    -  1.00e+00 4.68e-01h  1
  12  1.2596219e-02 2.20e-04 2.46e-03  -5.2 6.50e-01    -  1.00e+00 1.00e+00h  1
  13  1.2560692e-02 6.60e-06 6.58e-04  -5.7 6.48e-02    -  1.00e+00 9.86e-01h  1
  14  1.2552388e-02 7.99e-06 3.17e-04  -6.9 2.29e-02    -  1.00e+00 1.00e+00h  1
  15  1.2551895e-02 4.10e-07 3.41e-06  -8.4 5.51e-03    -  1.00e+00 1.00e+00h  1
  16  1.2551881e-02 5.99e-08 6.66e-06 -10.4 1.16e-03    -  1.00e+00 1.00e+00h  1
  17  1.2551880e-02 3.32e-09 9.16e-06 -11.0 1.94e-04    -  1.00e+00 1.00e+00h  1
  18  1.2551879e-02 2.13e-09 2.08e-06 -11.0 2.40e-03    -  1.00e+00 1.00e+00h  1
  19  1.2551880e-02 1.17e-09 5.64e-06 -11.0 1.10e-03    -  1.00e+00 1.00e+00H  1
  20  1.2551879e-02 2.27e-08 4.73e-06 -11.0 1.01e-03    -  1.00e+00 1.00e+00h  1
  21  1.2551883e-02 1.09e-08 1.60e-05 -11.0 1.90e-03    -  1.00e+00 1.00e+00h  1
  22  1.2551878e-02 1.73e-08 1.92e-06 -11.0 1.87e-03    -  1.00e+00 1.00e+00h  1
  23  1.2551881e-02 1.11e-09 7.01e-06 -11.0 7.55e-04    -  1.00e+00 1.00e+00H  1
  24  1.2551878e-02 4.08e-08 5.81e-06 -11.0 4.42e-04    -  1.00e+00 1.00e+00h  1
  25  1.2551879e-02 3.54e-08 7.53e-07 -11.0 1.07e-03    -  1.00e+00 1.00e+00h  1
```
