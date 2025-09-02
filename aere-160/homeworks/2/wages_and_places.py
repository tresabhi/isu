pay = 50000
location = 'Texas'

if location == 'space':
  print("I'll take it!")
elif location == 'Iowa':
  if pay <= 100000:
    print("Not interested")
  else:
    print("I'll take it!")
elif location == 'Texas':
  if pay >= 60000:
    print("I'll take it!")
  else:
    print("I would've loved to work here if the pay was at least $60K")
elif pay >= 70000:
  print("I'll take it!")
else:
  print("No thanks!")
