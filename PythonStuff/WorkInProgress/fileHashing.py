from os import error
from urllib.request import HTTPDefaultErrorHandler


try:
    import hashlib
    import requests
    import re
    import os
    import pathlib
    import json
except:
    print("Please run 'pip install wget' to get the needed dependencies to run this program")
    raise

def md5(filename):
    return hashlib.md5(open(str(filename), "rb").read()).hexdigest()

def verifyHash(filename, hash):
    return md5(filename) == hash

def downloadURL(url):
    def getFileName(cd, url):
        if cd:
            return (re.findall("filename=(.+)", cd))[0]
        else:
            return url.split("/")[-1]
    r = requests.get(url)
    fileName = str(getFileName(r.headers.get('content-disposition'), url))
    if os.name == "nt": 
        open(str(os.getcwd() + "\\" + fileName), 'wb').write(r.content)
        return str(os.getcwd() + "\\" + fileName)
    else:
        open(str(os.getcwd() + "\\" + fileName), 'wb').write(r.content)
        return str(os.getcwd() + "\\" + fileName)

def getDataFile():
    if os.name == "nt":
        if os.path.isfile(str(pathlib.Path(__file__).parent.absolute()) + "\data.json"):
            return str(pathlib.Path(__file__).parent.absolute()) + "\data.json"
        else:
            f = open(str(pathlib.Path(__file__).parent.absolute()) + "\data.json", "w+")
            f.write('{\n "links": {}\n}')
            f.close()
            return str(pathlib.Path(__file__).parent.absolute()) + "\data.json"
    else:
        if os.path.isfile(str(os.getcwd()) + "/data.json"):
            return str(pathlib.Path(__file__).parent.absolute()) + "/data.json"
        else:
            f = open(str(pathlib.Path(__file__).parent.absolute()) + "/data.json", "w+")
            f.write("{}")
            f.close()
            return str(pathlib.Path(__file__).parent.absolute()) + "/data.json"

def writeData():
    global data
    f = open(getDataFile(), "w")
    f.write(json.dumps(data, indent=4, ))#sort_keys=True))
    f.close

def clearJSON():
    f = open(getDataFile(), "w+")
    f.write("{}")
    f.close()
    
def addData(url, hash, filename):
    global data
    data["links"][url] = hash
    data[hash] = {"Filename": filename}
    
    
    
    

url = str()
dataPath = getDataFile()
data = json.load(open(dataPath))
currentHash = str()

print("Version 1.0")
url = input("Please Input URL: ")
if url in data["links"]:
    currentHash = data["links"][url]
    print(currentHash)
else:
    print("This link is not in the database.")
    if input("Would you like to add it? ").strip().lower() in ["y", "yes"]:
        fileName = downloadURL(url)
        addData(url, md5(fileName), fileName.split("\\")[-1])
        writeData()
        exit()
    else:
        if input("Ok, would you like to download the file anyway?").strip().lower() in ["y", "yes"]:
            downloadURL(url)
            exit()
        else:
            print("Goodbye.")
            exit()
if len(data[currentHash]) > 1:
    print("The following links are available for that file:")
    for i in data[currentHash]:
        print(i)
else:
    print("that is the only link available for that file.")
if input("continue download? ").strip().lower() in ["y", "yes"]:
    downloadURL(url)
else:
    print("Goodbye.")
    exit()
