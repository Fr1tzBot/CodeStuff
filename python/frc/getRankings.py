#!/usr/bin/env python3
"""Get rankings from TBA and print them in a CSV format."""
import json
from sys import argv
import requests
argv = argv[1:]
with open(".apiKey", "r") as f:
    apiKey = f.readlines()[0].strip()

def apiCall(suffix: str) -> str:
    """Make an API call to TBA."""
    headers = {'X-TBA-Auth-Key': apiKey}
    base = "https://www.thebluealliance.com/api/v3/"
    return requests.get(base + suffix, headers=headers).text

for j in argv:
    for i in json.loads(apiCall("/event/" + j + "/rankings"))["rankings"]:
        print(i["team_key"][3:] + "," + str(i["rank"]))
