import numpy as np

point_a = np.array([5, 3, 5])
point_b = np.array([4, 2, 7])

# vector between points
vector_between = point_b - point_a
print(f"Vector between points: {vector_between}")

# magnitude of the vector
magnitude = np.linalg.norm(vector_between)
print(f"Magnitude of the vector: {magnitude}")

# unit vector
unit_vector = vector_between / magnitude
print(f"Unit vector: {unit_vector}")
