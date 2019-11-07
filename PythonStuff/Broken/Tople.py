def tople(t):
  counter = 0
  while not counter >= len(t):
    tople = tuple()
    tople = tople + (int(t[counter]),)
    counter = counter + 1
  tople = tople + (int(t[len(t)-1]),)
  return tople