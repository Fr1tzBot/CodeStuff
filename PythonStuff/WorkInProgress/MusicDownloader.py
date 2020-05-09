from googlesearch import search #Used For Google Searching
import youtube_dl               #Used To Download Videos
import urllib.request           #Used To Get Youtube Info
import json                     #Used To Handle Youtube Info
import urllib                   #Used To Get Youtube Info
import os                       #Used For file detection
from pydub import AudioSegment  #Used For Audio Conversion
import glob                     #Used For file detection

#Utility Functions
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
def getYoutubeInfo(url):
    params = {"format": "json", "url": "https://www." + str(url)}
    embedURL = "https://www.youtube.com/oembed"
    query_string = urllib.parse.urlencode(params)
    embedURL = embedURL + "?" + query_string
    with urllib.request.urlopen(embedURL) as response:
        response_text = response.read()
        data = json.loads(response_text.decode())
    return data
def YoutubeHandler(url):
    ydl_opts = {
        "extractaudio" : True,
        "format": "bestaudio/best",
        "noplaylist" : True
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(["https://" + url])


#Define Variables
domainWhitelist = ("youtube.com")
videoChoice = int()
searchList = list()
siteList = list()
httpList = list()
deleteRest = bool()
userReview = bool()
userReviewString = str()
fileName = list()
convertedFilename = str()

#Input Functions
songName = str(input("What is the Title of the Song You Would Like To Search For? "))
if songName == None or songName == "":
    songName = "Welcome To the Jungle"
artist = str(input("Who is the Artist of this Song? "))
print("")
if artist == None or artist == "":
    artist = "Guns N Roses"

#Create Search Query
query = (songName + " by " + artist + " Official Audio")
print("Now Searching For: " + query)

#Perform Google Search
for i in search(query, tld="com", num=10, stop=10, pause=2):
    httpList.append(i)

#Add all items of the httpList to the searchlist
for i in httpList:
    searchList.append(i)

#remove https and http at the beginning f adresses
for i in range(len(httpList)):
    searchList[i] = searchList[i].replace("https://www.", "")
    searchList[i] = searchList[i].replace("https://", "")
    searchList[i] = searchList[i].replace("http://www.", "")
    searchList[i] = searchList[i].replace("http://", "")

#add all items of the httpless searchlist to sitelist
for i in searchList:
    siteList.append(i)

#remove slashes and all following values from sitelist adresses
for i in range(len(siteList)):
    for j in range(len(siteList[i])):
        if siteList[i][j] == "/":
            deleteRest = True
        if deleteRest:
            siteList[i] = siteList[i][:j]
            break
    deleteRest = False

        
#make adresses in the blacklist empty
for i in range(len(siteList)):
    if siteList[i] not in domainWhitelist:
        siteList[i] = ""
        searchList[i] = ""
        httpList[i] = ""

#remove empty values
siteList = list(filter(None, siteList))
searchList = list(filter(None, searchList))
httpList = list(filter(None, httpList))

#show user the quantity of results

if len(searchList) == 1:
    print(str(len(searchList)) + " Result Found")
else:
    print(str(len(searchList)) + " Results Found")
print("")

#Removed Until I add automated Video Picking
#ask the user if they would like to review the videos
#userReviewString = input("Would You Like To Review These Videos Yourself? [Y/N] ")
#print("")
#if userReviewString.lower() == "y" or userReviewString.lower() == "yes":
#    userReview = True
#else:
#    userReview = False
userReview = True

if userReview:
    #List all video info to user
    for i in range(len(searchList)):
        print(str(i+1) + afterNumber(i+1) + " Video:")
        print(getYoutubeInfo(searchList[i])["title"])
        print(getYoutubeInfo(searchList[i])["author_name"])
        print("")

    #Ask USer To Pick Best Video to Download
    videoChoice = int(input("Which Number Would You Like? (1-" + str(len(searchList)) + "): "))-1
    print("")

    #Download the Chosen Video
    print("Now Downloading " + searchList[videoChoice])
    YoutubeHandler(searchList[videoChoice])

    #Search For .webm Files
    fileName = glob.glob("./*.webm")

    #Convert Those Files to mp3
    print("Converting File '" + str(fileName[0].replace("./", "")) + "' To mp3")
    convertedFilename = fileName[0].replace(".webm","")
    for i in fileName:
        AudioSegment.from_file(str(i)).export((str(convertedFilename) + ".mp3"), format="mp3")

    #Remove .webm files
    print("Removing File '" + str(fileName[0].replace("./", "")) + "'")
    for i in fileName:
        os.remove(i)
else:
    pass