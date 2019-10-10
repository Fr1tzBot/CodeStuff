import time
import os

def play(Music):
	os.system("play " + Music + ".mp3")
def timer(hours = 0, minutes = 0, seconds = 0):
	totalseconds = hours/360 + minutes/60 + seconds
	now = time.time()
	future = now + totalseconds
	while time.time() < future:
		pass
	play("~/Desktop/Voice_AI/Effects/Alarm")

timer(0,0,10)
