import json


data = {}

with open("vids.txt") as f:
    rawVids = f.read()

for i in rawVids.split("\n"):
    a = i.split(" ")
    year = a[0]
    number = a[1]
    a = i.split("~")
    video = "https://www.youtube.com/watch?v=" + a[-2]

    if not number in data:
        data[number] = {}
    if not year in data[number]:
        data[number][year] = []
    data[number][year].append(video)

print(json.dumps(data, indent=4))
