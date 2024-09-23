import json
import base64
import zlib

def decode(raw: str) -> dict:
    #remove first byte
    raw = raw[1:]

    #decode base64
    decoded = base64.b64decode(raw)

    #decompress zlib level 9
    decompressed = zlib.decompress(decoded)

    return json.loads(decompressed)

def encode(data: dict) -> str:
    #compress json
    compressed = zlib.compress(json.dumps(data).encode(), 9)

    #encode base64
    encoded = base64.b64encode(compressed)

    #add first byte
    return "0" + encoded.decode()

#some quick tests
testString = "0eNqVkN0OgjAMhV+F9FoJPwOGr2KMAW3MktGRbaiE7N0t0+iF3njXc7rztd0CvZ5wtIo87JIF1MmQ42q/gFMX6nR0/TwiF6A8DrBJgLohaucN4fbWaQ2BbUVnvLOfhwMrJK+8whctqvlI09CjXd/8xrA7Gsc5Q3FyxFVSpBV3ZhaNrNMq8LRvZPEHsi7rN1KWYkWuO8cDOf75FDavaN0zXMhcNG3BO7RZmYkQHmw3YJ0="
assert encode(decode(testString)) == testString


class Blueprint:
    def __init__(self, raw: str):
        self.raw = raw
        self.data = decode(self.raw)
    def encode(self) -> str:
        return encode(self.data)
    def getVersion(self) -> int:
        return self.data["blueprint"]["version"]
    def getIcons(self) -> list:
        return self.data["blueprint"]["icons"]
    def getEntities(self) -> list:
        return self.data["blueprint"]["entities"]


blah = "0eNqlletuhCAQhd9lfuNG8Iqv0jSN65INKSIBbHaz8d2LbtNsK1up/DJ4Od+ZOXHmBkcxMqW5tNDcgHeDNNC83MDws2zFfM9eFYMGuGU9IJBtP5+YYJ3VvEt6Lrk8JyfNhYAJAZcndoEGT2hb46I0MyaxupVGDdomRybsgwiZXhEwabnl7O5qOVzf5NgfmXaULS0EajDu80HOLmZfZZYfCgRXaCpaHwoHO3HtalleIbPrXwyyh1H8j5HF1UEdw6Oaf6sa23bvCZeGaeue/O2Yhjgu9jgun3cl9zDKOAYNYVQxna/T1N/5Ok4V+1XpnjzvHjfzxOk+cRwkjmOS9FTgSxKTOAgOgmRxyRJ/sjhfyY5uBOqzHtw1RDhb3H+N2WG0apwH6RpU7IuZBMW8/mGNEtw+ky9/eN/qfBUXLwmC1BsL7u8uFWuGW2DL0mse9iyCD6bNvY01zitKqrqkaZbm0/QJCnl6cA=="
bp = Blueprint(blah)
render = []
minX = 999999999999
minY = 999999999999

for i in bp.getEntities():
    x = i["position"]["x"]
    y = i["position"]["y"]
    if x < minX:
        minX = x
    if y < minY:
        minY = y


maxY = 0
maxX = 0
for i in bp.getEntities():
    x = i["position"]["x"]-minX
    y = i["position"]["y"]-minY
    if y > maxY:
        maxY = int(y)
    if x > maxX:
        maxX = int(x)

for i in range(maxY+1):
    render.append([])
    for j in range(maxX+1):
        render[i].append(" ")

for i in bp.getEntities():
    x = i["position"]["x"]-minX
    y = i["position"]["y"]-minY
    render[int(y)][int(x)] = "#"


for i in render:
    for j in i:
        print(j, end="")
    print()

