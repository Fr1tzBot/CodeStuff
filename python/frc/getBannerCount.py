#!/usr/bin/env python3
"""Ported getBannerCount.sh to python"""
import json
from sys import argv
import requests
import subprocess
argv = argv[1:]
with open(".apiKey", "r") as f:
    apiKey = f.readlines()[0].strip()


def apiCall(suffix: str) -> str:
    headers = {'X-TBA-Auth-Key': apiKey}
    base = "https://www.thebluealliance.com/api/v3/"
    url = base + suffix
    return requests.get(url, headers=headers).text

count = 0
for i in json.loads(apiCall("team/frc" + argv[0] + "/awards")):
    if i["award_type"] == 0:
        count += 1
print(count)


