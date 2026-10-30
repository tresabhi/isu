N = 15  # horizontal node count [1]
M = 10  # vertical node count [1]

w = 3  # width [m]
Delta = w / N  # node spacing [m]
h = Delta * M  # height [m]

n_quads = N * M  # quad count
n_triangles = 2 * n_quads  # triangle count
n_vertices = (N + 1) * (M + 1)  # vertex count

rho = 7850  # metal density [kg/m^3]

t_wall = 10 / 1000  # side wall thickness [m]
t_effective = 120 / 1000  # frontal effective thickness
