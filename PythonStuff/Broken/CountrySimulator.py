from time import sleep
from random import randint
from math import ceil
def afternumber(i):
  st = (1,21,31,41,51,61,71,81,91,101,121)
  rd = (3,23,33,43,53,63,73,83,93,103,123)
  nd = (2,22,32,42,52,62,72,82,92,102,122)
  if i in st:
    return "st"
  elif i in rd:
    return "rd"
  elif i in nd:
    return "nd"
  else:
    return "th"
pop = 5000
mil = 1000
eco = 80
year = 0
lost= 0
millist = []
ownedcountries = []
events = ["plague", "war", "poverty", "revolt"]
resources = ["wood", "iron", "gold", "coal"]
yourresource = resources[randint(0, 3)]
print("welcome to Country Simulator!")
name = input("please choose a name for your country: ")
ownedcountries.append(name)
count = int(input("how many other countries would you like to have? "))
if count > 50:
  print("you country count must be 50 or lower to keep you from going insane.")
  exit()
namelist = list()
for i in range(count):
  namelist.append(input("what would you like to name the " + str(i+1) + afternumber(i+1) + " country? "))
for i in range(len(namelist)):
  millist.append((1000 + (randint(-5, 5)*100)))
print("you countries are: ")
print(namelist)
startyear = int(input("what year would you like to start in? "))
if startyear < 0:
  print("your number must be positive.")
  exit()
print("preparing simulation...")
sleep(0.5)
print("the rules are simple:")
print("to win, control the continent for 10 years.")
print("You lose if you lose control of your country or if all your people die")
print("you are beginning in the year " + str(startyear))
print("there are " + str(count) + " other countries")
print("Which are:")
print(namelist)
print("your country is called " + name)
print("at the beginnning of each year you will see your \nmilitary might, population, and economy. Keep these things \nbalanced to become a powerful country.")
print("your economy is shown as a percent out of 100")
print("_______________________________________________________________")
while pop > 0:
  print("year " + str(startyear + year) + ":")
  print("your population is: " + str(pop))
  print("your military is: " + str(mil))
  print("your economy is: " + str(eco))
  task = input("Would you like to Attack, Trade, Train, or Do Nothing?")
  if task == "Attack" or task == "attack" or task == "a":
    print(namelist)
    target = input("who would you like to attack?")
    if not target in namelist:
      pass
    elif target in ownedcountries:
      pass
    else:
      listnumber = 0
      for i in range(len(namelist)):
        if namelist[i] == target:
          listnumber = i
          break
      print(target + " has " + str(millist[listnumber]) + " military units")
      print("you have " + str(mil) + " units")
      attack = input("are you sure you would like to attack?")
      if attack == "y" or attack == "yes" or attack == "Y" or attack == "Yes":
        print("Beginning Battle...")
        sleep(0.5)
        if abs(millist[listnumber] - mil) <= 500:
          if mil > millist[listnumber]:
            win = randint(1, 10) in range(1, 7)
            lost = randint(1, 3) * 100
          elif mil < millist[listnumber]:
            win = randint(1, 10) in range(1, 5)
            lost = randint(1, 4) * 100
          elif mil == millist[listnumber]:
            win == randint(1, 10) in range(1, 6)
            lost = randint(1, 5) * 100
          if win:
            print("you have successfully conquered " + target)
            ownedcountries.append(target)
            print("you lost " + str(lost) + " troops")
            mil = mil - lost
            lost = 0
          else:
            print("you failed to conquer " + target)
            print("you lost " + str(lost) + " trooops")
            mil = mil - lost
            lost = 0
  if task == "train" or task == "Train":
    #train a specific number of troops
    totrain = int(input("how many troops would you like to train?"))
    if totrain > pop/2:
      print("you can only train as much as half of your population")
    else:
      print("preparing to train troops...")
      train = input("this will cost " + str(ceil(totrain/10)) + " are you sure you would like to continue?")
      if train == "yes" or train == 'Yes' or train == "Y" or train == "y":
        eco = eco - ceil(totrain/10)
        mil += totrain
  if task == "nothing" or task == "do nothing" or task == "Do nothing" or task == "do Nothing":
    eco += randint(0, 2)
    pop += randint(50, 100)
  if task == "trade" or task == "Trade":
    print("your material is: " + yourresource)
    tradecountry = input("Who would you like to trade with?")
    if tradecountry not in namelist:
      pass
    elif tradecountry in ownedcountries:
      pass
    else:
      countrymat = resources[randint(0, 3)]
      print(tradecountry + " currently has an access of "  + countrymat)
      trade = input("would you like to trade for that?")
      if trade == "y" or trade == "Y" or trade == "yes" or trade == "Yes":
        