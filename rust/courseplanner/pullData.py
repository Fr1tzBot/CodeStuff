#!/usr/bin/env python3

import sys
import requests
from selectolax.parser import HTMLParser
import json

class Constants:
    BASE = "https://www.banweb.mtu.edu"
    TERM_LIST = f"{BASE}/owassb/bzskfcls.p_sel_crse_search"
    SUBJ_LIST = f"{BASE}/owassb/bwckgens.p_proc_term_date"
    CLASS_LIST = f"{BASE}/owassb/bzckschd.p_get_crse_unsec"
    CLASS_DATA = {
        "term_in": None,
        "sel_subj": ["dummy"],
        "sel_day": "dummy",
        "sel_schd": ["dummy", "%"],
        "sel_insm": "dummy",
        "sel_camp": ["dummy", "%"],
        "sel_levl": ["dummy", "%"],
        "sel_sess": "dummy",
        "sel_instr": ["dummy", "%"],
        "sel_ptrm": ["dummy", "%"],
        "sel_attr": ["dummy", "%"],
        "sel_crse": "",
        "sel_title": "",
        "sel_from_cred": "",
        "sel_to_cred": "",
        "begin_hh": "0",
        "begin_mi": "0",
        "begin_ap": "a",
        "end_hh": "0",
        "end_mi": "0",
        "end_ap": "a",
    }
    SUBJ_DATA = {"p_calling_proc": "bzskfcls.P_CrseSearch"}

class Course:
    def __init__(self, data):
        self.url = data[0]
        self.crn = int(data[1])
        self.subject = data[2]
        self.number = data[3]
        self.section = data[4]
        self.campus = data[5]
        self.credits = data[6]
        self.name = data[7]
        self.days = data[8]
        self.time = data[9]
        self.capacity = int(data[10])
        self.used = int(data[11])
        self.remaining = int(data[12])
        self.instructor = data[13]
        self.date = data[14]
        self.location = data[15]
        self.fee = data[16]

def checkResponse(response: requests.Response) -> bool:
    if response.status_code == 200:
        return True

    print(f"Request to {response.url} failed with code {response.status_code}")
    sys.exit(1)

def scrapeData(name, text):
    tree = HTMLParser(text)
    vals = tree.css(f"select[name='{name}'] > option")
    tmp = {}
    for i in vals:
        text = i.text()
        value = i.attributes["value"]
        if value is None or text == "None":
            continue
        tmp[value] = text

    return tmp

def getTerms() -> dict:
    termRaw = requests.get(Constants.TERM_LIST)
    checkResponse(termRaw)

    return scrapeData("p_term", termRaw.text)

def getSubjs(term: str) -> dict:

    Constants.SUBJ_DATA["p_term"] = term
    subjList = requests.post(Constants.SUBJ_LIST, data = Constants.SUBJ_DATA)
    checkResponse(subjList)

    return scrapeData("sel_subj", subjList.text)


def getCourses(subj) -> list:
    Constants.CLASS_DATA["sel_subj"] = ["dummy", subj]
    classList = requests.post(Constants.CLASS_LIST, data = Constants.CLASS_DATA)
    checkResponse(classList)

    tree = HTMLParser(classList.text)
    vals = tree.css("table.datadisplaytable tr")

    courses = []

    for i in vals:
        cells = i.css("td")
        data = []
        for j in cells:
            if j.attributes["class"] == "ntdefault":
                continue
            if len(j.css("a")) > 0:
                data.append(Constants.BASE + j.css("a")[0].attributes["href"])
            data.append(j.text().strip())

        if len(data) == 17:
            courses.append(Course(data))
    return courses

def getInfo(course: Course) -> dict:
    classRaw = requests.get(course.url)
    checkResponse(classRaw)

    tree = HTMLParser(classRaw.text)
    vals = tree.css("ul li")
    for i in vals:
        print(i.attributes, i.text().split("\n"))

def prettyprint(adict) -> None:
    print(json.dumps(adict, indent = 4))

terms = getTerms()

Constants.TERM = list(terms.keys())[1]
print(Constants.TERM)

subjs = getSubjs(Constants.TERM)

Constants.SUBJ = list(subjs.keys())[0]
print(Constants.SUBJ)


Constants.CLASS_DATA["term_in"] = Constants.TERM


courses = getCourses("EE")
print(getInfo(courses[0]))

