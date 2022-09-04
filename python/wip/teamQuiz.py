import json
from random import choice
from os import system
from time import sleep
def formatTeamName(name: str) -> str:
    name = name.replace(" ", "").lower()
    if name.startswith("the"):
        name = name[3:]
    if name.endswith("robotics"):
        name = name[len(name)-8:]
    return name

def makeQuestion(teamInfo: str) -> bool:
    teamInfo = teamInfo.split(" ")
    teamInfo = [teamInfo[0], " ".join(teamInfo[1:])]
    answer = input("What team is #" + teamInfo[0] + "?\n> ")
    answer = formatTeamName(answer)
    return answer == formatTeamName(teamInfo[1])

teams = open("teamlist.txt", "r")
teamList = teams.read().split("\n")
teams.close()
while True:
    system("clear")
    team = choice(teamList)
    if makeQuestion(team):
        input("Correct!")
    else:
        input("Incorrect.\nThe correct answer was:\n" + team)

