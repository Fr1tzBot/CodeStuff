from time import sleep
import random

target = 50
Kp = 5
data = 0
isOn = False
error = 0

def getData():
    global data
    if random.randint(0, 100) == 69:
        print("NOICE!")
        data = data * 2
        if data > 100:
            data = 100
    elif isOn:
        if random.randint(1, 2) == 1:
            data += 1
        else:
            data += 2
    elif data == 0:
        pass
    else:
        data -= random.randint(1, 2)
    return data
def setCondition(error, Kp):
    global isOn
    calc = Kp*error
    if calc > 0:
        isOn = True
    elif calc < 0:
        isOn = False
while True:
    error = target - getData()
    setCondition(error, Kp)
    print("E: " + str(error) + " On?: " + str(isOn) + " Data: " + str(data))
    if data < 0 or data > 100:
        print("Out Of Bounds Error 969")
        exit()
    sleep(0.1)
    
