#choose your own adventure game
#line 24 left off
print("you are sailing with your dad when suddenly you see a large ship on the horizon, as the ship gets closer, you see that the ship is flying the pirate flag! Do you fight or run?")
import time
time.sleep(8)
choice = input("fight or run?")
if choice == "fight":
  time.sleep(1)
  print("the pirates easily outgun you and you are forced to let them board your boat, where they raid it and kill you and your dad.")
if choice == "run":
  print("you and your dad got away from the pirates but in your distraction, went straight into a massive storm!")
  time.sleep(8)
  choice = input("do you try to hold out or run away?")
  time.sleep(1)
  if choice == "hold out":
    print("your ship is damaged but your sails still work. you and your dad packed lunches but want to head home because the pirates are still looking for you")
    time.sleep(8)
    choice = input("do you go home or stay?")
    time.sleep(1)
    if choice == "go home":
      print("when you try to go home, the pirates head you off and destroy your ship")
    if choice == "stay":
      print("you and your dad decide to stay and eat your lunches.")
      time.sleep(8)
      choice
  if choice == "run away":
    print("when you try to run away, a gigantic wave tips the ship over. Game Over")