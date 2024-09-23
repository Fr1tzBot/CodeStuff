#!/usr/bin/env python3
"""Ported getWinLoss.py to python"""
import json
from sys import argv
import requests
argv = argv[1:]
with open(".apiKey", "r") as f:
    apiKey = f.readlines()[0].strip()

def apiCall(suffix: str) -> str:
    headers = {'X-TBA-Auth-Key': apiKey}
    base = "https://www.thebluealliance.com/api/v3/"
    url = base + suffix
    return requests.get(url, headers=headers).text

def combineRecord(data: dict) -> str:
    l = 0
    w = 0
    t = 0
    for i in data.keys():
        for k in ["playoff", "qual"]:
            j = data[i][k]["ranking"] if k == "qual" else data[i][k]
            j = j["record"]
            l += j["losses"]
            w += j["wins"]
            t += j["ties"]
    return f"{w}-{l}-{t}"

print(combineRecord(json.loads(apiCall("/team/frc862/events/2022/statuses"))))
