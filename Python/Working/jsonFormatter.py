import json
import os
import sys

jsonFile = os.path.expanduser(sys.argv[1])

with open(jsonFile, "r") as f:
    j = json.load(f)
with open(jsonFile, "w") as f:
    f.write(json.dumps(j, indent=4))