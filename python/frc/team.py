#!/usr/bin/env python3.10
"""Ported team.sh to python"""
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

rawSocial = json.loads(apiCall("team/frc" + argv[0] + "/social_media"))
def parseSocial(socialType: str) -> str:
    foreignKey = ""
    for i in rawSocial:
        if i["type"] == socialType:
            foreignKey =  i["foreign_key"]
            break
    if foreignKey == "":
        return ""
    #haha funny switch statement will break on non 3.10 python versions :D
    match socialType:
        case "youtube-channel":
            return "https://www.youtube.com/channel/" + foreignKey
        case "twitter-profile":
            return "https://www.twitter.com/" + foreignKey
        case "instagram-profile":
            return "https://www.instagram.com/" + foreignKey
        case "facebook-profile":
            return "https://www.facebook.com/" + foreignKey
        case "github-profile":
            return "https://www.github.com/" + foreignKey
        case "linkedin-profile":
            return "https://www.linkedin.com/" + foreignKey
        case "twitch-channel":
            return "https://www.twitch.tv/" + foreignKey
        case default:
            return ""
def copy(text: str) -> None:
    subprocess.run("pbcopy", universal_newlines=True, input=text)

teamData = json.loads(apiCall("team/frc" + argv[0]))
for i in ["nickname", "rookie_year", "tba", "website"]:
    if i == "tba":
        j = "https://www.thebluealliance.com/team/" + argv[0]
        print("TBA Link: " + j)
        copy(j)
    else:
        j = str(teamData[i])
        print(i + ": " + j)
        copy(j)
        
    input()
for i in ["youtube-channel", "twitter-profile", "facebook-profile", "instagram-profile", "github-profile"]:
    j = parseSocial(i)
    print(i + ": " + j)
    copy(j)
    input()
