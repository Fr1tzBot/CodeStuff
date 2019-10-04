#import neccesary modules
from time import sleep
#define afternumber function
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
#define mode function
def mode(arr) :
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
#define total of tuple function
def total(i):
  count = int(len(i))
  t = int()
  while count != 0:
    t = float(t) + float(i[count - 1])
    count = count - 1
  if type(t) == "integer":
    t = int(t)
  return(t)
#define tople function
def tople(t):
  counter = int(0)
  length = len(t)
  out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  toremove = len(out) - length
  counter = toremove
  while len(out) != length:
    out.remove(0)
    counter -= 1
  counter = 0
  while counter != length:
      out[counter] = (int(t[counter]))
      counter += 1
  return out
#define median function
def median(l):
    l = tuple(l)
    half = len(l) // 2
    if not len(l) % 2:
        return (l[half - 1] + l[half]) / 2.0
    return l[half]
#ask for the amount of digits
try:
  number = int(input("how many numbers do you have? "))
#return error if user doesn't enter a number
except ValueError:
  print("you must enter a number")
  sleep(1)
  exit()
#format all variables
counter = int()
data = list()
#find number of numbers
while counter != number:
  after = afternumber(counter + 1)
  data = (data + list(input("what is your " + (str(counter + 1)) + str(after) + " number? ")))
  counter = counter + 1
#prevent strange errors #i don't know why this works but it does
if len(data) != number:
    print("fatal error:ok")
    sleep(1)
    print("two or more digits will be imported in future versions")
    sleep(2)
    exit()
#format data as tuple using tople function  #sort the data
data = sorted(tople(data))
#show the data
print(data)
sleep(1)
#calculate the total
print("calculating total...")
#format total variable
sleep(.5)
print("total is " + str(total(data)))
#calculate the mean
sleep(.5)
print("calculating average...")
sleep(.5)
print ("average is " + str((total(data)) / number))
sleep(.5)
#calculate the median
print("calculating median...")
sleep(.5)
print("median is " + str(median(data)))
sleep(.5)
#calculate the MAD
print("calculating MAD...")
sleep(.5)
print("MAD is " + str(mad(data, (total(data)))))
sleep(.5)
print("calculating mode...")
sleep(.5)
print("mode is " + str(mode(data)))
sleep(.5)
print("calculating Maximum...")
sleep(.5)
print("MAximum is " + str(max(data)))
sleep(.5)
print("Calculating Minimum...")
sleep(.5)
print("minimum is " + str(min(data)))
