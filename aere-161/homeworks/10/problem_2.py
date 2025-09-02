import math

"""
Abhigyaan Deep
AER E 161

Purpose: implement the given piece-wise function; there's no way I am
typing that function here haha.
"""

# declare each part of the piece-wise function separately
f1 = lambda a, x: (math.pow(a + 1, 2 / 3)) / (math.sqrt(abs(a)) + x)
f2 = lambda a, x: math.pow(math.tan(x + a / math.pi), 2)
f3 = lambda a, x: math.pow(math.log(a + math.pow(math.e, a * x), math.e), 2)

# ask for a, get x, and pre-compute ax for convenience
a = float(input("Enter a = "))
x = math.sin(0.5 * a)
ax = a * x

# apply the cases of the piece-wise function
y = f1(a, x) if ax <= 0 else f2(a, x) if 0 < ax < 1 else f3(a, x)

# print the result
print(f"y = {y}")
