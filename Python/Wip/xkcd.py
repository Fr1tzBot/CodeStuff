import random
from bs4 import BeautifulSoup
import requests
import os

from sys import argv

class MissingMetaError(Exception):
    pass
cache = {}

#Meta number Function
def getNumber(page: BeautifulSoup) -> int:
    """Get the comic number from the page metadata"""
    meta = page.find("meta", property="og:url")
    if meta:
        url = meta["content"]
    else:
        raise MissingMetaError
    url = url.split("/")
    for i in reversed(url):
        try:
            return int(i)
        except:
            continue

#Download managing functions
def downloadUrl(url: str) -> bytes:
    """Get the raw bytes of a url"""
    print("Sent get request for " + url)
    return requests.get(url).content
def writeBytes(fileName: str, contents: bytes) -> None:
    open(fileName, "wb").write(contents)
def downloadPage(comicNumber = 0) -> str:
    """Download the raw HTML of the XKCD homepage\n
    Setting the comicNumber to 0 will target the current comic"""

    global cache
    url = "https://xkcd.com/" 
    url += str(comicNumber) if comicNumber != 0 else ""
    if comicNumber in range(1, 1084):
        raise MissingMetaError("This style of grabbing image urls only works for the comics after #1083")
    if comicNumber in list(cache):
        print("Used cached URL: " + url)
        return cache[comicNumber]
    else:
        raw = str(downloadUrl(url))
        parsed = BeautifulSoup(raw, features="html.parser")
        cache[comicNumber] = parsed
        if comicNumber == 0:
            cache[getNumber(parsed)] = parsed
        return parsed

#Meta Functions
#This style of grabbing image urls only works for the comics after #1083
def getLatestNumber() -> int:
    """Get the number of the current comic"""
    return getNumber(downloadPage())
def getTitle(comicNumber: int) -> str:
    """Get the title from the page metadata"""
    parsed = downloadPage(comicNumber)
    title = parsed.find("meta", property="og:title")
    if title:
        return title["content"]
    else:
        raise MissingMetaError
def getImage(comicNumber: int) -> str:
    """Get the url for the comic image of a given comic number"""
    parsed = downloadPage(comicNumber)
    image = parsed.find("meta", property="og:image")
    if image:
        return image["content"]
    else:
        raise MissingMetaError

#Comic Downloading functions
def downloadComic(comicNumber: int, saveDir=os.getcwd()) -> None:
    """Download a given comic number"""
    filename = saveDir + "/" + getTitle(comicNumber) + ".png"
    writeBytes(filename, downloadUrl(getImage(comicNumber)))
def downloadRandomComic(saveDir=os.getcwd()) -> None:
    downloadComic(random.randint(1084, getLatestNumber()), saveDir)
def downloadLatestComic(saveDir=os.getcwd()) -> None:
    downloadComic(getLatestNumber(), saveDir)

downloadComic(argv[-1])