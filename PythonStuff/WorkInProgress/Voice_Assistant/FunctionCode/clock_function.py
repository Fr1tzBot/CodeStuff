import datetime

def Clock():
	now = datetime.datetime.now()
	h = str(now.hour)
	m = str(now.minute)
	t = h + ":" + m
	say(t)
Clock()
