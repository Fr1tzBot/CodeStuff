from os import system
import subprocess

#system("sudo updatedb")
DDpath = subprocess.getstatusoutput("locate DD-Blocksize.sh")[1]
speeds = []
sudo = True #for debug, default True
print(DDpath)
if sudo:
	speeds = subprocess.getstatusoutput("sudo " + DDpath)
else:
	speeds = subprocess.getstatusoutput(DDpath)
speeds = speeds[1]
sped2 = list([])
for i in range(len(speeds)):
	if i in range(32):
		continue
	else:
		print(str(speeds[i]))
		sped2 = sped2.extend(str(speeds[i]))
	#print(str(speds[i]))
	#print(i)
print(sped2)
print(type(speeds))
