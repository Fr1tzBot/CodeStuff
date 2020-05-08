from gtts import gTTS
from os import system

fileList = list()

def generateFile(textInput):
    global fileList
    textInput = str(textInput)
    if not textInput in fileList:
        tts = gTTS(text=textInput, lang='en')
        tts.save(textInput + ".mp3")
        fileList.append(textInput)
        print("Had to Create TTS File.")
    else:
        print("TTS File Already Exists!")

def playFile(fileName):
    global fileList
    if not fileName in fileList:
        print("You Need To Generate the File First!")
    else:
        system("play '" + fileName + ".mp3'  > /dev/null 2>&1")

def tts(textInput):
    generateFile(textInput)
    playFile(textInput)
    
    

def cleanup():
    global fileList
    for i in fileList:
        system("rm '" + i + ".mp3'")
