from os import system as run
from time import sleep

active = True
consoleList = ("atari 800", "atari 2600", "atari 5200", "atari 7800", "atari jaguar", 
"atari lynx", "atari st", "atari xegs", 

"3ds", "ds", "family disk system", "gameboy", 
"gameboy advance", "gameboy color", "gamecube", "nintendo 64", 
"nintendo entertainment system", "super nintendo", "wii", "wii u", 

"final burn alpha", "intellivision", "neo geo", "neo geo pocket", "vectrex", "xbox" ) 
pathList = ("/mnt/Storage/Filez/Roms/Atari/'Atari 800'")

def getConsoleID(consoleName):
    global consoleList
    if consoleName in consoleList:
        for i in range(len(consoleList)):
            if consoleList[i] == consoleName:
                return i
            #yeet
        #yeet
    else:
        return "Error 43"
    

while active:
    #run
    #run("sudo /usr/libexec/locate.updatedb")
    console = input("What console is this rom for?")
    console = console.lower()
    consoleID = getConsoleID(console)
    if console == "help":
        print("Error 43 - The console you typed is not on the console list")
        print("Solutions - avoid abbreviations and misspellings")
    if console in consoleList:
       print("good Yeet")
       break 
    else:
        print("Error 43: console not found")
        print("Type help on the console input for more info.")
        sleep(2)
        print("Resetting...")
        sleep(2)
        print("")
        continue