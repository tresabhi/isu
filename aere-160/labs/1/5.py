def factorialize(x: int) -> int:
  index = 1
  factorial = 1

  while index <= x:
    factorial *= index
    index += 1

    print(factorial)
  
  return factorial

print(factorialize(10))