n = int(input("How many numbers? "))

even = 0
for i in range(n):
  x = int(input("Enter an integer: "))
  if x % 2 == 0:
    even += 1

percent = (even/n)*100
print(percent,"%")