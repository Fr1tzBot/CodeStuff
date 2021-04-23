from time import sleep
#ax+by=c
#dx+ey=f
#y=(af-cd)/(ae-bd)
#x=(ce-bf)/(ae-bd)
a = float()
b = float()
c = float()
d = float()
e = float()
f = float()
x = float()
y = float()
print("welcome to the POI calculator")
print("this calculator works with the formulas ax+by=c and dx+ey=f")
while True:
	try:
		a = float(input("what is the value of a?"))
	except ValueError:
		print("you must enter a number")
		sleep(1)
		continue
	b = input("what is the value of b?")
	try:
		b = float(b)
	except ValueError:
		print("you must enter a number")
		sleep(1)
		continue
	c = input("what is the value of c?")
	try:
		c = float(c)
	except ValueError:
		print("you must enter a number")
		sleep(1)
		continue
	d = input("what is the value of d?")
	try:
		d = float(d)
	except ValueError:
		print("you must enter a number")
		sleep(1)
		continue
	e = input("what is the value of e?")
	try:
		e = float(e)
	except ValueError:
		print("you must enter a number")
		continue
	f = input("what is the value of f?")
	try:
		f = float(f)
	except ValueError:
		print("you must enter a number")
		sleep(1)
		continue
	break
if ((a*e)-(b*d)) == 0:
	x = "nan"
	y = "nan"
else:
	x = ((c*e)-(b*f))/((a*e)-(b*d))
	y = ((a*f)-(c*d))/((a*e)-(b*d))
print("Point of intersection is (" + str(x) + ", " + str(y) + ")")
