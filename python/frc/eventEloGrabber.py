#!/usr/bin/env python3
"""analyzes the elo of an event over time"""
from sys import argv
import json
import requests
import datetime
import re
with open(".apiKey", "r") as f:
    apiKey = f.readlines()[0].strip()

argv = argv[1:]
headers = {'X-TBA-Auth-Key': apiKey}
YEAR = datetime.date.today().year

def apiCall(suffix: str) -> str:
    """Make an API call to Statbotics."""
    base = "https://api.statbotics.io/v1"
    url = base + suffix
    return requests.get(url, headers=headers).text


if not re.search("^20[0-9][0-9]", argv[0]) is None:
    print("Printing Single Event:")
    print(json.loads(apiCall("/event/" + argv[0]))[0]["elo_mean"])
else:
    print("Printing Multiple Events:")
    for i in argv:
        eloYears = []
        for j in range(2002, YEAR + 1): #this may break early in january, but it's fine
            eventName = str(j) + str(i)
            try:
                rawEvent = json.loads(apiCall("/event/" + eventName))
                if len(rawEvent) != 0:
                    eloYears.append(rawEvent[0]["elo_mean"])
            except KeyError:
                continue
        print(i, "Average:", round(sum(eloYears)/len(eloYears), 2))
