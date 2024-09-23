#!/usr/bin/env python3
from ast import arg
from sys import argv
import requests
import re
import json
with open(".apiKey", "r") as f:
    apiKey = f.readlines()[0].strip()

argv = argv[1:]

def apiCall(suffix: str) -> str:
    headers = {'X-TBA-Auth-Key': apiKey}
    base = "https://www.thebluealliance.com/api/v3/"
    url = base + suffix
    return requests.get(url, headers=headers).text

def getWinLoss(teamNumber: int, year: int=2022, overall: bool=True) -> float:
    """this is based on web scraping because win/loss ratios aren't availible from tba api"""
    base = "https://www.thebluealliance.com/team/"
    url = base + str(teamNumber) + "/" + str(year)
    page = requests.get(url)
    page = page.text
    if overall:
        try:
            search = re.search(r"\d{1,3}-\d{1,3}-\d{1,3}</strong> overall", page).group().split("<")[0].split("-")
        except AttributeError:
            search = re.search(r"<strong>\d{1,3}-\d{1,3}-\d{1,3}", page).group()[8:].split("-")    
    else:
        search = re.search(r"<strong>\d{1,3}-\d{1,3}-\d{1,3}", page).group()[8:].split("-")
    for i in range(len(search)):
        search[i] = int(search[i])
    
    try:
        return search[0]/(sum(search))
    except ZeroDivisionError:
        return 0.0

def getBanners(teamNumber: int, year: int=2022, chairmans:bool=False):
    awards = json.loads(apiCall("/team/frc" + str(teamNumber) + "/awards/" + str(year)))
    print(awards)

def getTeamList(compKey: str) -> list:
    teamList = json.loads(apiCall("/event/" + compKey + "/teams/keys"))
    for i in range(len(teamList)):
        teamList[i] = int(teamList[i].split("frc")[-1])
    return sorted(teamList)

def getSchedule(compKey: str) -> list:
    rawSchedule = json.loads(apiCall("/event/" + compKey + "/matches/simple"))
    schedule = []
    for i in rawSchedule:
        schedule.append({"blue": i["alliances"]["blue"]["team_keys"], "red": i["alliances"]["red"]["team_keys"]})

    for i in range(len(schedule)):
        for k in ["blue", "red"]:
            for j in range(len(schedule[i][k])):
                schedule[i][k][j] = int(schedule[i][k][j].strip("frc"))
    return schedule

def getWinner(matchKey: str) -> str:
    winner = json.loads(apiCall("/match/" + matchKey + "/simple"))["winning_alliance"]
    if winner == "blue":
        return "Blue Win"
    elif winner == "red":
        return "Red Win"
    else:
        return "Tie"



def predictMatch(blue: list, red: list) -> str:
    total = 0
    for i in blue:
        total += getWinLoss(i)
    blue = total/len(blue)

    total = 0
    for i in red:
        total += getWinLoss(i)
    red = total/len(red)

    if red > blue:
        return "Red Win"
    elif blue > red:
        return "Blue Win"
    elif blue == red:
        return "Tie"
    else:
        raise TypeError

def predictComp(compKey: str) -> list:
    predictions = []
    for i in getSchedule(argv[0]):
        predictions.append(predictMatch(i["blue"], i["red"]))
    return predictions

def listComp(compKey: str) -> list:
    matches = []
    matchKeys = json.loads(apiCall("/event/" + compKey + "/matches/keys"))
    for i in matchKeys:\
        matches.append(getWinner(i))
    return matches

getBanners(862)
# getWinLoss(862)