# Optimizing Tank Armor

AERE 463 Individual Project

## Nomenclature

This passion subject of mine strays away from Aerospace Engineering quite a bit, so I shall describe a few terms that will be used in this project:

| Term                | Definition                                                                                                                                            |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Armor               | A protective layer of material that blocks incoming projectiles from piercing through and damaging the interior of a vehicle.                         |
| Plate               | A small, usually flat, subsection of armor.                                                                                                           |
| Shell               | A projectile that is fired from a tank.                                                                                                               |
| AP                  | Armor Piercing shells are simple inertia driven shells that pierce through armor with their hard casing.                                              |
| APCR                | Armor Penetrating Composite Rigid shells are also inertia weapons, but they use dense cores instead of solely relying on the toughness of the casing. |
| HE                  | High Explosive shells use explosives on contact to destroy armor.                                                                                     |
| HEAT                | High Explosive Anti-Tack shells concentrate a beam of molten metal onto a tiny area of the armor, melting and piercing through.                       |
| Spall               | Spalling is the high-velocity chipping of the interior surfaces of armor, causing injuries to the crew and damage to the equipment.                   |
| Spaced armor        | A layer of armor in front of the primary one to prematurely trigger HEAT shells and capture spall.                                                    |
| Tracks              | The chassis of a tank with treads and wheels.                                                                                                         |
| Effective thickness | The increased thickness of armor due to the angle of the plate.                                                                                       |

## Problem Statement

Given constraints on the minimum volume enclosed by the hull and turret and an effective thickness that all armor plates must match, the optimizer must minimize the mass of the armor and the manufacturing complexity.

Different manufacturing complexities will produce different results, all of which will be documented in this report.

The armor is subject to a frontal confrontation with the enemy firing $122mm$ AP shell weighing $25kg$ and traveling at $790m/s$, as was often fired by the Soviet IS-2 tank in WW2.

## Meshing Generation

All blocks of armor for this project will be rectangular meshes of size $w \times h$, made up of $N \times M$ vertices. This implies the resolution of the mesh is:

$$
\left ( N, M \right ) = \left ( \frac{w}{\Delta} + 1, \frac{h}{\Delta} + 1 \right )
$$

Inspired by computer graphics, a group of $3$ vertices form a triangle. A mesh with $N \times M$ vertices will have $2 (N - 1) (M - 1)$ triangles:

![](https://i.imgur.com/cPmccMj.png)

## Vertices

Every vertex of the mesh is a control node. However, the axis of perturbation will be limited to just the $z$ axis while the $x$ and $y$ components of the vertices are determined by the resolution of the mesh, aligned to a uniform grid.

![](https://i.imgur.com/lKGBVUQ.png)

## Armor Mass

For every group of $3$ vertices, a thickness will be available for mutation. An increase in thickness improves the effectiveness of the armor while also increasing the mass. The mass is given by:

$$
m_i = \rho A_i t_i
$$

Computing $A_i$ for a plate of armor will be discussed later.

![](https://i.imgur.com/mIjqAld.png)

## Wall Mass

To discourage the optimizer front infinitely expanding the armor forwards, away from the tank as it wrestles with optimization, the total mass will also include the mass of the walls.

For every pair of vertices on the edge of the block of armor, a wall mass will be computed, using a thickness $t_w$. For instance, this is the mass of a vertical wall with vertices $v_0$ and $v_1$:

$$
m_j = \frac{v_0 + v_1}{2} \Delta t_w \rho = \frac{1}{2} t_w \rho (v_0 + v_1) \Delta
$$

![](https://i.imgur.com/SdHspWx.png)

## Effective Armor Thickness

The thickness of every plate of armor does not paint the full picture. The angle the plate lies at changes the effective thickness:

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

## Volumetric Constraints

The insides of a tank are filled with equipment, crew, ammunition bays, vision ports, etc. Thus, there is a minimum volume that must be enclosed by the armor. A large tank is also not desirable due to cross-sectional considerations for stealth and added mass. In this project, the volumetric constrain will be represented by a minimum depth a vertex can be.

$$
v_i \ge v_{i, \text{min}}
$$

This minimum depth mesh will be defined by the user. In the case of this project, the internal layout of the Chinese 114 SP2 will be used:

![](https://i.imgur.com/SDXCtdp.png)

## Manufacturing Complexity

I haven't decided how this is evaluated yet.

## Objective Function

For every triangle, the following can be computed:

$$
|\vec{n}_i| = \sqrt{(v_0 - v_1)^2 \Delta^2 + (v_1 - v_2)^2 \Delta^2 + \Delta^2 \Delta^2}
$$

$$
A_i = \frac{|\vec{n}_i|}{2}
$$

$$
\cos \theta_i = \frac{\Delta \Delta}{|\vec{n}_i|}
$$

$$
t_i' = \frac{t_i}{\cos \theta_i}
$$

$$
m_i = \rho A_i t_i
$$

For every edge vertex pair, the wall mass will be:

$$
m_j = \frac{1}{2} t_w \rho (v_0 + v_1) \Delta
$$

The total mass of the block of armor would be:

$$
\mu = \sum_i m_i + \sum_j m_i'
$$

And the total effective thickness would be:

$$
\tau = \sum_i t_i'
$$

Thus, the objective function is:

$$
f \left( \begin{bmatrix}
  v_0 \\
  v_1 \\
  \vdots \\
  v_{NM}
\end{bmatrix}, \begin{bmatrix}
  t_0 \\
  t_1 \\
  \vdots \\
  t_{2 (N - 1) (M - 1)}
\end{bmatrix} \right) =  \frac{ \gamma \mu}{\tau}
$$

## Simplification: Spaced Armor Over Tracks

It's somewhat common to dedicate the space above the tracks to spaced armor, as shown by the German E-100 below. I will not be optimizing this external spaced armor for this project. Thus, this will not be present in the mesh, leaving it completely rectangular, though I will be adding it for presentation purposes after the optimization.

![](https://i.imgur.com/tRosYnA.png)

## Simplification: Rectangular Plates

While the a rectangular frontal projection of armor for hulls is extremely common for tanks even in the modern world, parts like the turrets often use cutouts on the sides as they're more exposed to incoming off-axis shots as often turn far more than the hull, as displayed by the American M1 Abrams:

![](https://i.imgur.com/VwAiJmp.png)

## Simplification: Regions of Protection

I am calculating the resistance here as a giant sum of all plates. In reality, you would assign higher weights to some plates than others to diminish/increase their significance, depending on factors like crew survivability, visibility, etc. This is ignored for this project.
