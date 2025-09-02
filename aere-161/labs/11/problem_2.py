# declare real number
real_number = 12345.6789

# prints as is, "12345.6789"
print(real_number)

# also prints as is, "12345.6789"
print("{:10.4f}".format(real_number))

# prints with only 2 decimal places with rounding (7 -> 8) "12345.68"
print("{:2.2f}".format(real_number))
