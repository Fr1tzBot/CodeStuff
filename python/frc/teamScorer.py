#!/usr/bin/env python3
from textwrap import indent
import requests
import re
import json
from sys import argv
with open(".apiKey", "r") as f:
    apiKey = f.readlines()[0].strip()

class Trendline:
    def __init__(self, slope: float, intercept: float):
        self.slope = slope
        self.intercept = intercept
    def __str__(self):
        return str((self.slope, self.intercept))
    def __eq__(self, other: object) -> bool:
        return self.slope == other.slope and self.intercept == other.intercept
    def getM(self) -> float:
        return self.slope
    def getB(self) -> float:
        return self.intercept
    def predict(self, x: float) -> float:
        return self.getM()*x + self.getB()


class WLT:
    def __init__(self, w: int, l: int, t: int):
        self.w = w
        self.l = l
        self.t = t
    def __str__(self):
        return "-".join([str(self.w), str(self.l), str(self.t)])
    def __eq__(self, other: object) -> bool:
        return self.w == other.w and self.l == other.l and self.t == other.t
    def __float__(self):
        return self.w/(self.w+self.l+self.t)


def getYearList(teamNumber: int) -> list:
    years = []
    # print(json.loads(apiCall("/team/frc" + str(teamNumber) + "/years_participated")))
    for i in json.loads(apiCall("/team/frc" + str(teamNumber) + "/years_participated")):
        years.append(int(i))
    for i in [2015, 2020, 2021]:
        if i in years:
            years.remove(i)
    if 2002 in years:
        years = years[years.index(2002)+1:]
    return years

def apiCall(suffix: str) -> str:
    headers = {'X-TBA-Auth-Key': apiKey}
    base = "https://www.thebluealliance.com/api/v3/"
    return requests.get(base + suffix, headers=headers).text

def getWinLoss(teamNumber: int, year: int=2022, overall: bool=True) -> WLT:
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
    return WLT(search[0], search[1], search[2])

def getBanners(teamNumber: int, year: int=2022, chairmans:bool=False) -> int:
    awards = json.loads(apiCall("/team/frc" + str(teamNumber) + "/awards/" + str(year)))
    count = 0
    for i in awards:
        if i['award_type'] == 1 or (chairmans and i['award_type'] == 0):
            count += 1
    return count

def linReg(x: list, y: list) -> Trendline:
    assert len(x) == len(y)
    xy = []
    for i, val in enumerate(x):
        xy.append(x[i] * y[i])
    
    x_sqrt = [i**2 for i in x]
    n  = len(x)
    w = (n*sum(xy) - sum(x)*sum(y)) / (n*sum(x_sqrt) - sum(x)**2)
    b = (sum(y) - w*sum(x))/n
    return Trendline(w, b)

def percent(x: float) -> str:
    x*=100
    x = round(x, 2)
    return str(x)

def pretify(x: float) -> str:
    x = round(x, 2)
    return str(x)

assert Trendline(1, 0) == linReg([0,1,2,3], [0,1,2,3])
assert Trendline(1, 1) == linReg([0,1,2,3], [1,2,3,4])
assert Trendline(0, 1) == linReg([0,1,2,3], [1,1,1,1])
assert getWinLoss(254, 2018, False) == WLT(53, 0, 0)
assert getBanners(862, 2019, True) == 4

for i in argv[1:]:
    i = int(i)
    years = getYearList(i)
    wlt = []
    banners = []
    for j in years:
        winLoss = getWinLoss(i, j, False)
        bannerCount = getBanners(i, j, False)
        wlt.append(float(winLoss))
        banners.append(bannerCount)

    assert len(wlt) == len(years)
    assert len(banners) == len(years)

    print(str(i) + ":")
    wlt = linReg(range(len(years)), wlt)
    banners = linReg(range(len(years)), banners)
    print("    wlt:  growth:" + percent(wlt.getM()) +     " base:" + percent(wlt.getB()) +     " 23:" + percent(wlt.predict(len(years)+1)))
    print("    ban:  growth:" + pretify(banners.getM()) + " base:" + pretify(banners.getB()) + " 23:" + pretify(banners.predict(len(years)+1)))
