#!/usr/bin/env python3.10
"""Ported getTeamList.sh to python"""
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

def copy(text: str) -> None:
    subprocess.run("pbcopy", universal_newlines=True, input=text)

teamList = []
for i in json.loads(apiCall("event/" + argv[0] + "/teams/simple")):
    teamList.append(int(i["team_number"]))

teamList.sort()

for i in teamList:
    print(i)

copy("\n".join([str(i) for i in teamList]))
