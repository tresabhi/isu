BONUSES = {
  1: 1,
  4: 3,
  9: 5,
  14: 7,
  24: 9
}

salary = int(input("What is your salary? "))
years = int(input("How many years have you worked? "))
bonus = 0

if years >= 24:
  bonus = BONUSES[24]
elif years >= 14:
  bonus = BONUSES[14]
elif years >= 9:
  bonus = BONUSES[9]
elif years >= 4:
  bonus = BONUSES[4]
elif years >= 1:
  bonus = BONUSES[1]

salary *= bonus / 100

print(f"Your bonus: ${salary}")