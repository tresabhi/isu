"""
Abhigyaan Deep AER E 161

Purpose: Solve a system of equations using numpy linalg
"""

import numpy as np

# create a 4x4 matrix of the coefficients
A = np.array(
    [
        [1, 1, 6, -2],
        [-1, 2, 9, -1],
        [1, -2, 3, 3],
        [
            0,
            -1,
            9,
            -4,
        ],
    ]
)
# create a column vector of the constants
b = np.array([10, 8, 8, -2])


# implement the tiny function
def solve(A, b):
    # solve the linear system
    x = np.linalg.solve(A, b)
    # return the Xs
    return x


# call and unpack the results
x1, x2, x3, x4 = solve(A, b)

# print the results
print(f"x1 = {x1} x2 = {x2} x3 = {x3} x4 = {x4}")
