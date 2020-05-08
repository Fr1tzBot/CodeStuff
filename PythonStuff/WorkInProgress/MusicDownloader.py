from googlesearch import search 

#define variables
domainWhitelist = ("youtube.com, archive.org")
domainBlacklist = ("en.wikipedia.org", "amazon.com")
searchList = list()
siteList = list()
deleteRest = bool()

#input Functions
songName = input("What is the Title of the Song You Would Like To Search For? ")
artist = input("Who is the Artist of this Song? ")
print("\n")

#create search query
query = (songName + " by " + artist + " mp3 download")

#make searchlist from search function
for i in search(query, tld="com", num=10, stop=10, pause=2):
    searchList.append(i)

#remove https and http at the beginning f adresses
for i in range(len(searchList)):
    searchList[i] = searchList[i].replace("https://www.", "")
    searchList[i] = searchList[i].replace("https://", "")
    searchList[i] = searchList[i].replace("http://www.", "")
    searchList[i] = searchList[i].replace("http://", "")

#add all items of searchlist to sitelist
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
    if siteList[i] in domainBlacklist:
        siteList[i] = ""
        searchList[i] = ""

#remove empty values
siteList = list(filter(None, siteList))
searchList = list(filter(None, searchList))

#(temporary) show user the search list
for i in searchList:
    print(i)
