import numpy as np

x = np.array([[1], [2], [3]])  # 3x1 matrix
y = np.array([10, 20, 30, 40])  # 1x4 matrix

# broadcasting is known to happen here
print(x + y, end="\n\n")

# this is just negative addition, I expect this to work
print(x - y, end="\n\n")

# this works, interestingly. we're breaking so many matrix rules here
print(x * y, end="\n\n")

# division doesn't make sense in matrix mindset but element-wise it works
print(x / y, end="\n\n")

# I am surprised the devs even know this operator existed, ha!
print(x // y, end="\n\n")

# modulus against individual numbers is useful (or one against a matrix), I don't see much use for this but ok
print(x % y, end="\n\n")

# no surprise here, element-wise exponentiation
print(x**y, end="\n\n")

# I am surprised they implemented bit-wise AND but I suppose it isn't that hard
print(x & y, end="\n\n")

# XOR! the coolest of bit operators
print(x ^ y, end="\n\n")

# this one blew my mind even more than the AND operation, but since it's element-wise, it ain't too hard
print(x << y, end="\n\n")

# uh it's all 0s? I thought Python used floats by default? hmmm.
print(x >> y, end="\n\n")

# woah! I expected these to be just False but it does this element-wise too!
print(x == y, end="\n\n")
print(x > y, end="\n\n")
print(x >= y, end="\n\n")
print(x < y, end="\n\n")
print(x <= y, end="\n\n")

# I give up testing operators, let's try mismatching shapes
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[10, 20], [30, 40]])

# voila! numpy sees the 3 of x's 2x3 and 2 of y's 2x2 and throws an error
print(x + y)
