#!/usr/bin/env python3
from sys import argv
import json
import requests
with open(".apiKey", "r") as f:
    apiKey = f.readlines()[0].strip()

argv = argv[1:]
headers = {'X-TBA-Auth-Key': apiKey}

def apiCall(suffix: str) -> str:
    """Make an API call to TBA."""
    headers = {'X-TBA-Auth-Key': apiKey}
    base = "https://www.thebluealliance.com/api/v3/"
    return requests.get(base + suffix, headers=headers).text

def getMedia(team: int, year: int) -> list:
    """Get the media for a team."""
    a = json.dumps(json.loads(apiCall("/team/frc" + str(team) + "/media/" + str(year))), indent=4)
    print(a)
    for i in a:
        try:
            # print(i["view_url"])
            pass
        except KeyError:
            continue
getMedia(862, 2014)