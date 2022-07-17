import os
import json
import hashlib
import glob
from datetime import datetime
import sys

def md5(filename):
    return hashlib.md5(open(str(filename), "rb").read()).hexdigest()

fileDict = {}
if len(sys.argv) > 1:
    topDirs = sys.argv[1:]
else:
    topDirs = [os.getcwd()]
startTime = datetime.now()

for topDir in topDirs:
    print("Scanning " + str(topDir) + "...")
    items = glob.glob(topDir + "/**/*", recursive=True)
    files = []

    for i in items:
        if os.path.isfile(i):
            files.append(i)
    print("Found " + str(len(files)) + " Files")
    fileDict[topDir] = {}
    for i in files:
        print("adding: " + str(i))
        fileDict[topDir][i] = {"size": os.path.getsize(i), "hash": md5(i)}

open((str(os.getcwd()) + "/index.json"), "w").write(json.dumps(fileDict, indent=4))
print("Time: " + str(datetime.now() - startTime))