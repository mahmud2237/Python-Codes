"""
myScore = input("Your score: ")
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")

----------------------------
myPi = float(input("What is Pi to 3dp? :"))
if myPi == 3.1416:
  print("Exactly!")
else:
  print("Try again 😭")

---------------------------
score = int(input("What was your score on the test?"))
if score >= 80:
  print("Not too shabby")
elif score > 70:
  print("Acceptable.")
else:
  print("Dude, you need to study more!")

"""
genBirth_Year = int(input("What generation are you from?"))

if genBirth_Year <= 1924:
    print("You are from the past")
elif genBirth_Year >= 1925 and genBirth_Year <= 1946:
    print("You are from the Traditionalists")
elif genBirth_Year >= 1947 and genBirth_Year <= 1964:
    print("You are from the Baby Boomers")
elif genBirth_Year >= 1965 and genBirth_Year <= 1981:
    print("You are from Generation X")
elif genBirth_Year >= 1982 and genBirth_Year <= 1995:
    print("You are from the Millennials")
elif genBirth_Year >= 1996 and genBirth_Year <= 2015:
    print("You are from Generation Z")
else:
    print("You are from the future")

