N = 3  # horizontal node count [1]
M = 2  # vertical node count [1]

w = 3  # width [m]
Delta = w / N  # node spacing [m]
h = Delta * M  # height [m]

n_q = N * M  # quad count
n_t = 2 * n_q  # triangle count
n_v = (N + 1) * (M + 1)  # vertex count

rho = 7850  # metal density [kg/m^3]

t_w = 80 / 1000  # side wall thickness [m]
