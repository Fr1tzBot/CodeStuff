from os import system as run

active = True
consoleList = ("atari 800", "atari 2600", "atari 5200", "atari 7800", "atari jaguar", "atari lynx", "atari st", "atari xegs", "3ds", "ds", "family disk system", "gameboy", "gameboy advance", "gameboy color", "gamecube", "nintendo 64", "nintendo entertainment system", "super nintendo", "wii", "wii u", "final burn alpha", "intellivision", "neo geo", "neo geo pocket", "vectrex", "xbox" ) 
pathList = ("/mnt/Storage/Filez/Roms/Atari/Atari")

def getConsoleID(consoleName):
    global consoleList
    if consoleName in consoleList:
        for i in range consoleList:
            if consoleList[i] == consoleName:
                return i
    else:
        return "Error 76"
    

while active:
    #run
    #run("sudo /usr/libexec/locate.updatedb")
    console = input("What console is this rom for?")
    console = console.lower()
    consoleID = getConsoleID(console)
    if console in consoleList:
        
    else:
        print("Error 43: console not found")
        print("type help on the console input for more info")
        continue