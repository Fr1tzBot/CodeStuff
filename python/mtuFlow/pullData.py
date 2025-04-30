#!/usr/bin/env python3

import sys
import json
import re
import requests
from selectolax.parser import HTMLParser

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

def get(url) -> HTMLParser:
    response = requests.get(url, timeout = 5)
    checkResponse(response)
    return HTMLParser(response.text)

def post(url, data) -> HTMLParser:
    response = requests.post(url, data, timeout = 5)
    checkResponse(response)
    return HTMLParser(response.text)

def checkResponse(response: requests.Response) -> bool:
    if response.status_code == 200:
        return True

    print(f"Request to {response.url} failed with code {response.status_code}")
    sys.exit(1)

def scrapeData(name, tree):
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
    return scrapeData("p_term", get(Constants.TERM_LIST))

def getSubjs(term: str) -> dict:
    Constants.SUBJ_DATA["p_term"] = term
    return scrapeData("sel_subj", post(Constants.SUBJ_LIST, Constants.SUBJ_DATA))


def getCourses(subj) -> list:
    Constants.CLASS_DATA["sel_subj"] = ["dummy", subj]
    tree = post(Constants.CLASS_LIST, Constants.CLASS_DATA)
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
    tree = get(course.url)
    vals = tree.css("ul li")
    for i, val in enumerate(vals):
        vals[i] = val.text()

    info = {}
    for i in vals:
        if "Credits" in i:
            info["credits"] = i.split("\n")[1]
        elif "Lec-Rec-Lab" in i:
            info["lrl"] = i.split("(")[1].strip(")\n").split("-")
        elif "Offered" in i:
            info["offered"] = i.split("\n")[-1].split(", ")
        elif "Requisite" in i:
            info["prereq"] = i.split(":")[1].replace("\n", "")
        elif "Restriction" in i:
            info["restrict"] = i.split(":")[1]
        else:
            print(f"No idea what to do with: {i.split(":")[0]}")
            continue
    return info

#Bugs here:
#classes that require special testing break
#classes that require pre-calc 1 classes can break
def checkPrereq(prereq, currentClasses, pastClasses) -> bool:
    if prereq == "":
        return True


    #force uppercase to ensure compatibility
    for i, course in enumerate(currentClasses):
        currentClasses[i] = course.upper()
    for i, course in enumerate(pastClasses):
        pastClasses[i] = course.upper()

    prereq = prereq.strip()

    classes = re.split(r' and | or ', prereq)
    andors = re.findall(f' or | and ', prereq)
    for i, val in enumerate(andors):
        andors[i] = val.strip()

    combined = []
    combined.append(classes[0])
    for i in range(len(andors)):
        combined.append(andors[i])
        combined.append(classes[i+1])


    toeval = ""

    for i, val in enumerate(combined):
        #first push or/and statements
        if val in ["or", "and"]:
            toeval += f" {val} "
            continue

        #then push all open parenthesis
        while val[0] == "(":
            toeval += " ( "
            val = val[1:]

        course = val.strip("(C)").strip(")").replace(" ", "").upper()

        if ">=" in val or ">" in val:
            print(f"Pushed 1 for {val}")
            toeval += " 1 "
        elif (course in pastClasses) or ("(C)" in val and course in currentClasses):
            toeval += " 1 "
        else:
            toeval += " 0 "

        val = val.replace("(C)", "")

        for i in range(val.count(")")):
            toeval += " ) "

    return bool(eval(toeval))

def prettyprint(adict) -> None:
    print(json.dumps(adict, indent = 4))

terms = getTerms()

Constants.TERM = list(terms.keys())[1]

subjs = getSubjs(Constants.TERM)


Constants.CLASS_DATA["term_in"] = Constants.TERM

currentClasses = ["ma2321", "ma3521", "un1015", "cs2311", "cs1142", "ph2200", "ph1200"]
pastClasses = ["cs1121", "eng1101", "ma1160", "cs1111",
               "ph1100", "ma2160", "eng1102", "ch1151", "ph2100"]

courses = getCourses("MA")
for i in courses:
    print(i.number)
    a = getInfo(i)
    if "prereq" in a:
        print(checkPrereq(getInfo(i)["prereq"], currentClasses, pastClasses))
    else:
        print(checkPrereq("", currentClasses, pastClasses))


