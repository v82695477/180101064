gpa = float(input("gpa : "))
num_lec = int(input("number of lecture : "))

if (gpa < 2.0):
  if num_lec < 47:
    print("Not enough number of lectures and GPA!")
  else:
    print("Not enough GPA!")
else:
  if num_lec < 47:
    print("Not enough number of lectures!")
  else:
    print("GRADUATED!!!")

