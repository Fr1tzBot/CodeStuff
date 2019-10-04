from time import ctime
CT = ctime()
CT = str(CT)
CT = (CT[11])+(CT[12])+(CT[13])+(CT[14])+(CT[15])
if len(CT) == 5:
  hour = (CT[0])+(CT[1])
else:
  hour = (CT[1])
minute = (CT[3])+(CT[4])
  
