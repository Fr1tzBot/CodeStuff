from gtts import gTTS
from os import system

fileList = list()

def generateFile(textInput, filename):
    global fileList
    textInput = str(textInput)
    if not textInput in fileList:
        tts = gTTS(text=textInput, lang='en')
        tts.save(filename + ".mp3")
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

text = "First, open the settings app. Then, click on the Desktop tab under the personal section. Then select a background from the provided options, or upload your own. Finally, click close and you will have successfully changed your background"
generateFile(text, "test")
