#this is just the bare bones of the program without any installation
a = []
b = []
c = []
d = []
e = []
f = []
gradelist = [a,b,c,d,e,f]
print("welcome to Grade manager 1.0")
print("Type Help for a List of Commands")
while True:
  run = input(">>")
  if run == "help":
    print(" help \n exit \n add \n view \n percentcalc \n viewc \n")
  if run == "exit":
    break
  if run == "add":
    if len(a) > 0:
      run = input("Would You Like to Add (g)rades or (c)lasses? ")
      if run == "c":
        #add classes
        pass
      elif run == "g":
        #add grades
        pass
    else:
      #add classes
      run = input("how mant classes would you like to add? ")
      try:
        run = int(run)
      except:
        pass
      if not type(run) == int:
        print("please enter an integer between 1 and 6")
        continue
      elif run > 6:
        print("your number must be between 1 and 6.")
        continue
      else:
        for i in range(run):
          run = input("what is your " + str(i + 1) + "st class? ")
          gradelist[i].append(run)
        print("classes added successfully")
      
  if run == "view":
    #view grades
    if len(a) > 0:
      for i in range(len(a)):
        print(a[i])
    else:
      continue
    if len(b) > 0:
      for i in range(len(b)):
        print(b[i])
    if len(b) > 0:
      for i in range(len(b)):
        print(b[i])
    if len(c) > 0:
      for i in range(len(c)):
        print(c[i])
    if len(d) > 0:
      for i in range(len(d)):
        print(d[i])
    if len(e) > 0:
      for i in range(len(e)):
        print(e[i])
    if len(f) > 0:
      for i in range(len(f)):
        print(f[i])
    pass
  if run == "percentcalc":
    percent1 = input("what did you score? ")
    try:
      percent1 = float(percent1)
    except:
      print("you must enter a number")
      continue
    percent2 = input("how many points was it worth? ")
    try:
      percent2 = float(percent2)
    except:
      print("you must enter a number.")
      continue
    print(percent1/percent2)
  if run == "viewc":
    if len(a) > 0:
      print(a[0])
    else:
      continue
    if len(b) > 0:
      print(b[0])
    if len(c) > 0:
      print(c[0])
    if len(d) > 0:
      print(d[0])
    if len(e) > 0:
      print(e[0])
    if len(f) > 0:
      print(f[0])
