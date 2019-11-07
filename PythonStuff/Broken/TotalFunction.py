def total(i):
  count = int()
  count = len(i)
  t = int()
  while count != 0:
    t = float(t) + float(i[count - 1])
    count = count - 1
  if int(t) == t:
    t = int(t)
  return(t)
