N = 3  # horizontal node count [1]
M = 2  # vertical node count [1]

w = 3  # width [m]
Delta = w / N  # node spacing [m]
h = Delta * M  # height [m]

N_q = N * M  # quad count
N_t = 2 * N_q  # triangle count
N_v = (N + 1) * (M + 1)  # vertex count
