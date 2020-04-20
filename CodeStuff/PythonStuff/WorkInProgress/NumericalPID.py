from time import sleep
import time
import random
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

target = 50
Kp = 1
data = 0
Power = 0

def setPower(power):
    global Power 
    if power > 100:
        Power = 100
    elif power < -100:
        Power = 0
    else:
        Power = power
def getData():
    global data
    #if random.randint(0, 100) == 69:
        #print("NOICE!")
        #data = data * 2
        #if data > 100:
            #data = 100
    if Power == 0 and random.randint(0, 16) == 6:
        if data == 100:
            data -= random.randint(-3, -1)
            pass
        if data == 0:
            data += random.randint(1, 3)
            pass
        else:
            data += random.randint(-3, 3)
    else:
        data = Power + data
    return data
def setCondition(error, Kp):
    global Power
    setPower(Kp*error)
for i in range(1000):
    if i == 0:
        start_time = time.time()
    try:
        if int(i/100) > 0:
            target = random.randint(0, 100)
            print("YEET")
    except:
        pass
    error = target - getData()
    setCondition(error, Kp)
    print("E: " + str(error) + " Power?: " + str(Power) + " Data: " + str(data))
    if data < 0 or data > 100:
        print("Out Of Bounds Error 969")
        break
    #plt.plot(time.time() - start_time, data, 'o', color='black')
    plt.plot(i, data, '-ok')
    #sleep(0.1)
plt.show()
    
