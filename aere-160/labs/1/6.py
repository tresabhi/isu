SAFE_DRINK_THRESHOLD = 60 # degrees celsius

temperature = int(input("What is the temperature? "))

if temperature < SAFE_DRINK_THRESHOLD:
  print("The drink is cool enough to drink")
else:
  while temperature > SAFE_DRINK_THRESHOLD:
    temperature -= 1
    print(f"Drink has cooled down to {temperature} degrees celsius")

  print(f"Drink has reached the safe temperature of {temperature} degrees celsius")
