import os
import subprocess
import shlex
import json
import pyclip
import markdown

def formatjson(jsonName):
    jsonFile = os.path.expanduser(jsonName)
    with open(jsonFile, "r") as f:
        j = json.load(f)
    with open(jsonFile, "w") as f:
        f.write(json.dumps(j, indent=4))

def scanUrl(url):
    odd = pathFormat("~/Downloads/OpenDirectoryDownloader-osx-x64-self-contained/OpenDirectoryDownloader")
    subprocess.call(shlex.split(f"{odd} -u {url} -q -f -c -o 10"))

def readClipboard():
    return pyclip.paste(text=True)

def pathFormat(path):
    return os.path.expandvars(os.path.expanduser(path))

with open(pathFormat("~/Downloads/chrome_bookmarks.json"), "r") as f:
    bookmarks = json.load(f)

def writeMD(name, contents):
    with open(name + ".md", "w+") as f:
        f.write(contents)

formattedBookmarks = []
inFolder = False
for i in range(len(bookmarks)):
    if bookmarks[i]["parentId"] != "1":
        inFolder = True
    elif i != 0:
        break
    if inFolder:
        formattedBookmarks.append(bookmarks[i])

clipboards = []

for i in formattedBookmarks[0:1]:
    scanUrl(i["url"])
    clipboards.append(readClipboard())


for i in range(10):
    print("\n")
if len(clipboards) == len(formattedBookmarks[0:1]):
    for i in range(len(clipboards)):
        writeMD(formattedBookmarks[i]["title"], clipboards[i])

