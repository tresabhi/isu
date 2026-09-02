# Tank Armor Optimization

AERE 463 Individual Project - Abhigyaan Deep

## Nomenclature

This passion subject of mine strays away from Aerospace Engineering quite a bit, so I shall describe a few terms that will be used in this project:

| Term         | Definition                                                                                                                                                          |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Armor        | A protective layer of material that blocks incoming projectiles from piercing through and damaging the interior of a vehicle.                                       |
| Plate        | A plate is a small, flat subsection of armor.                                                                                                                       |
| Shell        | A shell is a projectile that is fired from a tank, which can be thought of as a big bullet.                                                                         |
| AP           | Armor Piercing (AP) shells are simple inertia driven shells that pierce through armor.                                                                              |
| APCR         | Armor Penetrating Cartridge (APCR) shells are similar in idea to AP shells, but they use heavier cores instead of solely relying on the hard casing of an AP shell. |
| HE           | High Explosive (HE) shells, unlike inertia based shells, use explosives on contact to destroy armor.                                                                |
| HEAT         | High Explosive Anti-Tack (HEAT) shells concentrate a beam of molten armor right before coming into contact with armor to peirce through it.                         |
| Spall        | Spalling is the high-velocity chipping (the particles here are called spall) of armor off the interior walls of armor upon an external impact.                      |
| Spaced Armor | A layer of armor in front of the primary layer of armor to capture spall or counter HEAT shells.                                                                    |
| Tracks       | An assembly of a set of wheels wrapped around with a continuos band of linked metal plates, serving as the contacts with the ground for the vehicle.                |

## Problem Statement

Given minimum volumetric and maximum geometric complexity constraints, the optimizer must find the best armor profile for the hull and turret of a tank while minimizing weight and size and maximizing the resistance coefficient, when facing a classic $122mm$ AP shell weighing $25kg$ traveling at $790m/s$, as was often fired by the IS-2 tank in WW2.

## Meshing The Armor

All blocks of armor for this project will be rectangular meshes of size $w \times h$, made up of $N \times M$ vertices. This implies the resolution of the mesh is:

$$
\left ( \Delta x, \Delta y \right ) = \left ( \frac{w}{N}, \frac{h}{M} \right )
$$

As a user, I will have manual control over the resolution ($\Delta x$ and $\Delta y$) and the size of the armor plan ($w$ and $h$). So, really, the computer is responsible for computing:

$$
\left ( N, M \right ) = \left ( \frac{w}{\Delta x}, \frac{h}{\Delta y} \right )
$$

Much like computer graphics, a relation that will because naturally obvious as I later explain, a group of $3$ vertices form a triangle. A mesh with $N \times M$ vertices will have $2 (N - 1) (M - 1)$ triangle. I have illustrated everything discussed here below:

![](https://i.imgur.com/YxdPdht.png)

## Control Nodes: Vertices

Every vertex of the mesh I discussed before can be controlled. However, the axis of perturbation will be limited to just the $z$ axis while the $x$ and $y$ components of the vertices are determined by the resolution of the mesh, as shown below:

![](https://i.imgur.com/lKGBVUQ.png)

## Control Nodes: Thicknesses

For every group of $3$ vertices, a thickness will be stored. This contributes to the total mass which I am trying to minimize while improving the effectiveness. The mass is given by a simplified formula that disregards the slop of the armor, made even simpler as the $x$ and $y$ components of the vertices are fixed to the grid of resolution $\Delta x$ and $\Delta y$:

$$
m_i = \rho \left ( \frac{1}{2} \Delta x \Delta y \right) t_i
$$

![](https://i.imgur.com/mIjqAld.png)

## Objective Function: Weight

The total mass across armor plate would simply be a sum:

$$
m = \sum_i m_i
$$

## Object Function: Armor Resistance

This is where the meat of the heuristic based armor performance model comes in. Computing the effectiveness for all possible shells from all possible angles for all possible spots on the armor is impractical for a project of this scope. Thus, I will be using the heuristic Krupp formula described in the book _WWII Ballistics: Armor and Gunnery_ by Lorrin Rexford Bird and Robert D. Livingston:

$$
B = \frac{V \sqrt{P}}{K \sqrt{D}}
$$

Here $B$ is the thickness of the armor, $V$ is the velocity of the shell, $P$ is the mass of the shell, $K$ is the resistance factor, and $D$ is the diameter of the shell.

It's of course $K$ that we're trying to optimize here, just I will be using this form of the Krupp formula:

$$
K = \frac{V \sqrt{P}}{B \sqrt{D}}
$$

Looking at this formula, one may be concerned about the units:

$$
\left[ \frac{V \sqrt{P}}{B \sqrt{D}} \right] = \frac{m/s \sqrt{kg}}{m \sqrt{m}}
$$

That does not simplify to anything meaningful. This is a quirk of notation abuse. Really, the Krupp formula is a proportionality discovered through the Buckingham theorem:

$$
K \propto \frac{V \sqrt{P}}{B \sqrt{D}}
$$

However, if we use standard units of this field ($[V] = m/s$, $[P] = kg$, $[B] = mm$, $[D] = mm$), we get $K$ in the correct magnitudes. For reference, the standard $K$ value for Soviet Union armor in WW2 was $K = 2400$. I am of course hoping to beat this value.

The story does not stop here. The thickness of the armor is dependant on the angle of the armor:

![](https://i.imgur.com/Raz5oHM.png)

The effective thickness for an armor plate of thickness $t_i$ is:

$$
\cos \theta_i = \frac{t_i}{t_i'} \implies t_i' = t_i \sec \theta_i
$$

$B$ can be swapped out with $t_i'$:

$$
K = \frac{V \sqrt{P}}{t_i \sec \theta_i \sqrt{D}} = \frac{V \sqrt{P}}{t_i \sqrt{D}} \cos \theta_i
$$

The last thing we need is the angle of the armor plate $\theta_i$. Thankfully, this is a solved problem directly coming from computer graphics. We define our vertices in a counter-clockwise fashion:

![](https://i.imgur.com/lKGBVUQ.png)

This lets us define the positions of our vertices in order:

$$
\left( 0, 0, v_0 \right) \\
\left( \Delta x, 0, v_1 \right) \\
\left( \Delta x, \Delta y, v_2 \right) \\
$$

This triangle has the classic winding order of $0 \to 1 \to 2$ so we can use $v_0 \to v_1$ and $v_0 \to v_2$ for form the orthogonal vectors of the triangle:

![](https://i.imgur.com/JWWj7A4.png)

Those vectors are:

$$
\left( \Delta x, 0, v_1 \right) - \left( 0, 0, v_0 \right) = \left( \Delta x, 0, v_1 - v_0 \right) \\
\left( \Delta x, \Delta y, v_2 \right) - \left( 0, 0, v_0 \right) = \left( \Delta x, \Delta y, v_2 - v_0 \right)
$$

The normal vector of these two vectors would be:

$$
\vec{n} = \begin{bmatrix}
  (v_0 - v_1) \Delta y \\
  (v_1 - v_2) \Delta x \\
  \Delta x \Delta y
\end{bmatrix}
$$

Finally, we arrive at $\theta$:

$$
\cos \theta_i = \hat{n} \cdot \hat{k} = \frac{\vec{n}}{|\vec{n}|} \cdot \hat{k}
$$

The $\hat{k}$ simply strips the everything but the $z$ component, so we get:

$$
\cos \theta_i = \frac{\Delta x \Delta y}{|\vec{n}|}
$$

And here, $|\vec{n}|$ of course is:

$$
|\vec{n}| = \sqrt{(v_0 - v_1)^2 \Delta y^2 + (v_1 - v_2)^2 \Delta x^2 + \Delta x^2 \Delta y^2}
$$

The total resistance factor for a complete plate is:

$$
K = \sum_i K_i
$$

$$
K_i = \frac{V \sqrt{P}}{t_i \sqrt{D}} \cos \theta_i
$$

$$
\cos \theta_i = \frac{\Delta x \Delta y}{|\vec{n}_i|}
$$

$$
|\vec{n}_i| = \sqrt{(v_{i0} - v_{i1})^2 \Delta y^2 + (v_{i1} - v_{i2})^2 \Delta x^2 + \Delta x^2 \Delta y^2}
$$

## Object Function: Everything Put Together

$m$ must be decreased while $K$ should be increased. Thus, they are combined here in a fraction:

$$
f(m_0, m_1, \dots, m_n, v_0, v_1, \dots, v_n) = \frac{m}{K}
$$

## Simplifications and Assumptions: No Spaced Armor Over Tracks

It's somewhat common to dedicate the space above the tracks to spaced armor, as shown by the German E-100 below. I will not be optimizing this external spaced armor for this project. Thus, this will not be present in the mesh, leaving it completely rectangular, though I will be adding it for presentation purposes after the optimization.

![](https://i.imgur.com/tRosYnA.png)

## Simplifications and Assumptions: Rectangular Plates

While the a rectangular frontal projection of armor for hulls is extremely common for tanks even in the modern world, parts like the turrets often use cutouts on the sides as they're more exposed to incoming off-axis shots as often turn far more than the hull, as displayed by the American M1 Abrams:

![](https://i.imgur.com/VwAiJmp.png)
