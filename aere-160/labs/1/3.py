value = int(input("Find the factorial of: "))
factorial = 1

for i in range(1, value + 1):
  factorial *= i
  print(factorial)

print(f"The factorial of {value} is {factorial}")