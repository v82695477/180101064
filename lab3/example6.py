a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))

delta = (b**2 - 4*a*c)

if delta > 0:
  x1 = (((-b) + delta**(1/2))/(2*a))
  x2 = (((-b) - delta**(1/2))/(2*a)) 
  print("there are two roots", x1, "and", x2)
elif delta ==0:
  x =-b / (2 * a)
  print("there are one root",x)
else:
  if delta < 0:
    delta = delta * (-1)
  sqrt_delta = delta**(1/2)
  x1 =- b / (2 * a)+ " + i"+ sqrt_delta  
  x1 =- b / (2 * a)+ " - i"+ sqrt_delta  
  print("there are two roots")
  print("x1 ",x1)
  print("x2 ",x2)
