pwd = "abc123"

while(True):
  p = input("Enter password: ")
  if(p == pwd):
    print("Welcome")
    break
  elif(p == "help"):
    print(pwd[0])
  else:
    print("Wrong")
