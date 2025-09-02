"""
Abhigyaan Deep
AER E 161

Purpose: Do some stuff with a point. Quite implicit if you look at the code 😄
"""

# declare as a tuple
point = (3.0, 1.5, 2.0)

# print with 1 decimal place
print(f"X-coordinate: {point[0]:.1f}")
print(f"Y-coordinate: {point[1]:.1f}")
print(f"Z-coordinate: {point[2]:.1f}")

# calculate the distance using the Pythagorean theorem
distance = (point[0] ** 2 + point[1] ** 2 + point[2] ** 2) ** 0.5
# use 1 decimal place again I suppose
print(f"Distance: {distance:.1f}")
