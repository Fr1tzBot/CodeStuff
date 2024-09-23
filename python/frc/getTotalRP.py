#!/usr/bin/env python3
"""Gets the total Ranking Points for a given event."""

from sys import argv
import json
import requests
argv = argv[1:]
with open(".apiKey", "r") as f:
    apiKey = f.readlines()[0].strip()

def apiCall(suffix: str) -> str:
    """Makes an API call to The Blue Alliance."""
    headers = {'X-TBA-Auth-Key': apiKey}
    base = "https://www.thebluealliance.com/api/v3/"
    return requests.get(base + suffix, headers=headers).text

for i in argv:
    total = 0
    rawRanking = json.loads(apiCall("/event/" + str(i) + "/rankings"))
    assert rawRanking["extra_stats_info"][0]["name"] == "Total Ranking Points"
    for j in rawRanking["rankings"]:
        total += j["extra_stats"][0]
    print(str(i) + ": " + str(round(total/len(rawRanking["rankings"]), 2)))
