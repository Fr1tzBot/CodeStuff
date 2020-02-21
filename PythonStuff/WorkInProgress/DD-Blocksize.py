from os import system
import subprocess

#system("sudo updatedb")
DDpath = subprocess.getstatusoutput("locate DD-Blocksize.sh")[1]
speds = []
sudo = True
print(DDpath)
if sudo:
	speds = subprocess.getstatusoutput("sudo " + DDpath)
else:
	speds = subprocess.getstatusoutput(DDpath)
speds = speds[1]
sped2 = list([])
for i in range(len(speds)):
	if i in range(32):
		continue
	else:
		print(str(speds[i]))
		sped2 = sped2.extend(str(speds[i]))
	#print(str(speds[i]))
	#print(i)
print(speds2)
print(type(speds))
