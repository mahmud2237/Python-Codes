"""
counter = 0
while counter < 10:
    print (counter)
    counter += 1


-------
exit = " "
while exit != "yes":
    print("🥳")
    exit= input("Exit?: ")

"""
exit = "no"

while exit == "no":
  animal_sound = input("What animal sound do you want to hear?: ")
  if animal_sound == "Cow" or "cow":
    print("🐮 Moo")
  elif animal_sound == "Pig" or "pig":
    print("🐷 Oink")
  elif animal_sound == "Sheep" or "sheep":
    print("🐑 Baaa")
  elif animal_sound == "Duck" or "duck":
    print("🦆 Quack")
  elif animal_sound == "Dog" or "dog":
    print("🐶 Woof")
  elif animal_sound == "Cat" or "cat":
    print("🐱 Meow")
  else:
    print("I don't know that animal sound. Try again.")
  exit = input("Do you want to exit?: ")
