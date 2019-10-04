import os
from gtts import gTTS


def learn(word):
	tts = gTTS(text=word, lang='en')
	tts.save(os.path.join("temps/",("temp.mp3")))
def say(String):
	learn(String)
	os.system("play " + "~/Voice_Assistant/Voice_Assistant_Python/temps/temp.mp3")
print("Good Day And Welcome To the Text to Speech program of greatness!")
print("Created By Fritz geib on Monday, August 6th at 1:20 PM")
print("ONLINE MODE ACTIVE")
print("Version 2.1")


while True:
	In = str(raw_input(">>>"))
	if In == "Stop" or In == "stop":
		print("Abort.")
		break
	else:
		In = str(In)
		In = In.lower()
		say(In)
