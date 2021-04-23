from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
from time import time
import datetime

def formatUrl(badUrl):
    if not type(badUrl) == str:
        badUrl = str(badUrl)
    if not "www" in badUrl:
        badUrl = "www." + badUrl
    if not "http" in badUrl.split("/"):
        badUrl = "http://" + badUrl
    if not badUrl[-1] == "/":
        badUrl = badUrl + "/"
    goodUrl = badUrl
    return goodUrl

def verifyUrl(url):
    request = requests.get(str(url))
    return request.status_code == 200

def dirOnly(linkList):
    dirList = []
    for i in linkList:
        if i[-1] == "/":
            dirList.append(i)
    return dirList

def fileOnly(linklist):
    fileList = []
    for i in linklist:
        if i[-1] != "/":
            fileList.append(i)
    return fileList

def grabLinks(url):
    links = []
    parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
    resp = requests.get(url)
    http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
    html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
    encoding = html_encoding or http_encoding
    soup = BeautifulSoup(resp.content, parser, from_encoding=encoding)

    for link in soup.find_all('a', href=True):
        if "http" in link["href"]:
            links.append((link["href"]).split("?")[0])
        else:
            links.append((url + link["href"]).split("?")[0])
    return links

def recursiveGrabber(calledUrl):
    global urlList
    global recursions
    global url
    if len(calledUrl.split("//")) > 2:
        print("Multiple // detected in " + str(calledUrl))
        return
    if not calledUrl.split("/")[2] == url.split("/")[2]:
        print(calledUrl)
        print(url)
        print(str((calledUrl.split("/"))[2]) + " is not equal to " + str((url.split("/"))[2]))
    else:
        for i in grabLinks(calledUrl):
            if i[-1] == "/":
                if not ".." in i:
                    if verifyUrl(i):
                        recursions += 1
                        print("Recursion " + str(recursions) + ": " + str(requests.utils.unquote(i)))
                        recursiveGrabber(i)
                    else:
                        print("VerifyUrl failed: " + str(i))
            else:
                urlList.append(i)

recursions = 0
urlList = []
url = (input("Input Domain Name: "))


startTime = time()
recursiveGrabber(url)
endTime = time()
print("Website Scrape Time: " + str(datetime.timedelta(seconds=(endTime-startTime))))
print("Files: " + str(len(fileOnly(urlList))))
print("Dirs: " + str(recursions))
print("Total: " + str(recursions + len(fileOnly(urlList))))
if input("Do you want to see the file list? ").strip().lower() in ["y", "yes"]:
    for i in urlList:
        print(i)