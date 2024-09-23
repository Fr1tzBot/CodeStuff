#!/usr/bin/env python3
"""grabs the average number of cap banners for each year at and event and averages them"""
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

def getCapCount(team: str) -> int:
    awards = json.loads(apiCall("/team/" + team + "/awards"))
    count = 0
    for k in awards:
        if k["award_type"] == 0:
            count += 1
    return count

def getEventCap(event: str) -> int:
    """Get the cap average of an event."""
    teams = json.loads(apiCall("/event/" + event + "/teams"))
    if type(teams) == dict:
        print("Skipped", event)
        return 0
    capCount = 0
    for j in teams:
        capCount += getCapCount(j["key"])
    print("Completed", event)
    return capCount/len(teams)

for i in argv:
    capYears = []
    for j in range(2002, 2023):
        eventName = str(j) + str(i)
        capYears.append(getEventCap(eventName))
    count2 = 0
    for l in capYears:
        if l > 0:
            count2 += 1
    print(i, "Cap Strength:", round(sum(capYears)/count2, 6))
