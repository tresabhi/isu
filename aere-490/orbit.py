import numpy as np
import math
import pyvista as pv

G = 6.6743
l_box = 0.5
m_box = 1000
r_sphere = 1
m_sphere = 1

sphere = pv.Icosphere(radius=r_sphere, center=(0, 0, 0))
box = pv.Box(
    bounds=(-l_box / 2, l_box / 2, -l_box / 2, l_box / 2, r_sphere, r_sphere + l_box)
)

cg_sphere = np.array(sphere.center)
cg_box = np.array(box.center)


def a(pos: np.ndarray) -> np.ndarray:
    pos = np.array(pos, dtype=float)
    r_box = pos - cg_box
    r_sphere = pos - cg_sphere
    r_box_norm = np.linalg.norm(r_box)
    r_sphere_norm = np.linalg.norm(r_sphere)
    a_box = -G * m_box * r_box / r_box_norm**3
    a_sphere = -G * m_sphere * r_sphere / r_sphere_norm**3
    return a_box + a_sphere


sampler_r = 2
sample_N = 100
gravity_points = []
gravity_vectors = []

for i in range(sample_N):
    frac = i / sample_N
    theta = 2 * math.pi * frac
    pos = np.array((0, math.cos(theta) * sampler_r, math.sin(theta) * sampler_r))
    gravity_points.append(pos)
    gravity_vectors.append(a(pos))

gravity_points = np.array(gravity_points)
gravity_vectors = np.array(gravity_vectors)


v = np.array((54, 54, 0))
p = np.array((0, 0, 3))
dt = 0.01
orbiter_points = [p]

for i in range(2000):
    accel = a(p)
    v = v + accel * dt
    p = p + v * dt
    orbiter_points.append(p)

orbiter_points = np.array(orbiter_points)

gravity_cloud = pv.PolyData(gravity_points)
gravity_cloud["vectors"] = gravity_vectors
orbiter_cloud = pv.PolyData(orbiter_points)

arrows = gravity_cloud.glyph(orient="vectors", scale=False, factor=0.25)
points = orbiter_cloud.glyph(orient=False, scale=False, factor=0.25)

plotter = pv.Plotter()
plotter.add_mesh(sphere, color="blue", opacity=0.4)
plotter.add_mesh(box, color="red", opacity=0.6)
plotter.add_mesh(arrows, color="green")
spline = pv.Spline(orbiter_points)
spline["time"] = np.linspace(0, 1, spline.n_points)
plotter.add_mesh(spline, scalars="time", cmap="RdYlGn", line_width=3)
plotter.show()
