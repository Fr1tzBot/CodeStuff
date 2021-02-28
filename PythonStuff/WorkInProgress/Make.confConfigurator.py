import requests
import json
import urllib
import os
from time import sleep

stockMakeConf = ("# These settings were set by the catalyst build script that automatically\n" +
    "# built this stage.\n" +
    "# Please consult /usr/share/portage/config/make.conf.example for a more\n" +
    "# detailed example.\n" +
    'COMMON_FLAGS="-O2 -pipe"\n' + 
    'CFLAGS="${COMMON_FLAGS}"\n' +
    'CXXFLAGS="${COMMON_FLAGS}"\n' +
    'FCFLAGS="${COMMON_FLAGS}"\n' +
    'FFLAGS="${COMMON_FLAGS}"\n\n' + 
    'MAKEOPTS="-J2"\n\n' +
    'USE=""\n\n' +
    '# NOTE: This stage was built with the bindist Use flag enabled\n' +
    'PORTDIR="/var/db/repos/gentoo"\n' + 
    'DISTDIR="/var/cache/distfiles"\n' + 
    'PKGDIR="/var/cache/binpkgs"\n\n' +
    '# This sets the language of build output to English.\n' +
    '# Please keep this setting intact when reporting bugs.\n' +
    'LC_MESSAGES=C\n'
).split("\n")
useIndex = stockMakeConf.index('USE=""')
makeFlagIndexUrl = "https://www.gentoo.org/support/use-flags/index.html"
blankList = ["", None, " ", "  ", "    "]
yesList = ["yes", "y", "ye", "yea", "yee"]
maybeList = ["maybe", "m", "?", ""]
noList = ["no", "n"]
includedFlags = []
excludedFlags = []
ignoredFlags = []

def grabIndex(url):
    with urllib.request.urlopen(makeFlagIndexUrl) as f:
        return f.read().decode('utf-8')  
def formatIndex(index):
    cleanedIndex = []
    index = index.split("\n")
    for i in range(len(index)):
        if "<table" in index[i]:
            index = index[i:]
            break

    for i in range(len(index)):
        if "</table" in index[i]:
            index = index[:i+1]
            break
    
    for i in index:
        if "<th>" in i or "<td>" in i:
            cleanedIndex.append(i)
    return cleanedIndex
def indexToDict(index):
    indexDict = {}
    for i in range(len(index)):
        if (i % 2) != 0:
            indexDict[int((i+1)/2)] = {}
            indexDict[int((i+1)/2)][index[i-1]] = index[i]
    return indexDict
def stripIndex(index):
    toRemove = ["<th>", "<td>", "<code>", "</code>", "</th>", "</td>"]
    x = index[-2]
    for i in range(len(index)):
        index[i] = index[i].strip()
        for e in toRemove:
            index[i] = index[i].replace(e, "")
    print(x)
    return index
    


index = grabIndex(makeFlagIndexUrl)
index = formatIndex(index)
index = stripIndex(index)
index = indexToDict(index)
print(len(index))

open((str(os.getcwd()) + "/index.json"), "w").write(json.dumps(index, indent=4))

for i in index:
    print("\n" + str(index[i]))
    answer = input("Do you need support for this? [y/m/n] ")
    if answer in yesList:
        includedFlags.append(str(index[i]).split(":")[0].strip("{'").strip("'"))
    elif answer in noList:
        excludedFlags.append(str(index[i]).split(":")[0].strip("{'").strip("'"))
    else:
        ignoredFlags.append(str(index[i]).split(":")[0].strip("{'").strip("'"))
print(includedFlags)
print(excludedFlags)

