import json
links = list()
with open("C:/Users/Fritz/Downloads/chrome_bookmarks.json") as f:
    data = json.load(f)
for i in range(len(data)):
    if data[i]["parentId"] == "1" and not i == 0:
        break 
    elif i != 0:
        links.append(data[i]["url"])
for i in links:
    print(i)
