from time import sleep

def scrollPrint(text, delay):
    for i in range(len(text)):
        print(text[:i+1], end = '\r')
        sleep(delay)
    print("\n")
    
def wordScroll(text, delay):
    currenttext = ""
    wordList = text.split()
    for word in wordList:
        currenttext = currenttext + word + " "
        print(currenttext, end = '\r')

        sleep(delay)
    print("\n")
    
scrollPrint("Hello World", 0.5)
wordScroll("Shall we play a game?", 1.5)
