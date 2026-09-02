# Tank Armor Optimization

AERE 463 Individual Project - Abhigyaan Deep

## Problem Statement

Given minimum volumetric and maximum geometric complexity constraints, the optimizer must find the best armor profile for the hull and turret of a tank while minimizing weight and size and maximizing armor effectiveness.

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

## Control Node: Vertex
