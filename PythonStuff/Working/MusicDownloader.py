import os                       #Used For file removing      #No Pip
from time import sleep          #Used For mp3 delays         #No Pip
import sys                      #Used for Arguments          #No Pip
import subprocess               #Used for Install            #No Pip
import shutil                   #Used for moving files       #pip install pytest-shutil
from googlesearch import search #Used For Google Searching   #pip install google
import youtube_dl               #Used To Download Videos     #pip install youtube_dl
import urllib, urllib.request   #Used To Get Youtube Info    #pip install urllib3
import json                     #Used To Handle Youtube Info #pip install jsonlib
from pydub import AudioSegment  #Used For Audio Conversion   #pip install pydub
import glob                     #Used For file detection     #pip install glob3
import vlc                      #Used For Audio Preview      #pip install python-vlc
from mutagen.mp3 import MP3     #Used For mp3 Handling       #pip install mutagen
import getpass                  #Used To Detect the User     #pip install micropython-getpass
#import musicbrainzngs           #Used to get Music Metadata  #pip install musicbrainzngs      #Not in use Right now

#Function to check if user is Root
def isRoot():
    if os.geteuid()==0:
        return True
    else:
        return False
#Function to plan an mp3 with vlc media player
def playMp3(mp3Name):
    #Play the Song with VLC
    print("Now Playing " + str(mp3Name))
    vlcSong = vlc.MediaPlayer(str(mp3Name))
    vlcSong.play()

    #Load the mp3 file into a variable
    mp3Audio = MP3(str(mp3Name))

    #Wait Until the Audio is Finished Playing
    try:
        sleep(float(mp3Audio.info.length))
    except KeyboardInterrupt:
        #Finish if the User Presses ctrl + c
        vlcSong.stop()
        print("\nGoodbye.")
        exit()
#Function to get the two letters after a number (1st, 2nd, 3rd...)
def afterNumber(i):
    stringI = str(i)
    if int(stringI[-1]) == 1:
        if not len(stringI) == 1:
            if not int(stringI[-2]+stringI[-1]) == 11:
                return "st"
            else:
                return "th"
        else:
            return "st"
    elif int(stringI[-1]) == 2:
        if not len(stringI) == 1:
            if not int(stringI[-2]+stringI[-1]) == 12:
                return "nd"
            else:
                return "th"
        else:
            return "nd"
    elif int(stringI[-1]) == 3:
        if not len(stringI) == 1:
            if not int(stringI[-2]+stringI[-1]) == 13:
                return "rd"
            else:
                return "th"
        else:
            return "rd"
    else:
        return "th"

#Define Youtube Functions
#Function to Get a dictionary containing info about a video
def getYoutubeInfo(url):
    global failOver
    global notFoundDict
    try:
        params = {"format": "json", "url": "https://www." + str(url)}
        embedURL = "https://www.youtube.com/oembed"
        query_string = urllib.parse.urlencode(params)
        embedURL = embedURL + "?" + query_string
        with urllib.request.urlopen(embedURL) as response:
            response_text = response.read()
            data = json.loads(response_text.decode())
        return data
    except:
        #failOver += 1
        #if failOver >= 5:
        return dict(notFoundDict)
        #getYoutubeInfo(url)

#Function to Download a Youtube Video
def YoutubeHandler(url):
    global failOver
    ydl_opts = {
        "extractaudio" : True,
        "format": "mp4",
        'quiet': True,
        "noplaylist" : True
    }
    #Fix the Occasional Failed Download by Calling the Function Again
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(["https://" + url])
    except:
        failOver += 1
        if failOver == 3:
            print("youtube-dl has failed 3 times")
            #Recommend updating youtube-dl
            print("Suggest running pip install -U youtube-dl")
        if failOver >= 5:
            print("Fatal Error: Youtube-dl Has Thrown Too Many Errors.")
            if input("Would You like to see the errors? \n> ").lower() in ("y", "yes"):
                raise
            exit()
        YoutubeHandler(url)

#Define Variables
domainWhitelist = ("youtube.com")     #List of domains accepted when creating list
searchList = list()                   #List to Be filled with acceptable urls without http prefixes
siteList = list()                     #List to be filled with list of acceptable domain names
httpList = list()                     #List to be filled with acceptable urls and their http prefixes
failOver = 0                          #Fail Protection int
notFoundDict = {"title": "Title Not Found", "author_name": "Author Not Found"}

#Introduce the program
print("Music Downloader v1.7")
print("Last Updated 7/24/20\n")

#Input Function For Song Title
songName = str(input("What is the Title of the Song You Would Like To Download? \n> "))

#Require That Some Input is Given
if songName == "":
    print("\nYou Must Enter A Title")
    exit()

#Input Function For Song Artist
artist = str(input("Who is the Artist of this Song? \n> "))

#Require That Some Input is Given
if artist == "":
    print("\nYou Must enter an artist")
    exit()

#Create Search Query
query = (songName + " by " + artist + " Official Audio")
print("Now Searching For: " + query)

#Perform Google Search
for i in search(query, tld="com", num=10, stop=10, pause=2):
    httpList.append(i)

#Add all items of the httpList to the searchlist
for i in httpList:
    searchList.append(i)

#Remove https and http at the beginning f addresses
for i in range(len(httpList)):
    searchList[i] = searchList[i].replace("https://www.", "")
    searchList[i] = searchList[i].replace("https://", "")
    searchList[i] = searchList[i].replace("http://www.", "")
    searchList[i] = searchList[i].replace("http://", "")

#Add all items of the httpless searchlist to sitelist
for i in searchList:
    siteList.append(i)

#remove slashes and all following values from sitelist addresses
deleteRest = False
for i in range(len(siteList)):
    for j in range(len(siteList[i])):
        if siteList[i][j] == "/":
            deleteRest = True
        if deleteRest:
            siteList[i] = siteList[i][:j]
            break
    deleteRest = False

        
#Replace Addresses Not in the Whitelist with Empty Strings
for i in range(len(siteList)):
    if siteList[i] not in domainWhitelist:
        siteList[i] = ""
        searchList[i] = ""
        httpList[i] = ""

#Remove Empty Strings
siteList = list(filter(None, siteList))
searchList = list(filter(None, searchList))
httpList = list(filter(None, httpList))

#Show User the Quantity of Results
if len(searchList) == 0:
    print("No Results Found.")
    exit()
if len(searchList) == 1:
    print(str(len(searchList)) + " Result Found")
else:
    print(str(len(searchList)) + " Results Found\n")

userReview = True #TODO Add Functionality to Automatically Pick Video

if userReview:
    #List Titles and Channels of all Found Videos
    for i in range(len(searchList)):
        print(str(i+1) + afterNumber(i+1) + " Video:")
        print(getYoutubeInfo(searchList[i])['title'])
        print(getYoutubeInfo(searchList[i])['author_name'] + '\n')

    #Ask User To Pick Best Video to Download
    try:
        videoChoice = int(input("Which Number Would You Like? (1-" + str(len(searchList)) + "): \n> ")) - 1
    except:
        print("You Must Enter A Number")
        exit()

    #Error Protection
    if videoChoice < 0:
        print("Please Enter A Positive number")
        exit()
    if videoChoice > (len(searchList)-1):
        print("Please Enter a number between 1 and " + str(len(searchList)))
        exit()

    #Download the Video the User Chooses
    YoutubeHandler(searchList[videoChoice])

    #Search for .mp4 Files in the Current Directory
    fileName = glob.glob("./*.mp4")
    if len(fileName) > 1:
        print("Please Run This Program In a Directory Without mp3, mp4, or webm files, as they may break it.")
        print("(AKA i'm too lazy to figure out the filename format youtube-dl uses)")
        exit()

    #Convert Those Files to .mp3
    print("Converting File '" + str(fileName[0].replace("./", "")) + "' To mp3...")
    convertedFilename = (fileName[0].replace(".mp4","") + ".mp3").replace("./", "")
    for i in fileName:
        AudioSegment.from_file(str(i)).export(str(convertedFilename), format="mp3")

    #Remove .webm files
    #print("Removing File '" + str(convertedFilename) + "'...")
    for i in fileName:
        os.remove(i)

    #Search for .mp3 Files in the Current Directory
    fileName = glob.glob("./*.mp3")

    #Move mp3 files to the music directory
    for i in fileName:
        getpass.getuser()
        shutil.move(str(i), ("/home/" + str(getpass.getuser()) + "/Music/" + convertedFilename))
        convertedFilename = "/home/" + str(getpass.getuser()) + "/Music/" + convertedFilename
    print("\nThe File Has Been Placed in Your Music Folder.")

    #Ask User if They Would Like to Listen to the Downloaded Song
    if str(input("\nWould You Like to Preview This Song? [Y/N] \n> ")).lower() in ["y", "yes"]:
        try:
            playMp3(convertedFilename)
        except:
            print("An Error Occured While Trying to Play this Song.")
        print("Goodbye.")
    else:
        print("Goodbye.")
