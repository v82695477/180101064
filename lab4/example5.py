n = int(input('Enter a number'))

f = 1
range_ = n+1
if(n == 0 ):
  f = 1
else:
  for i in range(1,range_):
    f *= (i)

print(f)
