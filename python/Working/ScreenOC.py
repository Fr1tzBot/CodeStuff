#Overclocking Program
from os import system
import subprocess
import subprocess
from time import sleep
#set defaults
xres = 1366
yres = 768
ref = 60
def SetRef(NewRef, Interface): #function to set refresh rate
	command = str("~/cvt12" + " " + str(xres) + " " + str(yres) + " " + str(NewRef))
	cvt12 = (subprocess.getstatusoutput(command))
	cvt12 = cvt12[1]
	cvt = ""
	for i in range(cvt12.find('"'), (len(cvt12))):
		cvt = cvt + cvt12[i]
	print("Mode '" + cvt + "' Preparing to config...")
	system("xrandr --newmode " + cvt)
	rb2 = ""
	for i in range(len(str(xres)) + len(str(yres)) + len(str(NewRef)) + 7):
		rb2 = rb2 + cvt[i]
	print(rb2)
	system("xrandr --addmode " + Interface + " " + rb2)
	system("xrandr --output " + Interface + " --mode " + rb2)
def CheckInterfaces():
	command = "xrandr | grep -Pio '.*?\sconnected'"
	o = subprocess.getstatusoutput(command)
	o = o[1].split()
	for i in range(len(o)):
		if o[i] == "connected":
			del o[i]
	return o
def Reset(Interface):
	system("xrandr --output Interface --auto")
print("Welcome to Screen Overdrive beta 1.1!")
print("Currently Connected Interfaces:")
print(CheckInterfaces())
if len(CheckInterfaces()) == 1:
	oneDisplay = True
while True:
	
	if not oneDisplay:
		ocInterface = input("Which Display Would You Like To Overclock?")
		print(ocInterface)
	else:
		ocInterface = CheckInterfaces()[0]
	
	if ocInterface not in CheckInterfaces() and not ocInterface == CheckInterfaces()[0]:
		continue
	else:
		targetOC = input("What Refresh rate Would You Like to Overclock To?")									
		
		
		
		
		
		
		
		
		
		
		
		targetOC = int(targetOC)
		if type(targetOC) != int:
			continue
	if targetOC < ref:
		t = input("are you sure you wish to underclock your display? [y/n]")
		if t.lower() == "y" or t.lower() == "yes":
			pass
		else:
			continue
	break
SetRef(targetOC, ocInterface)
stable = input("Is this Stable? [y/n]")
if stable.lower() == "y" or stable.lower() == "yes":
	pass
else:
	Reset(ocInterface)
