try:
    import hashlib
    import requests
    import re
    import os
    import pathlib
    import json
    import urllib
except:
    print("Please run 'pip install regex requests' to get the needed dependencies to run this program")
    exit()

def md5(filename):
    return hashlib.md5(open(str(filename), "rb").read()).hexdigest()

def verifyHash(filename, hash):
    if md5(filename) == hash:
        print("File download successful")
    else:
        print("Warning: downloaded file hash does not match database hash")
        print("File may not have been downloaded successfully")
        
def getFileSize(filename):
    try:
        num = os.path.getsize(filename)
        for unit in ['','K','M','G','T','P','E','Z']:
            if abs(num) < 1000.0:
                return "%3.1f%s%s" % (num, unit, "B")
            num /= 1024.0
        return "%.1f%s%s" % (num, 'Y', "B")
    except:
        raise
        return None

def verifyUrl(url):
    request = requests.get(str(url))
    return request.status_code == 200

def downloadURL(url):
    url = urllib.parse.unquote(url)
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
        open(str(os.getcwd() + "/" + fileName), 'wb').write(r.content)
        return str(os.getcwd() + "/" + fileName)

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
            f.write('{\n "links": {}\n}')
            f.close()
            return str(pathlib.Path(__file__).parent.absolute()) + "/data.json"

def writeData():
    global data
    f = open(getDataFile(), "w")
    f.write(json.dumps(data, indent=4))
    f.close

def clearJSON():
    os.remove(getDataFile)
    getDataFile()
    
def addData(url, hash, filename, size):
    global data
    data["links"][url] = hash
    data[hash] = {"Filename": filename, "Size": size}
    

url = str()
dataPath = getDataFile()
data = json.load(open(dataPath))
currentHash = str()
counter = int()

url = input("Please Input URL: ")
if not verifyUrl(url):
    print("Warning: Requests could not verify that this URL is working")
    if not input("Would you like to continue the download anyway?") in ["y", "yes"]:
        exit()
if url in data["links"]:
    #If it is, set currentHash to the link's hash and provide that hash to the user
    currentHash = data["links"][url]
    print("The hash of that URL is: " + str(currentHash))

    #Then check for other links that provide the same file
    if len(data[currentHash]) > 1:
        print("The following links are available for that file:")
        for i in data[currentHash]:
            print(i)
    else:
        print("That is the only link available for that file.")
        
    if input("Continue download? ").strip().lower() in ["y", "yes"]:
        fileName = downloadURL(url)
        verifyHash(fileName, data["links"][url])
else:
    #If it isn't, ask the user if they would like to add it
    print("This link is not in the database.")
    if input("Would you like to add it? ").strip().lower() in ["y", "yes"]:
        fileName = downloadURL(url)
        addData(url, md5(fileName), fileName.split("\\")[-1], getFileSize(fileName))
        writeData()
        exit()
    else:
        if input("Would you like to download the file anyway?").strip().lower() in ["y", "yes"]:
            downloadURL(url)
            exit()
        else:
            print("Goodbye.")
            exit()
if len(data[currentHash]) > 1:
    print("The following links are available for that file:")
    counter = 0
    for i in data[currentHash]:
        print(str(counter) + ". " + str(i))
else:
    print("that is the only link available for that file.")
if input("continue download? ").strip().lower() in ["y", "yes"]:
    downloadURL(url)
else:
    print("Goodbye.")
    exit()
