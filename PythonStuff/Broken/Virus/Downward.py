from os import walk
import os

f = []
while len(f) > 1:
  for (dirpath, dirnames, filenames) in walk("/"):
    f.extend(dirnames)
    break
  os.system("cd " + f[1])
os.system("pwd")

