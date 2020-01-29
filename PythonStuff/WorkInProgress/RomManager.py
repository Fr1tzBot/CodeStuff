from os import system as run
from time import sleep

active = True
consoleList = ("atari 800", "atari 2600", "atari 5200", "atari 7800", "atari jaguar", 
"atari lynx", "atari st", "atari xegs", 

"3ds", "ds", "family disk system", "gameboy", 
"gameboy advance", "gameboy color", "gamecube", "nintendo 64", 
"nintendo entertainment system", "super nintendo", "wii", "wii u", 

"final burn alpha", "intellivision", "neo geo", "neo geo pocket", "vectrex", "xbox" ) 
pathPrefix = "/mnt/Storage/Filez/Roms/"
pathSuffix = "/Romset/"
pathList = ("Atari/'Atari 800'", "Atari/'Atari 2600'", "Atari/'Atari 5200'", 
"Atari/'Atari 7800", "Atari/'Atari Jaguar'", "Atari/'Atari Lynx'", "Atari/'Atari ST'",
"Atari/'Atari XEGS'",

"Nintendo/DS", "Nintendo/Famicon", "Nintendo/GameBoy", "Nintendo/'GameBoy Advance'",
"Nintendo/'GameBoy Color'", "Nintendo/GameCube", "Nintendo/'Nintendo 64'", 
"Nintendo/Nintendo Entertainment System", "Nintendo/'Super Nintendo'", "Nintendo/Wii",
"Nintendo/'Wii U'"

"Other/'Final Burn Alpha'", "Other/Intellivision", "Other/'Neo Geo'", 
"Other/'Neo Geo Pocket'", "Other/Vectrex", "Other/Xbox")

testPath = "~/Desktop/RomDataBase/Roms Database/roms database/"
testList = ("NES", "Nintendo 64", "GameBoy")
test = True

def getConsoleID(consoleName):
    global test
    global consoleList
    global testList
    if test:
        if consoleName in testList:
            for i in range(len(testList)):
                if testList[i] == consoleName:
                    return i
        else:
            return "Error 43"
    else:
        if consoleName in consoleList:
            for i in range(len(consoleList)):
                if consoleList[i] == consoleName:
                    return i
        else:
            return "Error 43"
    

while active:
    #run
    #run("sudo /usr/libexec/locate.updatedb")
    console = input("What console is this rom for?")
    console = console.lower()
    consoleID = getConsoleID(console)
    print(consoleID)
    if console == "help":
        print("Error 43 - The console you typed is not on the console list")
        print("Solutions - avoid abbreviations and misspellings")
        sleep(2)
        continue
    elif console in consoleList and not test:
       print("good Yeet")
       query = input("What is the name of this ROM?")
       run("locate " + query)
       break 
    elif test:
        if console in testList:
            print("test yeet")
            sleep(1)
            break
    else:
        print("Error 43: console not found")
        print("Type help on the console input for more info.")
        sleep(2)
        print("Resetting...")
        sleep(2)
        print("")
        continue