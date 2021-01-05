try:
    import hashlib #Used to calculate file hashes
    import requests#Used to download files and to verify URLs
    import os      #Used for file sizes, os detection, current working directory, and some file management
    import pathlib #Used for some path management
    import json    #Used to manage data file
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

def verifyUrl(url):
    request = requests.get(str(url))
    return request.status_code == 200

def downloadURL(url):
    url = requests.utils.unquote(url)
    def getFileName(cd, url):
        if cd:
            return cd.split("filename=")[1]
        else:
            return url.split("/")[-1]
    r = requests.get(url)
    fileName = str(getFileName(r.headers.get('content-disposition'), url))
    open(str(os.getcwd() + "/" + fileName), 'wb').write(r.content)
    return str(os.getcwd() + "/" + fileName)

def getDataFile():
    if os.path.isfile(str(os.getcwd()) + "/data.json"):
        return str(os.getcwd()) + "/data.json"
    else:
        f = open(str(os.getcwd()) + "/data.json", "w+")
        f.write('{\n "links": {}\n}')
        f.close()
        return str(os.getcwd()) + "/data.json"

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
    

dataPath = getDataFile()
data = json.load(open(dataPath))
counter = 0

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
            print(str(counter) + ". " + str(i))
    else:
        print("that is the only link available for that file.")
    
    #Ask if the user would like to continue
    if input("continue download? ").strip().lower() in ["y", "yes"]:
        fileName = downloadURL(url)
        verifyHash(fileName, currentHash)
else:
    #If it isn't, ask the user if they would like to add it
    print("This link is not in the database.")
    if input("Would you like to add it? ").strip().lower() in ["y", "yes"]:
        fileName = downloadURL(url)
        addData(url, md5(fileName), fileName.split("/")[-1], getFileSize(fileName))
        writeData()
    else:
        if input("Would you like to download the file anyway?").strip().lower() in ["y", "yes"]:
            downloadURL(url)