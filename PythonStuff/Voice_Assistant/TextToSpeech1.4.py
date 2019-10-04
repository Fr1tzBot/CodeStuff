import os
from gtts import gTTS


def learn(word):
	tts = gTTS(text=word, lang='en')
	tts.save(os.path.join("WordSave",(word + ".mp3")))
def say(String):
	if os.path.isfile('~/Desktop/Voice_AI/WordSave/' + String + ".mp3"):
		os.system("play " + "~/Desktop/Voice_AI/WordSave/" + String + ".mp3")
	else:
		learn(String)
		os.system("play " + "~/Desktop/Voice_AI/WordSave/" + String + ".mp3")
print("Good Day And Welcome To the Text to Speech program of greatness!")
print("Created By Fritz geib on Monday, August 6th at 1:20 PM")
print("Version 1.4")


while True:
	In = str(raw_input(">>>"))
	if In == "Stop" or In == "stop":
		print("Abort.")
		break
	else:
		In = str(In)
		In = In.lower()
		say(In)
