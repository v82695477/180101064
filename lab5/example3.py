n1 = input("Enter number 1: ")
n2 = input("Enter number 2: ")


if len(n1) <= len(n2):
  nmin = len(n1)
else:
  nmin = len(n2)

n1 = n1[::-1]
n2 = n2[::-1]

n = 0
for i in range(nmin):
  if n1[i] == n2[i]:
    n += 1

print(n)

