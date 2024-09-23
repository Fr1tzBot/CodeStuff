#!/usr/bin/env python3
import json
from statistics import multimode, mode

def most_frequent(List):
    return max(set(List), key = List.count)

with open("teams.json") as f:
    data = json.load(f)

allSponsors = []

for i in data:
    for j in data[i]:
        allSponsors.append(j)

allSponsors.sort()
allSponsors = list(filter(None, allSponsors))

for i in range(len(allSponsors)):
    allSponsors[i] = allSponsors[i].lower().replace(" ", "")

# commonSponsors = [
#     "nasa", #656 teams
#     "#39", #613 teams
#     "family", #395 teams
#     "community", #393 teams
#     "jcpenney", #272 teams
#     "boeing", #234 teams
#     "lockheedmartin", #197 teams
#     "baesystems", #178 teams
#     "solidworks", #172 teams
#     "theboeingcompany", #162 teams
#     "texasworkforcecommission", #157 teams
#     "argosyfoundation", #130 teams
#     "dodstem", #116 teams
#     "google", #112 teams
#     "qualcomm", #97 teams
#     "genehaasfoundation", #95 teams
#     "generalmotors", #90 teams
#     "fordmotorcompany", #86 teams
#     "s", #80 teams
#     "michigandepartmentofeducation", #79 teams
#     "3m", #77 teams
#     "rockwellautomation", #75 teams
#     "raytheon", #75 teams
#     "microsoft", #70 teams
#     "intuitivefoundation", #66 teams
#     "medtronic", #64 teams
#     "apple", #63 teams
#     "johndeere", #63 teams
#     "srt", #55 teams
#     "toyota", #55 teams
#     "autodesk", #52 teams
#     "ptc", #52 teams
#     "leidos", #51 teams
#     "homeschool", #50 teams
#     "4-h", #49 teams
#     "comcast", #48 teams
#     "first", #46 teams
#     "bosch", #45 teams
#     "fcafoundation", #44 teams
#     "ospi", #44 teams
#     "northropgrumman", #44 teams
#     "stateofmichigan", #43 teams
#     "bostonscientific", #43 teams
#     "neighborhoodgroup", #40 teams
#     "ford", #39 teams
#     "firstintexas", #39 teams
#     "pratt", #37 teams
#     "stateofflorida", #36 teams
#     "teconnectivity", #35 teams
#     ">", #35 teams
#     "departmentofdefense", #32 teams
#     "fastenal", #31 teams
#     "picatinnyarsenal", #31 teams
#     "abbott", #30 teams
#     "dow", #30 teams
#     "collinsaerospace", #30 teams
#     "kcstemalliance", #29 teams
#     "bechtel", #29 teams
#     "#34", #28 teams
#     "conedison", #28 teams
#     "bayer", #27 teams
#     "tesla", #27 teams
#     "nationalinstruments", #27 teams
#     "schneiderelectric", #26 teams
#     "novelis", #26 teams
#     "siemens", #26 teams
#     "johnson", #25 teams (johnson & johnson)
#     "bezosfamilyfoundation", #25 teams
#     "associates", #25 teams
#     "americanelectricpower", #24 teams
#     "c", #24 teams
#     "motorolasolutionsfoundation", #24 teams
#     "bloomberg", #24 teams
#     "intel", #24 teams
#     "intuitivesurgical", #24 teams
#     "comcastnbcuniversal", #23 teams
#     "aep", #23 teams
#     "argosy", #23 teams
#     "bestbuy", #23 teams
#     "dukeenergy", #23 teams
#     "ndep", #22 teams



# ]

# for j in commonSponsors:
#     allSponsors = [i for i in allSponsors if i != j]

while len(allSponsors) > 0:
    common = most_frequent(allSponsors)
    print(common + ": " + str(allSponsors.count(common)))
    allSponsors = [i for i in allSponsors if i != common]


# print(len(allSponsors))

# frequent = most_frequent(allSponsors)
# print(frequent)
# print(allSponsors.count(frequent))
