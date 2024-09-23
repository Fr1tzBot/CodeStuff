#!/usr/bin/env python3
"""analyzes the elo of an event over time"""
from sys import argv
import json
import requests
with open(".apiKey", "r") as f:
    apiKey = f.readlines()[0].strip()

argv = argv[1:]
headers = {'X-TBA-Auth-Key': apiKey}

def apiCall(suffix: str) -> str:
    """Make an API call to Statbotics."""
    base = "https://api.statbotics.io/v1"
    url = base + suffix
    return requests.get(url, headers=headers).text

for i in argv:
    print(json.loads(apiCall("/team/" + i))[0]["elo_recent"])

"862 1322 3536 3655 5530 5567 5674 5702 6078 6548 6570 6591 6610 7056 7195 7220 7289 8374 8424"
