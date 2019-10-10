from os import walk
import os

os.system("cd /")
f = []
c = 0
while len(f) > 1:
  for (dirpath, dirnames, filenames) in walk("~"):
    if c == 2:
      f.extend(dirnames)
      break
    else:
      c += 1
  os.system("cd " + f[1])
os.system("pwd")
print(f)
