#define afternumber function
def afternumber(number):
  if str(number)[-1] == "1":
    return "st"
  elif str(number)[-1] == "3":
    return "rd"
  elif str(number)[-1] == "2":
    return "nd"
  else:
    return "th"
#define mode function
def mode(arr):
  m = max([arr.count(a) for a in arr])
  return [x for x in arr if arr.count(x) == m][0] if m>1 else None
#define mad function
def mad(d, t):
  average = t / len(d)
  counter = 0
  tmad = 0
  while counter != len(d): 
    tmad = tmad + abs((d[counter]) - average)
    counter += 1
  mad = tmad / len(d)
  return mad
#define median function
def median(l):
  half = len(l) // 2
  if not len(l) % 2:
    return (l[half - 1] + l[half]) / 2.0
  return l[half]
#get data from user
data = input("input your data in [1,0,1] format (spaces will be removed) ")
toRemove = [" ", "[", "]", "(", ")"]
for i in toRemove:
  data = data.replace(i, "")
data = data.split(",")
for i in range(len(data)):
  try:
    data[i] = float(data[i])
  except ValueError:
    print("You Must Enter a Number.")
    exit()

#sort the data
data = sorted(data)

#show the data
print(data)

#print statistics info
print("Calculating total...")
print("Total is "   +  str(sum(data)))
print("Average is " +  str(sum(data)/len(data)))
print("Median is "  +  str(median(data)))
print("MAD is "     +  str(mad(data, sum(data))))
print("Mode is "    +  str(mode(data)))
print("Maximum is " +  str(max(data)))
print("Minimum is " +  str(min(data)))
