age = int(input("How old are you ?"))

if (age < 6 or age > 60):
  price = 0
elif (age>= 6 or age <= 18):
  price = 1.5
else:
  price = 3

if price > 0:
  print("Your price is",price)
else:
  print("Your price is free")