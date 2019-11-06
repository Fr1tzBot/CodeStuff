import os
from gtts import gTTS
import datetime
import time
def learn(word):
	tts = gTTS(text=word, lang='en')
	tts.save(os.path.join("temps/",("temp2.mp3")))
def say(String):
	learn(String)
	os.system("play " + "~/Voice_Assistant/Voice_Assistant_Python/temps/temp2.mp3")
def play(Music):
	os.system("play " + Music + ".mp3")
def clock():
	now = datetime.datetime.now()
	h = str(now.hour)
	m = str(now.minute)
	t = h + ":" + m
	say(t)
def timer(hours = 0, minutes = 0, seconds = 0):
	totalseconds = hours/360 + minutes/60 + seconds
	now = time.time()
	future = now + totalseconds
	while time.time() < future:
		pass
	play("~/Voice_Assistant/Voice_Assistant_Python/Effects/Alarm")
def volume(level):
	level = str(level)
	os.system("pactl set-sink-volume 0 " + level + "%")
