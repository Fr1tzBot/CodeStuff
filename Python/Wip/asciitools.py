import colorama
def horizontalStretch(logo: str, stretchtimes: int=1) -> str:
    outlogo = []
    for i in logo.split("\n"):
        outlogo.append("")
        for j in i:
            outlogo[-1] += j+j
    logo = ""
    for i in outlogo:
        logo += i
        logo += "\n"
    if stretchtimes <= 1:
        return logo
    else:
        return horizontalStretch(logo, stretchtimes-1)

def verticalStretch(logo: str, stretchtimes: int=1) -> str:
    outlogo = []
    for i in logo.split("\n"):
        outlogo.append(i)
        outlogo.append(i)
    logo = ""
    for i in outlogo:
        logo += i
        logo += "\n"
    if stretchtimes <= 1:
        return logo.strip("\n")
    else:
        return verticalStretch(logo, stretchtimes-1)

def stretch(logo: str, x: int=1, y: int=1) -> str:
    logo = horizontalStretch(logo, x)
    logo = verticalStretch(logo, y)
    return logo
def scale(logo: str, scale: int=1) -> str:
    logo = horizontalStretch(logo, scale)
    logo = verticalStretch(logo, scale)
    return logo.strip("\n")

def colorChars(logo: str, char: str, color) -> str:
    return logo.replace(char, color+char+colorama.Style.RESET_ALL)

#logo = """    ███
#  #███##
# # ██   #
##  ██    #
## ██     #
# #██    #
# ███████
# █  █  ██"""
logo = """
                ████████████
                ████████████
        ####████████████########
        ####████████████########
    ####    ████████            ####
    ####    ████████            ####
####        ████████                ####
####        ████████                ####
####    ████████                    ####
####    ████████                    ####
    ####████████                ####
    ####████████                ####
    ████████████████████████████
    ████████████████████████████
    ████        ████        ████████"""

#logo = stretch(logo, 2, 1)
#logo = colorChars(logo, "█", colorama.Fore.LIGHTYELLOW_EX)
#logo = colorChars(logo, "#", colorama.Fore.LIGHTBLUE_EX)
#logo = logo.replace("█", "#")
#logo = colorChars(logo, "#", colorama.Back.BLUE)
print(logo.strip("\n"))
