def f(x: int) -> int:
  return x ** 2

def summate(n: int, iterations: int) -> int:
  sum = 0

  for i in range(n, iterations + 1):
    sum += f(i)

    print(sum)
  
  return sum

print(f"Sum: {summate(1, 20)}")