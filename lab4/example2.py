y = int(input('year'))

if (y % 400 == 0):
  print("leap")
elif y % 100 ==0:
  print("not leap")
elif y % 4 == 0:
  print("leap")
else: 
  print("not leap")