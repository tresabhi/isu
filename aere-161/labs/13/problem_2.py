import numpy as np

# create a 3x4 array of random integers from 1 to 50
A = np.random.randint(1, 50, (3, 4))
print("Original", A)

# replace the last row (index -1)
A[-1, :] = [1, 2, 3, 4]
print("Row replaced", A)

# sum it all up
sum_A = A.sum()
print("Sum", sum_A)

# find min and max using internally defined functions
min_A, max_A = A.min(), A.max()
print("Min", min_A, "Max", max_A)

# delete some rows and columns
A = np.delete(A, 1, 0)
A = np.delete(A, 2, 1)
print("Row deleted", A)

# replace the 1st element with 0
A[0, 0] = 0
print("1st element replaced", A)
