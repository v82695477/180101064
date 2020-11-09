a = int(input('Enter a integer'))

if a < 10:
  r = "0" + str(a)
else: 
  f = a % 10
  s = (a // 10) % 10
  r = str(s) + str(f)

print(r)


