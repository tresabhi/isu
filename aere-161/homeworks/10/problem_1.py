"""
Abhigyaan Deep
AER E 161

Purpose:
Write a script to print a temperature conversion chart to a screen. Your script
prompts the user for the minimum and maximum temperatures in degrees
Fahrenheit and prints both values. The script checks to make sure that the minimum
is less than the maximum and swap the values if not. Scripts prints to the screen the
temperature in degrees F from the minimum to the maximum (with step 1 degree F)
in one column and the corresponding temperature in degrees Celsius in another
column.
"""

minimum = int(input("Enter the minimum temperature in degrees Fahrenheit: "))
maximum = int(input("Enter the maximum temperature in degrees Fahrenheit: "))

# check if minimum is less than maximum
if minimum > maximum:
    minimum, maximum = maximum, minimum

# print the chart
for f in range(minimum, maximum + 1):
    # use the formula C = (F - 32) * 5/9
    c = (f - 32) * 5 / 9
    # print the temperature in degrees F and C
    print(f"F: {f:3.0f} C: {c:3.0f}")
