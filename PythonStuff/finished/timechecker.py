from time import ctime
tr = range(8,20)
while True
  CT = ctime()
  CT = str(CT)
  CT = (CT[11])+(CT[12])+(CT[13])+(CT[14])+(CT[15])
  if len(CT) == 5:
    hour = (CT[0])+(CT[1])
  else:
    hour = (CT[1])
  minute = (CT[3])+(CT[4])
  if hour in tr:
    inv = True
    #invert colors here
    print("inverted")
  else:
    inv = False