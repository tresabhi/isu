import math

point_a = [1, 3, 5]
point_b = [-1, 4, 8]

if (len(point_a) != len(point_b)):
  raise ValueError("Points are not the same dimension")

# vector between points
vector_between = [None, None, None]
for index in range(0, len(point_a)):
  vector_between[index] = point_b[index] - point_a[index]

print(f"Vector between points: {vector_between}")

# magnitude of the vector
accumulator = 0
for index in range(0, len(vector_between)):
  accumulator += vector_between[index] ** 2

magnitude = math.sqrt(accumulator)
print(f"Magnitude of the vector: {magnitude}")

# unit vector
unit_vector = [None, None, None]
for index in range(0, len(vector_between)):
  unit_vector[index] = vector_between[index] / magnitude

print(f"Unit vector: {unit_vector}")
