from tinytag import TinyTag, tinytag
from sys import argv
from os import listdir
from pathlib import Path
from shutil import copyfile

def createDirs(tag: tinytag.Flac):
    if tag.albumartist != None:
        fullPath = outputPath + tag.albumartist + "/" + tag.album
    else:
        fullPath = outputPath + tag.artist + "/" + tag.album
    Path(fullPath).mkdir(parents=True, exist_ok=True)
    return str(fullPath)

def forceTwoDigit(number: int) -> str:
    number = str(number)
    if len(number) >= 2:
        return number
    else:
        while len(number) < 2:
            number = "0" + number
        return number
        

def getOutputName(tag: tinytag.Flac):
    outName = ""
    if tag.disc_total != None:
        if tag.disc_total > 1:
            outName += str(tag.disc) + "-"

    outName += forceTwoDigit(tag.track)
    outName += " "
    outName += tag.title
    outName += ".flac"

    return outName
    

    

if len(argv) >= 3:
    inputPath = argv[1]
    outputPath = argv[2]
else:
    inputPath =  input("Enter input path: ")
    outputPath = input("Enter output path: ")

if inputPath[-1] != "/":
    inputPath += "/"

if outputPath[-1] != "/":
    outputPath += "/"

for i in listdir(inputPath):
    if i.endswith(".flac"):
        try:
            tag = TinyTag.get(inputPath + i)
            copyfile(inputPath + i, (createDirs(tag) + "/" + getOutputName(tag)))
        except tinytag.TinyTagException:
            print("Error reading file: " + inputPath + i)
        except TypeError:
            print("Missing information in file: " + inputPath + i)