import random
digits = ("x", "o", "na")
y1 = ("na", "na", "na")
y2 = ("na", "na", "na")
y3 = ("na", "na", "na")
board = (y1, y2, y3)
def placepiece(x, y, digit = None):
  if not x in range(1, 3) or y in range(1, 3):
    return
  y = y-1
  x = x-1
  board[y][x] = digit
  return
placepiece(1, 1, "x")
print(y1)