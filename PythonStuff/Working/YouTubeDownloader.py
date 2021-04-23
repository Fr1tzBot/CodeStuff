import json
from os import system

downloadFiles = list()
maxVal = 0
f = open("~/Downloads/chrome_bookmarks.json",)
bookmarks = json.load(f)
youtubeFolder = bookmarks[0]

print(youtubeFolder['title'] + " Folder Found.")
print(str(len(bookmarks)) + " Bookmarks Found")
print("Please Ensure That You Have Downloaded The Latest Bookmarks json File.\n")
for i in range(len(bookmarks)):
    if int(bookmarks[i]['index']) > 0:
        maxVal = i-1
        break
for i in range(1, maxVal+1):
    downloadFiles.append(bookmarks[i]['url'])

print("Downloading Files...")

for i in range(len(downloadFiles)):
    system("youtube-dl -f 22 " + str(downloadFiles[i]))
f.close

removeBookmark = str(input("Would You Like To Delete the BookMark Json? [y/n]"))
if removeBookmark == "y" or removeBookmark == "yes":
    system("rm ~/Downloads/chrome_bookmarks.json")
    print("Removed Bookmarks File")
    print("Goodybye.")
else:
    print("Goodybye.")