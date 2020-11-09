mounth = int(input("Give a mounth : "))
day = int(input("Give a day : "))
year = '2020'


if mounth >= 3 and mounth <= 5:
  if month == 3 and day < 20:
    print(day,mounth,year, "is Winter")
  elif mounth == 3 and day >= 20:
    print(day,mounth,year, "is Spring")
  else:
    print(day,mounth,year, "is Spring")

elif month >=6 and month <= 8:
  if month == 6 and day < 21:
    print(day,mounth,year, "is Spring")
  elif month == 6 and day >= 21:


elif mounth >= 5 and mounth <= 8:
  if mounth == 5 and day >= 5:
    print(day,mounth,year, "is Summer")
  elif mounth==5 and day < 5:
    print(day,mounth,year, "is Spring")
  else:
    print(day,mounth,year, "is Summmer")
  




  
