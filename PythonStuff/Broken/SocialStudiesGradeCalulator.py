#social studies grade calculator
def frange(start, stop=None, step=None):
    #Use float number in range() function
    # if stop and step argument is null set start=0.0 and step = 1.0
    if stop == None:
        stop = start + 0.0
        start = 0.0
    if step == None:
        step = 1.0
    while True:
        if step > 0 and start >= stop:
            break
        elif step < 0 and start <= stop:
            break
        yield ("%g" % start) # return float number
        start = start + step
print("Welcome to social studies grade calculator 1.0")
print("This calculator will help you determine how you need to do on your next assignment to pass, ")
print("how much a score will affect your grade, and simple conversions to help tell what grade a percent is.")
print("to see what grade a percent is, type gradelist -c")
print("to see how an assignment will effect your grade, type effect -p")
print("to determine what you need tto get on your next assignment to pass, type passing -s")
print("also, type help for even more commands")
Aplus = (98, 99, 100)
A = (90, 90.1, 90.2, 90.2, 90.4, 90.5, 90.6, 90.7, 90.8, 90.9, 91, 91.1, 92.1, 92.2, 92.3, 92.4, 92.5, 92.6, 92.7, 92.8, 92.9, 93, 93.1, 93.2, 93.3, 93.4, 93.5, 93.6, 93.7, 93.8, 93.9, 94, 94.1, 94.2,   97.9,)
Aminus = frange(90, 92.9, 0.1)
Bplus = frange(87, 89.9, 0.1)
B = frange(83, 86.9, 0.1)
Bminus = frange(80, 82.9, 0.1)
Cplus = frange(77,  79.9, 0.1)
C = frange(73, 76.9, 0.1)
Cminus = frange(70, 72.9, 0.1)
Dplus = frange(67, 69.9, 0.1)
D = frange(63, 66.9, 0.1)
Dminus = frange(60, 62.9, 0.1)
E = frange(0, 59.9, 0.1)
while True:
  command = input(">>")
  if command == "gradelist -g":
    varA = float(input("how many points was the assignment worth?"))
    varB = float(input("what did you score?"))
    percent = (varB/varA)*100
    print("you socred " + str((varB/varA)*100) + "%")
    
    print("that is a(n)")
  if command == "gradelist -c":
    varA = float(input("how many points was the assignment worth?"))
    varB = float(input("what did you score?"))
    print("you scored " + str((varB/varA)*100) + "%")
  if command == "gradelist -l":
    print("98% and above is an A+")
    print("93% - 97.9% is an A")
    print("90% - 92.9% is an A-")
    print("87% - 89.9% is a B+")
    print("83% - 86.9% is a B")
    print("80% - 82.9% is a B-")
    print("77% - 79.9% is a C+")
    print("73% - 76.9% is a C")
    print("70 - 72.9 is a C-")
    print("67% - 69.9% is a D+")
    print("63% - 66.9% is a D")
    print("60% - 62.9% is a D-")
    print("59.9% and lower is an E")
  if command == "exit":
    break