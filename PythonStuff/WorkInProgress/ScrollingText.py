from time import sleep

def scrollPrint(text, delay):
    letterList = []
    for i in range(len(text)):
        letterList.append(text[i])
    for i in range(len(text)):
        sleep(delay)
        print(letterList[i], end="")
    print("\n")
def wordScroll(text, delay):
    wordList = text.split()
    for i in wordList:
        sleep(delay)
        print(i + " ", end="")
    print("\n")
scrollPrint("Galbert", 0.5)
wordScroll("Shall we play a game?", 1.5)
