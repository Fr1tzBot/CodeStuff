#nothine heer yet...
#from RPC import Run
digits = ("x", "o", "na")
y1 = ("", "", "")
y1 = list(y1)
y2 = ("", "", "")
y2 = list(y2)
y3 = ("", "", "")
y3 = list(y3)
def placepiece(x, y):
  if not x in range(1, 3) or y in range(1, 3):
    #nothing
    fillblank = True
  else:
    Y = y
    X = x
    global y1
    global y2
    global y3
    if Y == 1:
      if X == 1:
        y1[0] = "x"
      if X == 2:
        y1[1] = "x"
      if X == 3:
        y1[2] = "x"
    if Y == 2:
      if X == 1:
        y2[0] = "x"
      if X == 2:
        y2[1] = "x"
      if X == 3:
        y2[2] = "x"
    if Y == 3:
      if X == 1:
        y3[0] = "x"
      if X == 2:
        y3[1] = "x"
      if X == 3:
        y3[2] = "x"
  return y1
print(y1)
print(y2)
print(y3)
print(type(y1))
y1[0] = "x"
print(y1)
print(y2)
print(y3)