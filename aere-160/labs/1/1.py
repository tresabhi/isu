COST = 5
OFFER_THRESHOLD = 25
OFFER = 15 / 100

units = int(input("How many units do you want to buy? "))

offer = 0

if units >= OFFER_THRESHOLD:
  offer = 1 - OFFER
else:
  offer = 1

price = COST * units * offer

print(f"Price: ${price}")