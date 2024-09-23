#!/usr/bin/env python3.10
"""Ported team.sh to python"""
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

for i in argv:
    print(json.loads(apiCall("team/frc" + i))["nickname"])

