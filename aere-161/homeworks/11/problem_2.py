import math

"""
Abhigyaan Deep AER E 161

Purpose: rotate point by theta
"""

# request x0, y0, and theta
x0 = float(input("Enter x0: "))
y0 = float(input("Enter y0: "))
theta = float(input("Enter theta: "))


# define the function
def rotate(x0, y0, theta):
    # use the formula
    x = x0 * math.cos(theta) - y0 * math.sin(theta)
    y = x0 * math.sin(theta) + y0 * math.cos(theta)

    # return the result
    return x, y


# call the function
x, y = rotate(x0, y0, theta)

# print the result
print(f"x = {x}")
print(f"y = {y}")
